from iocorpus import read_corpus
from nltk.tokenize import word_tokenize

# arts = read_corpus('kompas_190223025615.txt')
arts = read_corpus('temp.txt')

class Word:
    def __init__(self, word):
        self.word = word
        self.freq = 1 #laplace smoothing
        self.probabilities = []
    
    def addFreq(self):
        self.freq += 1
        
    def addProbability(self, probability):
        self.probabilities.append(probability)
    
    def print(self):
        print(f'{self.word} \t: {self.freq}')
        
class Bigram:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
        self.freq = 1 #laplace smoothing
    
    def addFreq(self):
        self.freq += 1
    
    def print(self):
        print(f'{self.word1} {self.word2} \t: {self.freq}')

class Probability:
    def __init__(self, word, probability):
        self.word = word
        self.probability = probability

all_words = [] #array of string
word_freq = [] #array of Word (unique words)
bigrams = [] #array of [string, string]
bigram_freq = [] #array of Bigram

#get word frequency
def get_words_freq(words):
    print('Calculating word frequencies...')
    word_freq = []
    for i in words:
        found = False
        
        if len(word_freq)>0:
            for j in word_freq:
                if j.word==i:
                    j.addFreq()
                    found = True
                    break 
                
            if found==False:
                word_freq.append(Word(i))
        else:
            word_freq.append(Word(i))
    
    # for i in word_freq:
    #     i.print()
    return word_freq

#get freq of a word
def get_word_freq(word, word_freq):
    for i in word_freq:
        if i.word==word:
            return i.freq

#generate n-gram
def generate_ngram(words, n):
    l = []
    i = 0
    while i<len(words):
        l.append(words[i:i+n])
        i += 1
    l = l[:-1]
    return l

#tes bigram
# bigram = generate_ngram(word_tokenize(arts[0].sentences[0]), 2)
# for i in bigram:
#    print(i[0], "-",  i[1])


#get frequency of n-gram
def get_ngrams_freq(bigrams):
    print('Calculating n-gram frequencies...')
    bigram_freq = []
    for i in bigrams:
        found = False

        if(len(bigram_freq)>0):
            for j in bigram_freq:
                if j.word1==i[0] and j.word2==i[1]:
                    j.addFreq()
                    found = True
                    break 
                
            if found==False:
                bigram_freq.append(Bigram(i[0], i[1]))
        else:
            bigram_freq.append(Bigram(i[0], i[1]))
        
    # for i in bigram_freq:
    #     i.print()
    return bigram_freq
    
#get freq of a bigram
def get_bigram_freq(word1, word2, bigram_freq):
    freq = 1
    for i in bigram_freq:
        if i.word1==word1 and i.word2==word2:
            freq += i.freq
            break
    
    return freq
        
#calculate probability of bigram
def calculate_all_probability(word_freq, bigram_freq):
    print('Calculating probabilities...')
    for i in word_freq:
        for j in word_freq:
            if i.word!=j.word:
                f_bigram = get_bigram_freq(i.word, j.word, bigram_freq)
                
                prob = (f_bigram / i.freq)
                # print(prob)
                i.addProbability(Probability(j.word,prob))
    
    return word_freq
                
#get probability of 2 words
def get_probability(word1, word2, word_freq):
    prob = 0.001
    if any(x.word==word1 for x in word_freq) and any(x.word==word2 for x in word_freq):
        for i in word_freq:
            if i.word==word1:
                for j in i.probabilities:
                    if j.word==word2:
                        prob = j.probability
    
    return prob
    

#get next word (word with highest probability)
def get_next_word(sentence, word_freq):
    print('Generating next word...')
    tokens = word_tokenize(sentence)
    i = 0
    totalProb = 1
    
    #calculate probability from given sentence
    while i<len(tokens):
        if i==0:
            prob = get_probability("<s>", tokens[i], word_freq)
        else:
            prob = get_probability(tokens[i-1], tokens[i], word_freq)
         
        totalProb *= prob
        # print(prob)
        i += 1
    
    #calculate probability of possible next word
    nextWord = ""
    tempProb = 0
    
    for i in word_freq:
        prob1 = get_probability(tokens[len(tokens)-1], i.word, word_freq)
        # prob2 = get_probability(i.word, "</s>", word_freq)
        # if tempProb < prob1*prob2:
        #     tempProb = prob1*prob2
        #     nextWord = i.word
        # print(prob1, prob2)
        # print(prob1)
        if tempProb < prob1*totalProb:
            nextWord = i.word
            tempProb = prob1*totalProb
    
    totalProb *= tempProb
    
    print(f"Next word: {nextWord}")
    print(f"Probability: {totalProb}")
    print(f"Full sentence: {sentence} {nextWord}")


#main program
words = []
bigrams = []
for i in arts:
    for j in i.sentences:
        words = word_tokenize(j)
        words.insert(0, "<s>")
        words.append("</s>")
        
        for k in words:
            all_words.append(k)
            
        bigram = generate_ngram(words, 2)
        bigrams.extend(bigram)

word_freq = get_words_freq(all_words)
bigram_freq = get_ngrams_freq(bigrams)
word_freq_prob = calculate_all_probability(word_freq, bigram_freq)

#ask for input, return next word of that sentence
sentence = input("Enter a sentence: ")
get_next_word(sentence, word_freq_prob)
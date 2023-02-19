from iocorpus import read_corpus
from nltk.tokenize import word_tokenize

arts = read_corpus('kompas_190223025615.txt')

unique_words = []

#rata-rata kata per kalimat
len_sentence = []
for i in arts:
    for j in i.sentences:
        words = word_tokenize(j)
        len_sentence.append(len(words))
        
        #cari kata unik
        for k in words:
            if k not in unique_words and k.isnumeric()==False: unique_words.append(k)

avg_words = sum(len_sentence) / len(len_sentence)

#print('Jumlah kata per kalimat:', len_sentence)
print('Rata-rata jumlah kata per kalimat:', avg_words)

#rata-rata jumlah kalimat per dokumen
len_doc = []
for i in arts:
    len_doc.append(len(i.sentences))

avg_sentences = sum(len_doc) / len(len_doc)
#print('Jumlah kalimat per dokumen:', len_doc)
print('Rata-rata jumlah kalimat per dokumen:', avg_sentences)

#kata unik
#print('Kata unik:', unique_words)
print('Jumlah kata unik:', len(unique_words))
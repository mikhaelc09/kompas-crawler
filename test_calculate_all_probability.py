from languageModel import calculate_all_probability, get_ngrams_freq, get_words_freq

word_freq=get_words_freq(['kepala', 'pundak', 'lutut', 'kaki', 'lutut', 'kaki'])
bigram_freq=x = get_ngrams_freq([['kepala', 'pundak'], ['pundak', 'lutut'], ['lutut', 'kaki'], ['kaki', 'lutut'], ['lutut', 'kaki']])
x = calculate_all_probability(word_freq, bigram_freq)
for i in x:
    print("=================================")
    print(i.word)
    for j in i.probabilities:
        print("Word :", j.word.word)
        print("Word Frequency :", j.word.freq)
        print("Probability :", j.probability)
        # print("Word Probabilities :", j.word.probabilities)
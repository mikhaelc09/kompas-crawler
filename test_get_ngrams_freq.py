from languageModel import get_ngrams_freq

x = get_ngrams_freq([['kepala', 'pundak'], ['pundak', 'lutut'], ['lutut', 'kaki'], ['kaki', 'lutut'], ['lutut', 'kaki']])
for i in x:
    print(i.word1, i.word2, i.freq)
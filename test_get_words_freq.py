from languageModel import get_words_freq

x = get_words_freq(['kepala', 'pundak', 'lutut', 'kaki', 'lutut', 'kaki'])
for i in x:
    print(i.word, i.freq)
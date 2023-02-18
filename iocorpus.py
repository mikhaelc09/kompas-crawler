import datetime


def save_to_file(documents):
    today_date = datetime.datetime.now().strftime("%d%m%y%H%M%S")
    with open(f'kompas_{today_date}.txt','w') as f:
        f.write('<corpus>\n')
        for index, document in enumerate(documents):
            f.write(f'\t<doc id:{index} url={document.url}>\n')
            for sentence in document.sentences:
                f.write(f'\t\t<s>{sentence}</s>\n')
            f.write(f'\t</doc>\n')
        f.write('</corpus>')

def read_corpus(filename):
    with open(filename, 'r') as f:
        for i, x in enumerate(f):
            print(i,x)

import datetime
import re
from Article import Article

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
    articles = []
    with open(filename, 'r') as f:
        for i, x in enumerate(f):
            x = x.replace('\t', '')
            tag = x[1:x.find('>')]
            tokenized_tag = tag.split(' ')
        
            if(tokenized_tag[0][0] == '/') :
                pass
            elif(tokenized_tag[0] == 'corpus'):
                pass
            elif (tokenized_tag[0] == 'doc'):
                articles.append(Article(tokenized_tag[2][4:], []))
            elif (tokenized_tag[0] == 's'):
                sentence = x[x.find('>')+1:x.find('<',2)]
                articles[-1].sentences.append(sentence)

    return articles
            
            
arts = read_corpus('kompas_180223195900.txt')
for i in arts:
    print(i)
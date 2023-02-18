import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from iocorpus import save_to_file, read_corpus
import string
import re
from Article import Article

BASE_URL = "https://sorotpolitik.kompas.com/"

def get_articles(page):
    url = BASE_URL + ("/{page}" if page > 1 else "")
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find_all("a", {
        "class" : "article__link"
    })
    return content

def scrap_article(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find_all("div", {
        "class" : "read__content"
    })[0]
    para = content.find_all("p")

    return list(map(lambda x: x.text,para))

def remove_punctuation(source):
    result = "".join([c for c in source if c not in string.punctuation])
    return result

if __name__ == '__main__':
    corpus = []
    articles = get_articles(1)
    for index,article in enumerate(articles):
        # print(index,' : ',article.text)
        list_content = scrap_article(article.attrs["href"])
        #print(content)
        sentences = []
        for content in list_content:
            list_of_sentence = sent_tokenize(content)
            for sentence in list_of_sentence:
                sentence = sentence.replace(u'\xa0','')
                sentence = sentence.replace(u'\n','')
                sentence = remove_punctuation(sentence)
                sentence = re.sub(r'[^\w\s]', '', sentence)
                sentence = sentence.replace('  ',' ')
                sentences.append(sentence)
        
        art = Article(article.attrs["href"], sentences)
        corpus.append(art)
        print(index, ": ", art)

    save_to_file(corpus)
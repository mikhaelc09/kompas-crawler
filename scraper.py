import requests
from bs4 import BeautifulSoup

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

articles = get_articles(1)
for index,article in enumerate(articles):
    print(index,' : ',article.text)
    content = scrap_article(article.attrs["href"])
    print(content)
    
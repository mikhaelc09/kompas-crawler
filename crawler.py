import requests
from bs4 import BeautifulSoup

BASE_URL = "https://sorotpolitik.kompas.com/"

def get_articles(page):
    html = requests.get(BASE_URL).text
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
    for i, p in enumerate(para):
        if(i > 0 and len(p.text) > 0):
            print(i," : ",p.text)

    return para

# url = "https://sorotpolitik.kompas.com/memilih-pemimpin-negeri/read/2019/04/10/08470001/terbukti-jokowi-menaruh-harapan-besar-pada-pns-muda?utm_source=Kompas&utm_medium=Media&utm_campaign=Hasilketrampilan"
# scrap_article(url)

articles = get_articles(0)
for i,a in enumerate(articles):
    print(i,' : ',a.attrs['href'])
# https://github.com/Meinos10

import requests as req
from bs4 import BeautifulSoup

class Magazine():
    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    url = "https://www.sondakika.com/"

    def __init__(self):
        url = self.url
        header = self.header
        g = req.get(url+"magazin", headers=header).text
        self.soup = BeautifulSoup(g, "html.parser")
    
    def current_news(self):
        news = {
            "img": self.soup.find("a", {"class": "fr"}).img["data-original"],
            "title": self.soup.find("a", {"class": "content"}).span.text,
            "about": self.soup.find("p", {"class": "news-detail news-column"}).text
        }
        return news
    def news(self, limit: int=10):
        news = {}
        n = 1
        for i in self.soup.find_all("li", {"class": "nws"}):
            if n <= limit:
                news[n] = {
                    "img": i.find("a", {"class": "fr"}).img["data-original"],
                    "title": i.find("a", {"class": "content"}).span.text,
                    "about": i.find("p", {"class": "news-detail news-column"}).text
                }
            n+=1
        return news
# Developer: Meinos10

# https://www.sondakika.com/ 


import requests as req
from bs4 import BeautifulSoup as bf


class Sport:
    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    url = "https://www.sondakika.com/"

    def __init__(self):
        url = self.url
        header = self.header
        g = req.get(url+"spor", headers=header).text
        self.soup = bf(g, "html.parser")
    
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




#class SonDakika:
#    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
#
#    url = "https://www.sondakika.com/"
#
#    def title(self, limit: int=1):
#        url = self.url
#        header = self.header
#
#        requ = req.get(url, headers=header).text
#        sp = bf(requ, "html.parser")
#
#        title = ""
#        h = sp.find_all("a", {"class": "content"})
#        n = 1
#        for sport_title in h:
#            if n <= limit:
#                if limit == 1:
#                    title += sport_title.span.text
#                else:
#                    title += sport_title.span.text+"\n"
#            n+=1
#
#        return title
#
#
#    def about(self, limit: int=1):
#        url = self.url
#        header = self.header
#
#        requ = req.get(url, headers=header).text
#        sp = bf(requ, "html.parser")
#
#        about = ""
#        a = sp.find_all("p", {"class": "news-detail news-column"})
#        n = 1
#        for sport_about in a:
#            if n <= limit:
#                if limit == 1:
#                    about += sport_about.text
#                else:
#                    about += sport_about.text+"\n"
#            n+=1
#
#        return about
#    
#    def img(self, limit: int=1):
#        url = self.url
#        header = self.header
#        requ = req.get(url, headers=header).text
#        sp = bf(requ, "html.parser")
#        img = ""
#
#        m = sp.find_all("a", {"class": "fr"})
#        n = 1
#
#        for sport_img in m:
#            if n <= limit:
#                if limit == 1:
#                    img += sport_img.img["data-original"]
#                else:
#                    img += sport_img.img["data-original"]+"\n"
#            n+=1
#        
#        return img
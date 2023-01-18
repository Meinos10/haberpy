import requests as req
from bs4 import BeautifulSoup as bf


class Sport:
    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

    url = "https://www.sondakika.com/spor/"

    def title(self, limit: int=1):
        url = self.url
        header = self.header

        requ = req.get(url, headers=header).text
        sp = bf(requ, "html.parser")

        title = ""
        h = sp.find_all("a", {"class": "content"})
        n = 1
        for sport_title in h:
            if n <= limit:
                if limit == 1:
                    title += sport_title.span.text
                else:
                    title += sport_title.span.text+"\n"
            n+=1

        return title


    def about(self, limit: int=1):
        url = self.url
        header = self.header

        requ = req.get(url, headers=header).text
        sp = bf(requ, "html.parser")

        about = ""
        a = sp.find_all("p", {"class": "news-detail news-column"})
        n = 1
        for sport_about in a:
            if n <= limit:
                if limit == 1:
                    about += sport_about.text
                else:
                    about += sport_about.text+"\n"
            n+=1

        return about
    
    def img(self, limit: int=1):
        url = self.url
        header = self.header
        requ = req.get(url, headers=header).text
        sp = bf(requ, "html.parser")
        img = ""

        m = sp.find_all("a", {"class": "fr"})
        n = 1

        for sport_img in m:
            if n <= limit:
                if limit == 1:
                    img += sport_img.img["data-original"]
                else:
                    img += sport_img.img["data-original"]+"\n"
            n+=1
        
        return img
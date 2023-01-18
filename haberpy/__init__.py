# https://github.com/Meinos10

import requests as req
from bs4 import BeautifulSoup

class Haberler():
    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

    url = "https://www.sondakika.com/"
    


    def text(self, limit: int=1):
        url = self.url
        header = self.header
        requ = req.get(url, headers=header).text
        sp = BeautifulSoup(requ, "html.parser")
        text = ""
        h = sp.find_all("a", {"class": "active"})
        n = 1

        for haber in h:
            if n <= limit:
                text += haber.img["alt"]+"\n"
                n += 1
        return text

    def img(self, limit: int=1):
        url = self.url
        header = self.header
        requ = req.get(url, headers=header).text
        sp = BeautifulSoup(requ, "html.parser")
        img = ""
        h = sp.find_all("a", {"class": "active"})
        n = 1
        manset = 1
        for haber in h:
            if n <= limit:
                if manset == 1:
                    img += haber.img["src"]+"\n"
                else:
                    img += haber.img["data-original"]+"\n"
                n += 1
                manset += 1
        return img

    def text_and_img(self, limit: int=1):
        url = self.url
        header = self.header
        requ = req.get(url, headers=header).text
        sp = BeautifulSoup(requ, "html.parser")
        text = ""
        img = ""
        h = sp.find_all("a", {"class": "active"})
        n = 1
        manset = 1
        for haber in h:
            if n <= limit:
                text += haber.img["alt"]+"\n"
                if manset == 1:
                    img += haber.img["src"]+"\n"
                else:
                    img += haber.img["data-original"]+"\n"
                n += 1
                manset += 1
        return text, img

    
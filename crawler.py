import os
import sys
import requests
import urllib.request as ur
from bs4 import BeautifulSoup

def makeHtml(_str):
    _file = open("a.html","w")
    _file.write(_str)
    _file.close()

def downFile(url,name):
    ur.urlretrieve(url,name)

def spider(name):
    url = 'https://www.google.co.kr/search?q='+name+'&source=lnms&tbm=isch'# + str(page)
    print(url)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    makeHtml(soup.prettify())

    num = 0#len(os.listdir('./'+name))
    os.system('mkdir \"'+name+"\"")
    for link in soup.find_all("img"):
        if link.get('alt'):
            src = link.get('src')
            print(src)
            file_name = "./"+name+"/"+name + str(num)+".jpg"
            num += 1
            downFile(src,file_name)
            
if __name__ == "__main__":
    name = input("input name:")
    spider(name)
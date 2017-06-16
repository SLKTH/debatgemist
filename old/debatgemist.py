import html
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def getLinks(link, title):
    html = urlopen(link)
    bsObj = BeautifulSoup(html, "lxml")
    refList = []

    for link in bsObj.findAll("a", {"title": title}):
        if 'href' in link.attrs:
            a = link.attrs['href']
            print(a)
            refList.append(a)
    return refList



links = getLinks("http://debatgemist.tweedekamer.nl", "bekijk dit debat")
print(type(links))
print('----------------------------')
print(links)


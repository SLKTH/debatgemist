import html
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


class Collection:
    # URL from Debat Gemist
    collectionurl = "http://debatgemist.tweedekamer.nl"
    # Search query
    refattribute = "bekijk dit debat"

    # Retrieve HTML
    def getHTML():
        html = urlopen(Collection.collectionurl)
        return html

    # Iterate links and return list
    def getLinks():
        html = Collection.getHTML()
        bsObj = BeautifulSoup(html, "lxml")
        refList = []
        for link in bsObj.findAll("a", {"title": Collection.refattribute}):
            if 'href' in link.attrs:
                a = link.attrs['href']
                print(type(a))
                print(a)
                refList.append(a)
        return refList


# links = Collection.getLinks("http://debatgemist.tweedekamer.nl", "bekijk dit debat")
links = Collection.getLinks()

print(len(links))
# Output: 11

print(links)

# Output: ['/debatten/stemmingen-403',Collection  '/debatten/geannoteerde-agenda-europese-raad-24-en-25-maart',
# '/debatten/regeling-van-werkzaamheden-659', '/debatten/vaststelling-profielschets-nieuwe-voorzitter',
# '/debatten/be%C3%ABdiging-leden', '/debatten/be%C3%ABdiging-tijdelijke-voorzitter', '/debatten/mededelingen-726',
# '/debatten/afscheid-vertrekkende-leden-0', '/debatten/ontwerpprofielschets-nieuwe-voorzitter',
# '/debatten/commissie-geloofsbrieven', '/debatten/mededelingen-725']


from urllib.request import urlopen
from bs4 import BeautifulSoup

# VB: Enquetezaal_20170615170050_720p.mp4
# Link: http://debatgemistvod.download.kpnstreaming.nl/
# VB: http://debatgemistvod.download.kpnstreaming.nl/Enquetezaal_20170615170050_720p.mp4

# Download URL goes here (this might change)
VODURL = "http://debatgemistvod.download.kpnstreaming.nl/"


# Get all current debate links on main page
def getLinks(link, title):
    html = urlopen(link)
    bsObj = BeautifulSoup(html)
    refList = []

    for link in bsObj.findAll("a", {"title": title}):
        if 'href' in link.attrs:
            a = link.attrs['href']
            print(a)
            refList.append(a)
    return refList

# Get mp4 url from a specific debate URL
def getVideo(debatlink):
    html = urlopen(debatlink)
    vdObj = BeautifulSoup(html, "html.parser")
    reflist = []

    for video in vdObj.findAll("input", {"name": "debate_file_options"}):
        vidlink = video.attrs['value']
        return VODURL + vidlink


print(getVideo("https://debatgemist.tweedekamer.nl/debatten/auditdienst-rijk-adr-over-de-afronding-van-het-plan-van-aanpak-nvwa-en-de-uitvoering-van"))

# links = getLinks("http://debatgemist.tweedekamer.nl", "bekijk dit debat")
# print(type(links))
# print('----------------------------')
# print(links)

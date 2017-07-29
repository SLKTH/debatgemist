import html
import logging
from urllib.request import urlopen
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

class Collection:
    # URL from Debat Gemist
    dg_url = "https://debatgemist.tweedekamer.nl/plenaire-debatten"
    # Search query
    ref_attr = "bekijk dit debat"

    def __init__(self, page_count=1):
        self.ref_list = []
        self.html_resp = ""
        self.page_count = page_count

        self._handle_pages()

    def _handle_pages(self):
        for i in range(1, self.page_count):
            page_url = "%s?page=%d" % (
                Collection.dg_url.strip("/"),
                i
            )
            #print(page_url)
            self._get_html_resp(page_url)
            self._set_links()

    # Retrieve HTML
    def _get_html_resp(self, page_url):
        try:
            resp = urlopen(Collection.dg_url)
            self.html_resp = resp.read()
        except:
            logger.debug("Connection to remote site could not be established")

    # Extract video links from page
    def _set_links(self):
        bs = BeautifulSoup(self.html_resp, "lxml")
        for link in bs.findAll("a", {"title": Collection.ref_attr}):
            if 'href' in link.attrs:
                a = link.attrs['href']
                self.ref_list.append(a)

    # Return retrieven video links
    def get_links(self):
        return self.ref_list

    def __str__(self):
        return "\n".join(self.ref_list)

# from scrapy.crawler import Crawler
# from scrapy.utils import reactor

# crawler = Crawler(rocketu.settings)
# crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
# crawler.configure()
# crawler.crawl(spider)
import urllib2
from bs4 import BeautifulSoup
from scrapy.spider import BaseSpider
from rocketu.items import RocketuItem
from whoosh.index import create_in, open_dir
from whoosh.fields import *
import os


def open_writer():
    if not os.path.isdir("indexdir"):
        os.mkdir("indexdir")
        schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True))
        ix = create_in("indexdir", schema)
    else:
        ix = open_dir("indexdir")
    return ix.writer()


class RocketUSpider(BaseSpider):
    name = "rocketu"
    allowed_domains = ["http://127.0.0.1:8000/"]
    start_urls = [
        "http://127.0.0.1:8000/week1/1/",
        # "http://127.0.0.1:8000/week1/2/",
        # "http://127.0.0.1:8000/week1/3/",
        # "http://127.0.0.1:8000/week1/4_am/",

    ]
    # rules = [
    # Rule(SgmlLinkExtractor(), follow=True)
    # ]

    def parse(self, response):
        # writer = open_writer()
        cururl = response.url
        filename = response.url.split("/")
        file = filename[3]+filename[4]
        source = urllib2.urlopen(response.url).read()
        soup = BeautifulSoup(source)
        body = soup.find('div',id='classSlides')
        sections = body.find_all('section', recursive=0)
        page_number = 1
        page_down = 0
        for section in sections:
            sub = section.find_all('section', recursive=0)
            for each in sub:
                url = cururl+'#'+'/'+ str(page_number) + '/' + str(page_down)
                text = str(each)
                print url,'url'
                print page_down,'down'
                print page_number,'number'
                print each
                item = RocketuItem(text=text, page_url=url, page_number=page_number, page_down=page_down)
                yield item
                page_down+=1

            if len(sub)==0:
                url = cururl+'#'+'/'+ str(page_number) + '/' + str(page_down)
                text = str(section)
                print page_down,'down'
                print page_number,'number'
                print section,'single page'
                item = RocketuItem(text=text, page_url=url, page_number=page_number, page_down=page_down)
                yield item

            page_number+=1
            page_down = 0
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule
from scrapy.spider import BaseSpider
from scrapy.selector import  HtmlXPathSelector

from rocketu.items import RocketuItem

from bs4 import BeautifulSoup
import re



class RocketUSpider(BaseSpider):
    name = "rocketu"
    allowed_domains = ["http://127.0.0.1:8000/"]
    start_urls = [
        "http://127.0.0.1:8000/week2/1_am/#/",
        "http://127.0.0.1:8000/week1/1/",
        "http://127.0.0.1:8000/week3/1_am/"
    ]
    rules = [
        Rule(SgmlLinkExtractor(), follow=True)
    ]

    def parse(self, response):

        filename = response.url.split("/")[3]
        hxs = HtmlXPathSelector(response)
        divs = hxs.select('//div')
        sections = divs.select('//section').extract()
        for each in sections:
            soup = BeautifulSoup(each)
            #elements = soup.findAll("section".split())
            sections = soup.find_all('section')
            for each in sections: #iterate over loop [above sections]
           # print len(elements),'sublength'
                if each.find('section'):
                    continue
                else:
                    print each.prettify()
            #arylen = soup.findAll('section')
            #print arylen,'length of section'
           # res = re.search("    </section>", each)
            if len(elements ) > 1:
                for element in elements:
                    if len(element) > 1:
                        for subelement in element:
                            print subelement,'element'
                # for i in xrange(1,len(arylen)):
                #     subsection = soup.findNext('section')
                #     print subsection
                #     print "\n"
               # print res , 'This is res'
                # subs = divs.select('//section')
                # for sub in subs:
                #     print sub.extract()
            else:
                item = RocketuItem()
                item['html_content'] = each
                # title = each.select('//h2')
                # print title,'page title'
                # item['title'] = title
                print each
                yield item
        #     if len(each) > 1:
        #         for subsection in each:
        #             print subsection.extract()
        #     else :
        #         print each.extract
            #open(filename, 'wb').write(section)
        # for sel in selectors.xpath('//section/'):
        #     item = RocketuItem()
        #     item['title'] = sel.xpath('//h2/text()').extract()
         #   item['html_content'] = sel.xpath('//section/text()').extract()

            # item['link'] = sel.xpath('a/@href').extract()
            # yield item
        # filename = response.url.split("/")[3]
        # tree = html.fromstring(response.body).extract()
        # #data = response.body
        # section = tree.xpath('//section/text()')
        # print section
        # open(filename, 'wb').write(response.body)

import re
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from TatortScrape.items import TatortItem
from commonregex import CommonRegex

from tatort_fundus import Episode


def strip_it(stuff):
    if len(stuff) > 0:
        return stuff[0].strip()
    else:
        return ''


class TatortSpider(CrawlSpider):
    name = 'tatort'
    allowed_domains = ['tatort-fundus.de']
    start_urls = ['http://www.tatort-fundus.de/web/folgen/folgen-alphabetisch.html']
    rules = [Rule(SgmlLinkExtractor(allow='/web/'), callback='parse_episode', follow=True)]


    def parse_episode(self, response):
        #sel = Selector(response)
        episode = Episode(response.body_as_unicode())

        erstsendung = episode.erstsendung 

        if erstsendung:
            episodes = TatortItem()
            episodes['nummer'] = episode.episode_number.strip()
            #episodes['title'] = strip_it(sel.xpath('//table/tr/td/h1/text()').extract()) 
            episodes['titel'] = episode.title 
            episodes['drehbuch'] = episode.drehbuch.strip()
            episodes['idee'] = episode.idee.strip()
            episodes['regie'] = episode.regie.strip()
            episodes['sender'] = episode.sender.strip()
            episodes['firma'] = episode.firma.strip()
            episodes['drehzeit'] = episode.drehzeit.strip()
            episodes['drehort'] = episode.drehort.strip()
            episodes['bildformat'] = episode.bildformat.strip()
            episodes['redaktion'] = episode.redaktion.strip()
            episodes['erstsendung'] = episode.erstsendung.strip()
            episodes['quote'] = episode.quote.strip()
            episodes['darsteller'] = episode.actors
            
            return episodes
        else:
            pass

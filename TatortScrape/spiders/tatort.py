import re
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
#from scrapy.selector import Selector
from TatortScrape.items import TatortItem
from commonregex import CommonRegex
from tatort_fundus import Episode


#def strip_it(stuff):
#    if len(stuff) > 0:
#        return stuff[0].strip()
#    else:
#        return ''


class TatortSpider(CrawlSpider):
    name = 'tatort'
    allowed_domains = ['tatort-fundus.de']
    start_urls = ['http://www.tatort-fundus.de/web/index.php?id=7197&Nr=0',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=1',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=2',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=3',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=4',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=5',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=6',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=7',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=8',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=9',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=10',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=11',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=12',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=13',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=14',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=15',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=16',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=17',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=18',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=19',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=20',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=21',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=22',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=23',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=24',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=25',
                  'http://www.tatort-fundus.de/web/index.php?id=7197&Nr=26']
    rules = [Rule(SgmlLinkExtractor(allow='/web/'), callback='parse_episode', follow=True)]


    def parse_episode(self, response):
        #sel = Selector(response)
        episode = Episode(response.body_as_unicode())

        erstsendung = episode.erstsendung 

        if erstsendung:
            episodes = TatortItem()
            episodes['nummer'] = episode.episode_number.strip()
            #episodes['title'] = strip_it(sel.xpath('//table/tr/td/h1/text()').extract()) 
            episodes['titel'] = episode.title.strip() 
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

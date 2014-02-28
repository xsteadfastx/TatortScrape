from scrapy.item import Item, Field


class TatortItem(Item):
    nummer = Field()
    titel = Field()
    drehbuch = Field()
    idee  = Field()
    regie = Field()
    sender = Field()
    firma = Field()
    drehzeit = Field()
    drehort = Field()
    bildformat = Field()
    redaktion = Field()
    erstsendung = Field()
    quote = Field()
    darsteller = Field()

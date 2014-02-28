import re
import datetime
from bs4 import BeautifulSoup


class Episode(object):
    def __init__(self, response):
        self.response = response
        self.soup = BeautifulSoup(self.response)


    def _table_soup(self, info_item):
        """ soups the info box """
        soup = self.soup
        inhalt = soup.findAll('div', {'class': 'inhalt_folgen'})
        inhalt_extract = []

        try:
            for i in inhalt:
                inhalt_extract.append(i.text)

            for i in inhalt_extract:
                if i.startswith(info_item):
                    item_position = inhalt_extract.index(i)

                else:
                    pass

            return inhalt_extract[item_position+1]

        except Exception:
            return 'Keine Angaben'

    def _content_soup(self):
        """ soups the rest of the page informations """
        soup = self.soup
        inhalt = soup.findAll('div', {'id': 'lauftext'})
        inhalt_extract = []

        for i in inhalt:
            inhalt_extract.append(i.text)

        return inhalt_extract

    def _actors_soup(self):
        """ extracts the actors and put it into a list """
        soup = self.soup
        inhalt = soup.findAll('div', {'id': 'lauftext'})
        inhalt_extract = []

        for i in inhalt:
            inhalt_extract.append(i)

        actors_list = []

        for i in inhalt_extract[1].findAll('b'):
            actors_list.append(i.text)

        return actors_list

    @property
    def episode_number(self):
        soup = self.soup 
        number = re.findall(r"^\d\d\d", soup.title.text)
        return number[0]

    @property
    def title(self):
        return self.soup.findAll('h1')[0].text

    @property
    def drehbuch(self):
        return self._table_soup('Drehbuch:')

    @property
    def idee(self):
        return self._table_soup('Idee:')

    @property
    def regie(self):
        return self._table_soup('Regie:')

    @property
    def sender(self):
        return self._table_soup('Produktions- sender:')

    @property
    def firma(self):
        return self._table_soup('Produktionsfirma:')

    @property
    def drehzeit(self):
        return self._table_soup('Drehzeit:')

    @property
    def drehort(self):
        return self._table_soup('Drehort:')

    @property
    def bildformat(self):
        return self._table_soup('Bildformat:')

    @property
    def redaktion(self):
        return self._table_soup('Redaktion:')

    @property
    def erstsendung(self):
        return self._table_soup('Erstsendung:')

    @property
    def quote(self):
        return self._table_soup('Quote bei Erstsendung:')

    @property
    def actors(self):
        """ returns list of actors """
        actors = self._actors_soup()
        del actors[0] 
        return actors

    @property
    def summary(self):
        return self._content_soup()[0]

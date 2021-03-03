from abc import ABC, abstractmethod
from typing import List

from requests_html import HTMLSession

# from u import urls

urls = {
    'rodina': 'https://rodinakino.ru/schedule/',
    'mif': 'https://mythgallery.art/exibitions/',
    'manege': 'http://manege.spb.ru/'
}


class Film:
    def __init__(self, name, time, price, hall):
        self.name = name
        self.time = time
        self.price = price
        self.hall = hall

    def __repr__(self):
        return f'Кинцо заебатое "{self.name}"\nПо бабкам не дохуя всего {self.price}\nПо времени не поздно в {self.time}'


class Exhibition:
    def __init__(self, title, date, price, place):
        self.title = title
        self.date = date
        self.price = price
        self.place = place

    def __repr__(self):
        return f'Выставка сытная "{self.title}"\nПо бабкам не дохуя всего {self.price}\nПо дате вот так {self.date}\nМесто приличное{self.place}'


class ABCFilmHandler(ABC):
    @abstractmethod
    def get(self) -> List[Film]:
        pass


class ABCExhibitionHandler(ABC):
    @abstractmethod
    def get(self) -> List[Exhibition]:
        pass


class RodinaHandler(ABCFilmHandler):
    def get(self) -> List[Film]:
        session = HTMLSession()
        resp = session.get(self.url())
        all_program = []
        for l in resp.html.find('.anons'):
            film = Film(name=l.find('.film_name')[0].text,
                        time=l.find('.timeline')[0].text,
                        price=l.find('.ticket')[0].text[13:],
                        hall=l.find('.zall')[0].text)

            all_program.append(film)

        return all_program

    def url(self):
        return urls['rodina']



class MifHandler(ABCExhibitionHandler):
    def get(self) -> List[Exhibition]:
        session = HTMLSession()
        resp = session.get(self.url())
        all_program = []
        for l in resp.html.find('.content'):
            exhibition = Exhibition(
                title=l.find('.title')[0].text,
                date=l.find('.date')[0].text,
                price='по бабкам хуй пойми',
                place=l.find('.place')[0].text)

            all_program.append(exhibition)

        return all_program

    def url(self):
        return urls['mif']


class ManegeHandler(ABCExhibitionHandler):
    def get(self) -> List[Exhibition]:
        session = HTMLSession()
        resp = session.get(self.url())
        all_program = []
        for l in resp.html.find('.card'):
            exhibition = Exhibition(
                title=l.find('.vdsw_ch_fontsize vdsw_ch_kerning')[0],
                date=l.find('.card__meta__info'),
                price='по бабкам хуй пойми',
                place='Исаакиевская площадь, 1')

            all_program.append(exhibition)
            print(l.find('.card__title'))

        return all_program

    def url(self):
        return urls['manege']


def get() -> List[Exhibition]:
    session = HTMLSession()
    resp = session.get(murl())
    all_program = []



    a = resp.html.find('.search-layout__body', first=True)

    f = a.find('.layout', first=True)
    s = f.find('.layout__content', first=True)
    r = s.find('.recommendations', first=True)
    c = r.find('.recommendations__container', first=True)
    y = c.find('.card')

    print(y)
    # for i in all_years:
    #     print(i.find('.main__year__block-2021'))

    # for l in resp.html.find('.card__head'):
        # exhibition = Exhibition(
        #     title=l.find('.vdsw_ch_fontsize vdsw_ch_kerning')[0],
        #     date=l.find('.card__meta__info'),
        #     price='по бабкам хуй пойми',
        #     place='Исаакиевская площадь, 1')

        # title = l.find('.card__meta__info').text
        # print(l.text)

        # all_program.append(exhibition)



def murl():
    return urls['manege']

get()
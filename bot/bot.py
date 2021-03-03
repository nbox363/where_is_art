from web.main import RodinaHandler, ABCFilmHandler, MifHandler, ManegeHandler


class Helper():
    films = {
        'rodina': RodinaHandler,
    }

    exhibitions = {
        'mif': MifHandler,
        'manege': ManegeHandler
    }

    def __init__(self):
        self.map = {}

    def film(self, k: str) -> ABCFilmHandler:
        if self.map.get(k):
            return self.map[k]
        self.map[k] = self.films[k]
        return self.map[k]()

    def e(self, k: str):
        if self.map.get(k):
            return self.map[k]
        self.map[k] = self.exhibitions[k]
        return self.map[k]()
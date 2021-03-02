from abc import ABC, abstractmethod

from web.r import ABCReqClient, RequestsClient
from web.urls import urls


class ABCHandler(ABC):

    def __init__(self):
        self.url = self.get_url()
        self.req = RequestsClient()
        self.all_program = []

    @abstractmethod
    def get_program(self):
        pass

    @abstractmethod
    def get_url(self) -> str:
        pass


class RodinaHandler(ABCHandler):

    def get_program(self):
        resp = self._get_resp()

        for l in resp.html.find('.anons'):
            program = {
                'name': l.find('.film_name')[0].text,
                'time': l.find('.timeline')[0].text,
                'price': l.find('.ticket')[0].text[13:],
                'hall': l.find('.zall')[0].text,
            }
            self.all_program.append(program)

        return self.all_program

    def get_url(self) -> str:
        return urls['rodina']

    def _get_resp(self):
        return self.req.get(self.url)


if __name__ == '__main__':
    rodina_handler = RodinaHandler()




# class MifHandler(ABCHandler):
#
#     def __init__(self, url, req: ABCReqClient):
#         self.url = url
#         self.req = req
#         self.all_program = []
#
#     def get_info(self):
#         resp = self._get_resp()
#
#         for l in resp.html.find('.content'):
#             name = l.find('.title')[0].text
#             date = l.find('.date')[0].text
#             place = l.find('.place')[0].text
#             self.all_program.append((name, date, place))
#
#     def _get_resp(self):
#         return self.req.get(self.url)

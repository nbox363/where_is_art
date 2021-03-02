from abc import ABC, abstractmethod

from requests_html import HTMLResponse
from requests_html import HTMLSession

# from requests.models import Response

__all__ = ['ABCReqClient', 'RequestsClient']


class ABCResp(ABC):
    @abstractmethod
    def find(self) -> list:
        pass


class ABCReqClient(ABC):
    @abstractmethod
    def get(self, url: str) -> ABCResp:
        pass


class RequestsClient(ABCReqClient):
    def get(self, url) -> HTMLResponse:
        session = HTMLSession()
        resp = session.get(url)
        return resp

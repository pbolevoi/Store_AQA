import requests
from api.payloads import Payloads
from api.endpoints import Endpoints
from utils.helper import Helper


class BaseAPI(Helper):

    def __init__(self):
        self.session = requests.Session()
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    def get(self, url, **kwargs):
        return self.session.get(url, **kwargs)

    def post(self, url, **kwargs):
        return self.session.post(url, **kwargs)

    def put(self, url, **kwargs):
        return self.session.put(url, **kwargs)

    def delete(self, url, **kwargs):
        return self.session.delete(url, **kwargs)

    def close(self):
        self.session.close()

import requests
from resources.reqres import data


class BaseApi():
    def __init__(self):
        self.data = data
        self.base_url = self.data.base_url

    def app_is_up(self, url) -> int:
        return requests.get(url).status_code

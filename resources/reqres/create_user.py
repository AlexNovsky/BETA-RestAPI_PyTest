import requests

from resources.reqres.base_api import BaseApi
import time

class CreateUser(BaseApi):
    def __init__(self):
        super().__init__()
        self.uri = f"{self.base_url}/api/users"

    def is_api_up(self) -> bool:
        resp = self.app_is_up(self.uri)
        if resp == 200:
            return True

    def generate_new_payload(self):
        timestamp = int(time.time())
        return {
            "name": f"Alex{timestamp}",
            "job": f"Engineer{timestamp}"
        }

    def new_user(self, payload):
        return requests.post(self.uri, payload)

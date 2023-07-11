import requests
from resources.reqres.base_api import BaseApi


class UpdateUser(BaseApi):
    def __init__(self):
        super().__init__()
        self.uri = f'{self.base_url}/api/users/2'

    def is_update_api_up(self):
        resp = self.app_is_up(self.uri)
        if resp == 200:
            return True

    def patch_user(self, username):
        payload = {
            "name": username,
            "job": "updated job"
        }
        return requests.patch(self.uri, payload)

    def patch_put_user(self, username):
        payload = {
            "name": "updated name",
            "job": "updated job"
        }
        return requests.put(self.uri, payload)
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import pytest

from resources.reqres.base_api import BaseApi
from resources.reqres.create_user import CreateUser
from resources.reqres.update_user import UpdateUser

@pytest.fixture(scope="session")
def app():
    app.base_api = BaseApi()
    app.create_user = CreateUser()
    app.update_user = UpdateUser()
    yield app

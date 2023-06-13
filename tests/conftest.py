import pytest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from resources.pixegami.base_api import BaseApi
from resources.pixegami.create_task_api import CreateTaskApi
from resources.pixegami.get_task_api import GetTaskApi
from resources.pixegami.update_task_api import UpdateTaskApi
from resources.pixegami.delete_task_api import DeleteTaskApi
from resources.pixegami.make_tasks_list_api import TasksListApi


@pytest.fixture(scope='session')
def app():
    """Fixture returns an object, containing all the API Objects of the application under test.

        Includes BaseApi with all its standard methods (delete task, create task, update task, etc.)
        and all child API objects with all specific methods (create, update, delete or list tasks)
    """
    app.base_api = BaseApi()
    app.create_task_api = CreateTaskApi()
    app.get_task_api = GetTaskApi()
    app.update_task_api = UpdateTaskApi()
    app.delete_task_api = DeleteTaskApi()
    app.tasks_list_api = TasksListApi()
    yield app

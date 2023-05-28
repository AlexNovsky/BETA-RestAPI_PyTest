from resources.pixegami.base_api import BaseApi
from resources.pixegami.create_task_api import CreateTaskApi
from resources.pixegami.get_task_api import GetTaskApi


class Application:
        """Returns an object, containing all the Page Objects of the application under test.

        Includes BasePage with all its standard methods (delete task, create task, update task, etc.)
        and all the child page objects (TodoPage etc.) with all their endpoints and payloads (payload, new payload
        generation, search and comparison, etc.)
        """
        base_api = BaseApi()
        create_task_api = CreateTaskApi()
        get_task_api = GetTaskApi()

from resources.pixegami.base_api import BaseApi
from resources.pixegami.create_task_api import CreateTaskApi
from resources.pixegami.get_task_api import GetTaskApi
from resources.pixegami.update_task_api import UpdateTaskApi
from resources.pixegami.delete_task_api import DeleteTaskApi
from resources.pixegami.make_tasks_list_api import TasksListApi


class Application:
    """Returns an object, containing all the API Objects of the application under test.

        Includes BasePage with all its standard methods (delete task, create task, update task, etc.)
        and all the child API objects with all specific methods (create, update, delete or list tasks)
        """
    base_api = BaseApi()
    create_task_api = CreateTaskApi()
    get_task_api = GetTaskApi()
    update_task_api = UpdateTaskApi()
    delete_task_api = DeleteTaskApi()
    tasks_list_api = TasksListApi()

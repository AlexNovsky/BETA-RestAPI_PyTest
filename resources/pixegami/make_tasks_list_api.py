from requests import Response
# from resources.pixegami.application import Application
from resources.pixegami.base_api import BaseApi


class TasksListApi(BaseApi):
    """Class, containing methods for retrieving list of tasks, specified by user_id
    """
    def __init__(self):
        super().__init__()
        self.uri = f"{self.url}/list-tasks/"

    def list_tasks(self, user_id) -> Response:
        """
        Making an API call to create a list of all tasks, created by specified user
        :param user_id:     Id of the user who created the task
        :return:            List of all user's tasks
        """
        return self.get(f"{self.uri}{user_id}")

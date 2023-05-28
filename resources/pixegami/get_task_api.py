from requests import Response
from resources.pixegami.base_api import BaseApi


class GetTaskApi(BaseApi):
    """Base class for every page object of the application under test
    Includes all basic page methods, applicable to every page, like (delete task,
    create task, get task info, update task, and many more)
    """

    def __init__(self):
        super().__init__()
        self.uri = f"{self.url}/get-task"

    def get_task(self, task_id) -> Response:
        """
        Making an API call to get specific task information (payload)
        :param task_id:     Id of the task, which payload has been requested
        :return:            Payload if the task, specified by task_id
        """
        return self.get(f"{self.uri}/{task_id}")

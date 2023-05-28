import time
from requests import Response
from typing import Dict
from resources.pixegami.base_api import BaseApi


class CreateTaskApi(BaseApi):
    """Base class for every page object of the application under test
    Includes all basic page methods, applicable to every page, like (delete task,
    create task, get task info, update task, and many more)
    """

    def __init__(self):
        super().__init__()
        self.uri = f"{self.url}/create-task"

    @staticmethod
    def generate_task_payload() -> Dict[str, str]:
        """
        Function generates a payload with random user_id and content
        :return:            New generated payload with unique user_id and content
        """
        timestamp = int(time.time())
        return {
            "content": f"API_testing_{timestamp}",
            "user_id": f"Alex_Novsky_{timestamp}",
            "is_done": False,
        }

    def create_task(self, payload) -> Response:
        """
        Making an API call to create task with desired payload
        :param payload:     Payload,used for creating task
        :return:            Executed action (call - create)
        """
        return self.put(self.uri, payload)

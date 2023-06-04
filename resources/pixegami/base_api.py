import requests
from requests import Response
from typing import Dict
from resources.pixegami import data


class BaseApi:
    """Base class for every API object of the API under test
    Includes all basic methods, applicable to any API call, like (delete task,
    create task, get task info, update task, and many more)
    """
    def __init__(self):
        """
        Initializing endpoint variable for the class from external endpoint, stored in separate file
        """
        self.data = data
        self.url = self.data.base_url

    def app_is_up(self) -> bool:
        """
        Checking that endpoint is callable
        :return:            Status code of API call (200 for successful request/call)
        """
        return requests.get(self.url).status_code == 200

    def get(self, url: str) -> Response:
        """
        Making an API call to get specific task information (payload)
        :param url:         Url of the task, which payload has been requested
        :return:            Payload if the task, specified by task_id
        """
        return requests.get(url)

    def post(self, url: str, payload: Dict[str, str]) -> Response:
        """
        Making an API call to create task with desired payload
        :param url:         Url of the task, which payload has been requested
        :param payload:     Payload,used for creating task
        :return:            Executed action (call - create)
        """
        return requests.post(url, json=payload)

    def put(self, url: str, payload: Dict[str, str]) -> Response:
        """
        Making an API call to create task with desired payload
        :param url:         Url of the task, which payload has been requested
        :param payload:     Payload,used for creating task
        :return:            Executed action (call - create)
        """
        return requests.put(url, json=payload)

    def patch(self, url: str, payload: Dict[str, str]) -> Response:
        """
        Making an API call to create task with desired payload
        :param url:         Url of the task, which payload has been requested
        :param payload:     Payload,used for creating task
        :return:            Executed action (call - create)
        """
        return requests.patch(url, json=payload)

    # def delete(self, url: str, payload: str) -> Response:
    def delete(self, url: str) -> Response:
        """
        Making an API call to delete specific task identified by task_id
        :param payload:
        :param user_id:
        :param url:     Url of the task, which payload has been requested
        :return:            Executed action (call - delete)
        """
        # return requests.delete(url, payload)
        return requests.delete(url)

    # def list_tasks(self, user_id) -> Response:
    #     """
    #     Making an API call to create a list of all tasks, created by specified user
    #     :param user_id:     Id of the user who created the task
    #     :return:            List of all user's tasks
    #     """
    #     return requests.get(self.url + f"/list-tasks/{user_id}")

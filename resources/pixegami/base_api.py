from typing import Dict

import requests
import uuid

from requests import Response

import data as data


class BaseApi:
    """Base class for every page object of the application under test
    Includes all basic page methods, applicable to every page, like (delete task,
    create task, get task info, update task, and many more)
    """
    def __init__(self):
        """
        Initializing endpoint variable for the class from external endpoint, stored in separate file
        """
        self.endpoint = data.endpoint

    def can_call_endpoint(self):
        response = requests.get(self.endpoint)
        # return response.status_code
        if not response.status_code == 200:
            return False
        return True
    def create_task(self, payload) -> Response:
        """
        Making an API call to create task with desired payload
        :param payload:     Payload,used for creating task
        :return:            Executed action (call - create)
        """
        return requests.put(self.endpoint + "/create-task", json=payload)

    def delete_task(self, task_id) -> Response:
        """
        Making an API call to delete specific task identified by task_id
        :param task_id:     Id of the task to be deleted
        :return:            Executed action (call - delete)
        """
        return requests.delete(self.endpoint + f"/delete-task/{task_id}")

    def get_task(self, task_id) -> Response:
        """
        Making an API call to get specific task information (payload)
        :param task_id:     Id of the task, which payload has been requested
        :return:            Payload if the task, specified by task_id
        """
        return requests.get(self.endpoint + f"/get-task/{task_id}")

    def list_tasks(self, user_id) -> Response:
        """
        Making an API call to create a list of all tasks, created by specified user
        :param user_id:     Id of the user who created the task
        :return:            List of all user's tasks
        """
        return requests.get(self.endpoint + f"/list-tasks/{user_id}")

    def new_task_payload(self) -> dict[str, str]:
        """
        Function generates a payload with random user_id and content
        :return:            New generated payload with unique user_id and content
        """
        user_id = f"Alex_Novsky_{uuid.uuid4().hex}"
        content = f"API_testing_{uuid.uuid4().hex}"
        return {
            "content": content,
            "user_id": user_id,
            "is_done": False,
        }

    def update_task(self, payload) -> Response:
        """
        Making an API call to update task with partially or fully modified payload
        :param payload:     Updated payload for the task
        :return:            Executed action (call - update)
        """
        return requests.put(self.endpoint + "/update-task", json=payload)

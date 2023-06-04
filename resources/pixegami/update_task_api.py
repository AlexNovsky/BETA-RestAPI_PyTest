from requests import Response
from resources.pixegami.base_api import BaseApi


class UpdateTaskApi(BaseApi):
    """Class, containing methods for the task update
    """

    def __init__(self):
        super().__init__()
        self.uri = f"{self.url}/update-task/"

    def post_update_task(self, user_id, task_id) -> Response:
        """
        Making an API call to update, specified by task_id and user_id, task with desired payload
        :param user_id:     Specific user_id of updated task owner/creator
        :param task_id:     Specific task_id
        :return:            Executed action (call - put)
        """
        # TODO: make a function that generate updated payload instead hardcoded values
        payload = {
            "content": "updated payload",
            "user_id": user_id,
            "task_id": task_id,
            "is_done": True,
        }
        return self.put(self.uri, payload)

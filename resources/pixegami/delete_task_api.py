from requests import Response
from resources.pixegami.base_api import BaseApi


class DeleteTaskApi(BaseApi):
    """Class, containing methods for tasks deletion
    """

    def __init__(self):
        super().__init__()
        self.uri = f"{self.url}/delete-task/"

    # @staticmethod
    def delete_task(self, task_id) -> Response:
        """
        Making an API call to create task with desired payload
        :param task_id:
        :return:            Executed action (call - delete)
        """
        return self.delete(f"{self.uri}{task_id}")

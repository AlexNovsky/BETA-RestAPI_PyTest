import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


from resources.pixegami.application import Application


class TestTodoAPI:
    api = Application().todo_api

    def test_api_is_callable(self):
        assert self.api.endpoint_is_callable() is True

    def test_task_is_created(self):
        create_task_response_status, get_task_response_status, payload, get_task_data, task_id\
            = self.api.post_create_task()  # https://tesera.ru/images/items/812467/575689ce8b4d362ec5391f085011734f1.jpg
        assert create_task_response_status == 200
        assert get_task_response_status == 200
        assert get_task_data["content"] == payload["content"]
        assert get_task_data["user_id"] == payload["user_id"]
        assert get_task_data["task_id"] == task_id

    def test_task_is_updated(self):
        get_task_data, new_payload, update_task_response_status, get_task_response_status \
            = self.api.post_update_task()  # https://tesera.ru/images/items/812467/575689ce8b4d362ec5391f085011734f1.jpg
        assert update_task_response_status == 200
        assert get_task_response_status == 200
        assert get_task_data["content"] == new_payload["content"]
        assert get_task_data["is_done"] == new_payload["is_done"]

    def test_tasks_is_listed(self):
        n, create_task_response_status, list_tasks_response_status, number_of_tasks \
            = self.api.get_tasks_list()  # https://tesera.ru/images/items/812467/575689ce8b4d362ec5391f085011734f1.jpg
        assert create_task_response_status == 200
        assert list_tasks_response_status == 200
        assert n == number_of_tasks

    def test_task_is_deleted(self):
        create_task_response_status, delete_task_response_status, get_deleted_task_response_status \
            = self.api.post_delete_task()  # https://tesera.ru/images/items/812467/575689ce8b4d362ec5391f085011734f1.jpg
        assert create_task_response_status == 200
        assert delete_task_response_status == 200
        assert get_deleted_task_response_status == 404

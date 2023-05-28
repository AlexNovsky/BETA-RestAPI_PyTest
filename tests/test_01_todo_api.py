import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from resources.pixegami.application import Application


class TestTodoAPI:

    def test_app_is_up(self):
        api = Application().base_api
        assert api.app_is_up() is True

    def test_task_is_created(self):
        api = Application().create_task_api
        expected_task = api.generate_task_payload()
        created_task = api.create_task(expected_task)
        assert created_task.status_code == 200
        created_task_details = created_task.json()
        assert created_task_details["task"]["user_id"] == expected_task["user_id"]
        assert created_task_details["task"]["content"] == expected_task["content"]
        assert created_task_details["task"]["is_done"] == expected_task["is_done"]

        api = Application().get_task_api
        retrieved_task = api.get_task(created_task_details["task"]["task_id"])
        assert retrieved_task.status_code == 200
        retrieved_task_details = retrieved_task.json()
        assert retrieved_task_details["user_id"] == expected_task["user_id"]
        assert retrieved_task_details["content"] == expected_task["content"]
        assert retrieved_task_details["is_done"] == expected_task["is_done"]

    # def test_task_is_updated(self):
    #     get_task_data, new_payload, update_task_response_status, get_task_response_status \
    #         = self.api.post_update_task()  # https://tesera.ru/images/items/812467/575689ce8b4d362ec5391f085011734f1.jpg
    #     assert update_task_response_status == 200
    #     assert get_task_response_status == 200
    #     assert get_task_data["content"] == new_payload["content"]
    #     assert get_task_data["is_done"] == new_payload["is_done"]
    #
    # def test_tasks_is_listed(self):
    #     n, create_task_response_status, list_tasks_response_status, number_of_tasks \
    #         = self.api.get_tasks_list()  # https://tesera.ru/images/items/812467/575689ce8b4d362ec5391f085011734f1.jpg
    #     assert create_task_response_status == 200
    #     assert list_tasks_response_status == 200
    #     assert n == number_of_tasks
    #
    # def test_task_is_deleted(self):
    #     create_task_response_status, delete_task_response_status, get_deleted_task_response_status \
    #         = self.api.post_delete_task()  # https://tesera.ru/images/items/812467/575689ce8b4d362ec5391f085011734f1.jpg
    #     assert create_task_response_status == 200
    #     assert delete_task_response_status == 200
    #     assert get_deleted_task_response_status == 404

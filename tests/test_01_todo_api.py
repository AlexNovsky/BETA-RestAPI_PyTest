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

    def test_task_is_updated(self):
        api = Application().create_task_api
        expected_task = api.generate_task_payload()
        created_task = api.create_task(expected_task)
        assert created_task.status_code == 200
        created_task_details = created_task.json()
        assert created_task_details["task"]["user_id"] == expected_task["user_id"]
        assert created_task_details["task"]["content"] == expected_task["content"]
        assert created_task_details["task"]["is_done"] == expected_task["is_done"]
        created_task_id = created_task_details["task"]["task_id"]
        created_user_id = created_task_details["task"]["user_id"]

        api = Application().update_task_api
        updated_task = api.post_update_task(created_user_id, created_task_id)
        assert created_task.status_code == 200
        updated_task_details = updated_task.json()
        assert updated_task_details["updated_task_id"] == created_task_id

        api = Application().get_task_api
        retrieved_updated_task = api.get_task(updated_task_details["updated_task_id"])
        assert retrieved_updated_task.status_code == 200
        retrieved_updated_task_details = retrieved_updated_task.json()
        # TODO: change hardcoded content value in assertion to value from post_update_task
        assert retrieved_updated_task_details["content"] == "updated payload"
        assert retrieved_updated_task_details["user_id"] == created_user_id

    def test_task_is_deleted(self):
        api = Application().create_task_api
        expected_task = api.generate_task_payload()
        created_task = api.create_task(expected_task)
        assert created_task.status_code == 200
        created_task_details = created_task.json()
        assert created_task_details["task"]["user_id"] == expected_task["user_id"]
        assert created_task_details["task"]["content"] == expected_task["content"]
        assert created_task_details["task"]["is_done"] == expected_task["is_done"]
        task_id = created_task_details["task"]["task_id"]

        api = Application().get_task_api
        retrieved_task = api.get_task(task_id)
        assert retrieved_task.status_code == 200

        api = Application().delete_task_api
        delete_task = api.delete_task(task_id)
        delete_task_response_status = delete_task.status_code
        assert delete_task_response_status == 200

        api = Application().get_task_api
        get_deleted_task_response_status = api.get_task(task_id)
        assert get_deleted_task_response_status.status_code == 404

    def test_tasks_listed(self):
        tasks_to_create = 4
        api = Application().create_task_api
        payload = api.generate_task_payload()
        for t in range(tasks_to_create):
            create_task_response = api.create_task(payload)
            create_task_response_status = create_task_response.status_code
            assert create_task_response_status == 200

        user_id = payload["user_id"]
        api = Application().tasks_list_api
        list_tasks_response = api.list_tasks(user_id)
        list_tasks_response_status = list_tasks_response.status_code
        data = list_tasks_response.json()
        tasks = data["tasks"]
        number_of_created_tasks = len(tasks)
        assert list_tasks_response_status == 200
        assert tasks_to_create == number_of_created_tasks

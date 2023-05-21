import requests
from base_page import BasePage


class TodoPage:
    base_page = BasePage()

    def can_call_endpoint(self):
        response = requests.get(self.base_page.endpoint)
        if not response.status_code == 200:
            return False
        return True

    def can_create_task(self):
        payload = self.base_page.new_task_payload()
        create_task_response = self.base_page.create_task(payload)
        if not create_task_response.status_code == 200:
            return False

        data = create_task_response.json()

        task_id = data["task"]["task_id"]
        get_task_response = self.base_page.get_task(task_id)
        if not get_task_response.status_code == 200:
            return False

        get_task_data = get_task_response.json()
        if not get_task_data["content"] == payload["content"]:
            return False
        if not get_task_data["user_id"] == payload["user_id"]:
            return False
        if not get_task_data["task_id"] == task_id:
            return False
        return True

    def can_update_task(self):
        payload = self.base_page.new_task_payload()
        create_task_response = self.base_page.create_task(payload)
        task_id = create_task_response.json()["task"]["task_id"]

        new_payload = {
            "content": "updated payload",
            "user_id": payload["user_id"],
            "task_id": task_id,
            "is_done": True,
        }
        update_task_response = self.base_page.update_task(new_payload)
        if not update_task_response.status_code == 200:
            return False

        get_task_response = self.base_page.get_task(task_id)
        if not get_task_response.status_code == 200:
            return False

        get_task_data = get_task_response.json()
        if not get_task_data["content"] == new_payload["content"]:
            return False
        if not get_task_data["is_done"] == new_payload["is_done"]:
            return False
        return True

    def can_list_tasks(self):
        n = 3
        payload = self.base_page.new_task_payload()
        for t in range(n):
            create_task_response = self.base_page.create_task(payload)
            if not create_task_response.status_code == 200:
                return False

        user_id = payload["user_id"]
        list_tasks_response = self.base_page.list_tasks(user_id)
        if not list_tasks_response.status_code == 200:
            return False
        data = list_tasks_response.json()

        tasks = data["tasks"]
        if not len(tasks) == n:
            return False
        return True

    def can_delete_task(self):
        payload = self.base_page.new_task_payload()
        create_task_response = self.base_page.create_task(payload)
        if not create_task_response.status_code == 200:
            return False

        task_id = create_task_response.json()["task"]["task_id"]
        delete_task_response = self.base_page.delete_task(task_id)
        if not delete_task_response.status_code == 200:
            return False

        get_task_response = self.base_page.get_task(task_id)
        if not get_task_response.status_code == 404:
            return False
        return True

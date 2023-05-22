import requests
from base_api import BaseApi


# class TodoPage:
class TodoApi(BaseApi):

    def post_create_task(self):
        payload = self.generate_task_payload()
        create_task_response = self.create_task(payload)
        if not create_task_response.status_code == 200:
            return False

        data = create_task_response.json()

        task_id = data["task"]["task_id"]
        get_task_response = self.get_task(task_id)
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

    def post_update_task(self):
        payload = self.generate_task_payload()
        create_task_response = self.create_task(payload)
        task_id = create_task_response.json()["task"]["task_id"]

        new_payload = {
            "content": "updated payload",
            "user_id": payload["user_id"],
            "task_id": task_id,
            "is_done": True,
        }
        update_task_response = self.update_task(new_payload)
        if not update_task_response.status_code == 200:
            return False

        get_task_response = self.get_task(task_id)
        if not get_task_response.status_code == 200:
            return False

        get_task_data = get_task_response.json()
        if not get_task_data["content"] == new_payload["content"]:
            return False
        if not get_task_data["is_done"] == new_payload["is_done"]:
            return False
        return True

    def get_tasks_list(self):
        n = 3
        payload = self.generate_task_payload()
        for t in range(n):
            create_task_response = self.create_task(payload)
            if not create_task_response.status_code == 200:
                return False

        user_id = payload["user_id"]
        list_tasks_response = self.list_tasks(user_id)
        if not list_tasks_response.status_code == 200:
            return False
        data = list_tasks_response.json()

        tasks = data["tasks"]
        if not len(tasks) == n:
            return False
        return True

    def post_delete_task(self):
        payload = self.generate_task_payload()
        create_task_response = self.create_task(payload)
        if not create_task_response.status_code == 200:
            return False

        task_id = create_task_response.json()["task"]["task_id"]
        delete_task_response = self.delete_task(task_id)
        if not delete_task_response.status_code == 200:
            return False

        get_task_response = self.get_task(task_id)
        if not get_task_response.status_code == 404:
            return False
        return True

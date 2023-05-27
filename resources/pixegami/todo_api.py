from resources.pixegami.base_api import BaseApi


class TodoApi(BaseApi):

    def post_create_task(self):
        payload = self.generate_task_payload()
        create_task_response = self.create_task(payload)
        create_task_response_status = create_task_response.status_code

        data = create_task_response.json()
        task_id = data["task"]["task_id"]
        get_task_response = self.get_task(task_id)
        get_task_response_status = get_task_response.status_code
        get_task_data = get_task_response.json()
        return create_task_response_status, get_task_response_status, payload, get_task_data, task_id

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
        update_task_response_status = update_task_response.status_code
        get_task_response = self.get_task(task_id)
        get_task_response_status = get_task_response.status_code
        get_task_data = get_task_response.json()
        return get_task_data, new_payload, update_task_response_status, get_task_response_status

    def get_tasks_list(self):
        # global create_task_response_status
        n = 3
        payload = self.generate_task_payload()
        for t in range(n):
            create_task_response = self.create_task(payload)
            create_task_response_status = create_task_response.status_code

        user_id = payload["user_id"]
        list_tasks_response = self.list_tasks(user_id)
        list_tasks_response_status = list_tasks_response.status_code
        data = list_tasks_response.json()

        tasks = data["tasks"]
        number_of_tasks = len(tasks)
        return n, create_task_response_status, list_tasks_response_status, number_of_tasks

    def post_delete_task(self):
        payload = self.generate_task_payload()
        create_task_response = self.create_task(payload)
        create_task_response_status = create_task_response.status_code
        task_id = create_task_response.json()["task"]["task_id"]
        delete_task_response = self.delete_task(task_id)
        delete_task_response_status = delete_task_response.status_code

        get_deleted_task_response = self.get_task(task_id)
        get_deleted_task_response_status = get_deleted_task_response.status_code
        return create_task_response_status, delete_task_response_status, get_deleted_task_response_status
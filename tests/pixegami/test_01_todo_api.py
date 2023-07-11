class TestTodoAPI:
    def test_app_is_up(self, app):
        assert app.base_api.app_is_up() is True

    def test_task_is_created(self, app):
        expected_task = app.create_task_api.generate_task_payload()
        created_task = app.create_task_api.create_task(expected_task)
        assert created_task.status_code == 200
        created_task_details = created_task.json()
        assert created_task_details["task"]["user_id"] == expected_task["user_id"]
        assert created_task_details["task"]["content"] == expected_task["content"]
        assert created_task_details["task"]["is_done"] == expected_task["is_done"]

        retrieved_task = app.get_task_api.get_task(created_task_details["task"]["task_id"])
        assert retrieved_task.status_code == 200
        retrieved_task_details = retrieved_task.json()
        assert retrieved_task_details["user_id"] == expected_task["user_id"]
        assert retrieved_task_details["content"] == expected_task["content"]
        assert retrieved_task_details["is_done"] == expected_task["is_done"]

    def test_task_is_updated(self, app):
        expected_task = app.create_task_api.generate_task_payload()
        created_task = app.create_task_api.create_task(expected_task)
        assert created_task.status_code == 200
        created_task_details = created_task.json()
        assert created_task_details["task"]["user_id"] == expected_task["user_id"]
        assert created_task_details["task"]["content"] == expected_task["content"]
        assert created_task_details["task"]["is_done"] == expected_task["is_done"]
        created_task_id = created_task_details["task"]["task_id"]
        created_user_id = created_task_details["task"]["user_id"]

        updated_task = app.update_task_api.post_update_task(created_user_id, created_task_id)
        assert created_task.status_code == 200
        updated_task_details = updated_task.json()
        assert updated_task_details["updated_task_id"] == created_task_id

        retrieved_updated_task = app.get_task_api.get_task(updated_task_details["updated_task_id"])
        assert retrieved_updated_task.status_code == 200
        retrieved_updated_task_details = retrieved_updated_task.json()
        # TODO: change hardcoded content value in assertion to value from post_update_task
        assert retrieved_updated_task_details["content"] == "updated payload"
        assert retrieved_updated_task_details["user_id"] == created_user_id

    def test_task_is_deleted(self, app):
        expected_task = app.create_task_api.generate_task_payload()
        created_task = app.create_task_api.create_task(expected_task)
        assert created_task.status_code == 200
        created_task_details = created_task.json()
        assert created_task_details["task"]["user_id"] == expected_task["user_id"]
        assert created_task_details["task"]["content"] == expected_task["content"]
        assert created_task_details["task"]["is_done"] == expected_task["is_done"]
        task_id = created_task_details["task"]["task_id"]

        retrieved_task = app.get_task_api.get_task(task_id)
        assert retrieved_task.status_code == 200

        delete_task = app.delete_task_api.delete_task(task_id)
        delete_task_response_status = delete_task.status_code
        assert delete_task_response_status == 200

        get_deleted_task_response = app.get_task_api.get_task(task_id)
        assert get_deleted_task_response.status_code == 404

    def test_tasks_listed(self, app):
        tasks_to_create = 4
        payload = app.create_task_api.generate_task_payload()
        for t in range(tasks_to_create):
            create_task_response = app.create_task_api.create_task(payload)
            create_task_response_status = create_task_response.status_code
            assert create_task_response_status == 200

        user_id = payload["user_id"]
        list_tasks_response = app.tasks_list_api.list_tasks(user_id)
        list_tasks_response_status = list_tasks_response.status_code
        data = list_tasks_response.json()
        tasks = data["tasks"]
        number_of_created_tasks = len(tasks)
        assert list_tasks_response_status == 200
        assert tasks_to_create == number_of_created_tasks

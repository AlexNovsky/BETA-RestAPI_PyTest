"""
sys and os libraries necessary to implement the code, that automatically determining the path and allowing to
use relative path to the files for import from different folders
"""
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(parent_dir, 'resources', 'pixegami'))

from application import Application
import pytest


class TestTodoAPI:
    api = Application.todo_api

    def test_api_is_callable(self):
        self.api.assertEqual(self.api.endpoint_is_callable(), 200)
        # assert self.api.endpoint_is_callable() == 200

    def test_task_is_created(self):
        create_task_response_status, get_task_response_status, payload, get_task_data, task_id\
            = self.api.post_create_task()
        self.api.assertEqual(create_task_response_status, 200)
        self.api.assertEqual(get_task_response_status, 200)
        self.api.assertEqual(get_task_data["content"], payload["content"])
        self.api.assertEqual(get_task_data["user_id"], payload["user_id"])
        self.api.assertEqual(get_task_data["task_id"], task_id)
        # assert create_task_response_status == 200
        # assert get_task_response_status == 200
        # assert get_task_data["content"] == payload["content"]
        # assert get_task_data["user_id"] == payload["user_id"]
        # assert get_task_data["task_id"] == task_id

    def test_task_is_updated(self):
        get_task_data, new_payload, update_task_response_status, get_task_response_status \
            = self.api.post_update_task()
        self.api.assertEqual(update_task_response_status, 200)
        self.api.assertEqual(get_task_response_status, 200)
        self.api.assertEqual(get_task_data["content"], new_payload["content"])
        self.api.assertEqual(get_task_data["is_done"], new_payload["is_done"])
        # assert update_task_response_status == 200
        # assert get_task_response_status == 200
        # assert get_task_data["content"] == new_payload["content"]
        # assert get_task_data["is_done"] == new_payload["is_done"]

    def test_tasks_is_listed(self):
        n, create_task_response_status, list_tasks_response_status, number_of_tasks \
            = self.api.get_tasks_list()
        self.api.assertEqual(create_task_response_status, 200)
        self.api.assertEqual(list_tasks_response_status, 200)
        self.api.assertEqual(n, number_of_tasks)
        # assert create_task_response_status == 200
        # assert list_tasks_response_status == 200
        # assert n == number_of_tasks

    def test_task_is_deleted(self):
        create_task_response_status, delete_task_response_status, get_deleted_task_response_status \
            = self.api.post_delete_task()
        self.api.assertEqual(create_task_response_status, 200)
        self.api.assertEqual(delete_task_response_status, 200)
        self.api.assertEqual(get_deleted_task_response_status, 404)
        # assert create_task_response_status == 200
        # assert delete_task_response_status == 200
        # assert get_deleted_task_response_status == 404

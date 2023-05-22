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


class TestTodoAPI:
    api = Application.todo_api

    def test_api_is_callable(self):
        assert self.api.endpoint_is_callable() == True

    def test_task_is_created(self):
        assert self.api.post_create_task() == True

    def test_task_is_updated(self):
        assert self.api.post_update_task() == True

    def test_tasks_is_listed(self):
        assert self.api.get_tasks_list() == True

    def test_task_is_deleted(self):
        assert self.api.post_delete_task() == True

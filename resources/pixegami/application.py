from base_page import BasePage
from todo_page import TodoPage

class Application:
        """Returns an object, containing all the Page Objects of the application under test.

        Includes BasePage with all its standard methods (delete task, create task, update task, etc.)
        and all the child page objects (TodoPage etc.) with all their endpoints and payloads (payload, new payload
        generation, search and comparison, etc.)
        """
        base_page = BasePage()
        todo_page = TodoPage()

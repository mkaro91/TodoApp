from models.Todo import Todo, Priority

class TodoFilterer:
    def by_completed(self, todo_list: list[Todo], is_completed=True):
        """
        Return a list of Todo objects if todo is completed if is_completed else if is incomplete

        :param todo-list: List of Todo objects to be filtered
        :param is_completed: Return completed todos if True else incompleted todos if False

        :return list[Todo]: List of Todo objects filtered by completed attribute
        """
        return [todo for todo in todo_list if todo.completed] if is_completed else [todo for todo in todo_list if not todo.completed]

    # Priority Order: Critical -> High -> Medium -> Low
    def by_priority(self, todo_list: list[Todo], priority: Priority):
        """
        Return a list of Todo objects filtered by priority

        :param todo_list: List of Todo objects to be filtered
        :param priority: Priority to filter by

        :return list[Todo]: List of Todo objects filtered by priority attribute
        """
        return [todo for todo in todo_list if todo.priority == priority]

    def by_due_date(self, todo_list: list[Todo], due_date):
        """
        Return a list of Todo objects filtered by due date less than or equal to provided due date

        :param todo_list: List of Todo objects to be filtered
        :param due_date: Cutoff due date

        :return list[Todo]: List of Todo objects filtered by due date
        """
        return [todo for todo in todo_list if todo.due_date <= due_date]

    def by_keyword(self, todo_list: list[Todo], keyword: str):
        """"
        Return a list of Todo objects that has the keyword in their title or description

        :param todo_list: List of Todo objects to be filtered
        :param keyword: Keyword to filter by

        :return list[Todo]: List of Todo objects filtered by keyword
        """
        keyword = keyword.lower()
        return [todo for todo in todo_list if keyword in todo.title.lower() or keyword in todo.description.lower()]
    

    

        
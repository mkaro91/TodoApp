from models.TodoList import TodoList
from services.todo_service import TodoService

class TodoApp:
    """ Class to contain the application """
    def __init__(self):
        self.todo_list = TodoList()
        self.service = TodoService()

    def run(self):
        """
        Run the main interface of the application
        """
        while True:
            print(f"\n{'=' * 40}")
            print("TODO APP".center(40))
            print("=" * 40)

            print("1. View Todos")
            print("2. Add New Todo")
            print("3. Delete Todo")
            print("4. Complete Todo")
            print("5. Uncomplete Todo")
            print("0. Exit")

            choice = input("\n> ").strip()
            match choice:
                case "0": break
                case "1": self.service.view_todos(todo_list=self.todo_list)
                case "2": self.service.create_todo(todo_list=self.todo_list)
                case "3": self.service.delete_todo(todo_list=self.todo_list)
                case "4": self.service.complete_todo(todo_list=self.todo_list)
                case "5": self.service.uncomplete_todo(todo_list=self.todo_list)
                case _: print("\nInvalid selection.")

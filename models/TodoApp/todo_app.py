from datetime import datetime

from models.Todo import Todo, Priority
from models.TodoList import TodoList
from services.todo_service import TodoService

class TodoApp:
    """ Class to contain the application """
    def __init__(self):
        self.todo_list = TodoList()
        self.service = TodoService()

    def _print_result_list(self, results: list[Todo]):
        print("\n=== Results ===")
        if not results:
            print("No results.")
        else:
            for todo in results:
                print(todo)

    def _filter_menu(self):
        """ Runs the filter submenu """
        while True:
            print("\nFilter by:")
            print("1. Completed")
            print("2. Priority")
            print("3. Due Date")
            print("4. Keyword")
            print("0. Return to Main Menu")

            choice = input("\n> ").strip()
            match choice:
                case "0": break
                case "1":
                    print("\nFilter By:")
                    print("1. Completed")
                    print("2. Incomplete")
                    print("0. Cancel")

                    choice = input("\n> ").strip()
                    match choice:
                        case "0": pass

                        case "1": 
                            results = self.todo_list.filterer.by_completed(todo_list=self.todo_list.get_all(), is_completed=True)
                            self._print_result_list(results=results)

                        case "2": 
                            results = self.todo_list.filterer.by_completed(todo_list=self.todo_list.get_all(), is_completed=False)
                            self._print_result_list(results=results)

                        case _: 
                            print("Invalid selection.")

                case "2":
                    print("\nFilter By:")
                    print("1. Low Priority")
                    print("2. Medium Priority")
                    print("3. High Priority")
                    print("4. Critical Priority")
                    print("0. Cancel")

                    choice = input("\n> ").strip()
                    match choice:
                        case "0": pass

                        case "1": 
                            results = self.todo_list.filterer.by_priority(todo_list=self.todo_list.get_all(), priority=Priority.LOW)
                            self._print_result_list(results=results)

                        case "2": 
                            results = self.todo_list.filterer.by_priority(todo_list=self.todo_list.get_all(), priority=Priority.MEDIUM)
                            self._print_result_list(results=results)

                        case "3": 
                            results = self.todo_list.filterer.by_priority(todo_list=self.todo_list.get_all(), priority=Priority.HIGH)
                            self._print_result_list(results=results)

                        case "4": 
                            results = self.todo_list.filterer.by_priority(todo_list=self.todo_list.get_all(), priority=Priority.CRITICAL)
                            self._print_result_list(results=results)

                        case _: 
                            print("Invalid selection")

                case "3":
                    while True:
                        try:
                            due_date = datetime.strptime(input("\nEnter cutoff date: "), "%Y-%m-%d")
                            break
                        except ValueError:
                            print('Invalid date format. Must be YYYY-MM-DD')

                    results = self.todo_list.filterer.by_due_date(todo_list=self.todo_list.get_all(), due_date=due_date)
                    self._print_result_list(results=results)

                case "4":
                    kw = input("\nEnter Keyword: ").strip()

                    results = self.todo_list.filterer.by_keyword(todo_list=self.todo_list.get_all(), keyword=kw)
                    self._print_result_list(results=results)
                    
                case _: print("Invalid choice.")

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
            print("6. Filter Todos")
            print("0. Exit")

            choice = input("\n> ").strip()
            match choice:
                case "0": break
                case "1": self.service.view_todos(todo_list=self.todo_list)
                case "2": self.service.create_todo(todo_list=self.todo_list)
                case "3": self.service.delete_todo(todo_list=self.todo_list)
                case "4": self.service.complete_todo(todo_list=self.todo_list)
                case "5": self.service.uncomplete_todo(todo_list=self.todo_list)
                case "6": self._filter_menu()
                case _: print("\nInvalid selection.")

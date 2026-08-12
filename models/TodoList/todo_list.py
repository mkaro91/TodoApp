from models.Todo import Todo
from .todo_repository import TodoRepository

class TodoList:
    """ Represents a collection of Todos """
    def __init__(self) -> None:
        self.repo = TodoRepository()

    def _id_in_collection(self, todo_id):
        """
        Helper method to check if provided Todo ID is found in the collection

        :param todo_id: ID value to search collection keys for

        :return True: Matching ID located
        :return False: Matching ID not found
        """
        return todo_id in self.repo.get_all()

    def get_todo_by_id(self, todo_id: int) -> Todo | None:
        """ 
        Searches collection and returns Todo with matching ID or None if no Todo with matching ID is found 
        
        :param todo_id: ID value to search for in collection

        :return Todo: Todo with matching ID
        :return None: No Todo found with matching ID
        """
        return self.repo.get_todo_by_id(todo_id=todo_id)

    def add(self, todo: Todo) -> bool:
        """
        Adds a new Todo object to the collection

        :param todo: Todo object to be added to collection

        :return True: Todo object was successfully added to the collection
        :return False: Todo object was not added to collection
        """
        # Check if Todo already exists in collection
        if self._id_in_collection(todo_id=todo.id):
            return False
        
        self.repo.collection[todo.id] = todo
        return True

    def remove(self, todo_id: int) -> bool:
        """
        Removes a Todo object from collection using it's ID value

        :param todo_id: ID value to search collection for

        :return True: Matching ID was found and Todo object was removed from collection
        :return False: Todo object was not removed from collection
        """
    
        # Check matching Todo object was found in collection
        if not self._id_in_collection(todo_id=todo_id):
            return False

        del self.repo.collection[todo_id]
        return True

    def get_all(self) -> list[Todo]:
        """
        Returns a list of all Todo objects found in collection

        :return list[Todo]: List of all Todo objects
        """
        return list(self.repo.get_all().values())

    def get_completed(self) -> list[Todo]:
        """
        Returns a list of all completed Todo objects found in collection

        :return list[Todo]: List of all completed Todo objects found in collection
        """
        return [todo for todo in self.repo.get_all().values() if todo.completed]

    def get_pending(self) -> list[Todo]:
        """
        Returns a list of all incomplete Todo objects found in collection

        :return list[Todo]: List of all incomplete Todo objects found in collection
        """
        return [todo for todo in self.repo.get_all().values() if not todo.completed]
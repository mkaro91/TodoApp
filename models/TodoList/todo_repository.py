import json
from pathlib import Path

from models.Todo import Todo

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
SAVE_PATH = DATA_DIR / "collection.json"

class TodoRepository:
    def __init__(self):
        self.collection: dict[int, Todo] = self._load_todos() # Uses dictionary for faster and less expensive lookups
    
    def _collection_to_dict(self) -> dict[int, dict[str, any]]:
        """
        Returns current collection of Todo objects in serializable format

        :return dict[int, dict[str, any]]: Todo objects in serializable format
        """
        return {
            k: v.to_dict()
            for k, v in self.collection.items()
        }
        
    def _load_todos(self) -> dict:
        """
        Load Todo objects from JSON file

        :return dict: Returns loaded Todo objects or empty dictionary
        """
        try:
            with open(SAVE_PATH, 'r') as f:
                return {k: Todo.from_dict(v) for k, v in json.load(f).items()}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_todos(self) -> None:
        """
        Save Todo objects to JSON file
        """
        with open(SAVE_PATH, 'w') as f:
            json.dump(self._collection_to_dict(), f, indent=4)

    def get_all(self) -> dict[int, Todo]:
        """
        Returns all Todo objects currently stored in repository

        :return list[Todo]: entire collection
        """
        return self.collection

    def get_todo_by_id(self, todo_id: str) -> Todo | None:
        """
        Returns Todo object with ID that matches provided ID or None

        :return Todo: Todo object with matching ID
        :return None: No Todo object located with matching ID 
        """
        return self.collection.get(todo_id, None)
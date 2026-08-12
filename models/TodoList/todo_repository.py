import json
from pathlib import Path

from models.Todo import Todo

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
SAVE_PATH = DATA_DIR / "collection.json"

class TodoRepository:
    def __init__(self):
        self.collection: dict[int, Todo] = self._load_todos() # Uses dictionary for faster and less expensive lookups
        
    def _load_todos(self):
        """
        Load Todo objects from JSON file
        """
        collection = {}

        try:
            with open(SAVE_PATH, 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return collection

        for k, v in data.items():
            collection[k] = Todo.from_dict(v)

        return collection

    def save_todos(self):
        """
        Save Todo objects to JSON file
        """
        data = {
            k: v.to_dict()
            for k, v in self.collection.items()
        }

        with open(SAVE_PATH, 'w') as f:
            json.dump(data, f, indent=4)

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
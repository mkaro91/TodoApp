from datetime import datetime, date
from .priority import Priority
from .category import Category

class Todo:
    """ Represents a single task to be done """
    def __init__(self, id: int, title: str, description: str, category: Category, priority: Priority, due_date: date | None = None) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.due_date = due_date

        self.completed: bool = False
        self.created_date: date = datetime.now()

    def __str__(self) -> str:
        """ String representation of Todo object """
        return f"[{self.id}] {self.title} | Priority: {self.priority}"

    @classmethod
    def from_dict(cls, data):
        todo = cls(
            id = data['id'],
            title = data['title'],
            description = data['description'],
            category = Category(data['category']),
            priority = Priority(data['priority']),
            due_date = datetime.strptime(data['due_date'], "%Y-%m-%d") if data['due_date'] is not None else None
        )
        todo.completed = data['completed']
        todo.created_date = datetime.strptime(data['created_date'], "%Y-%m-%d")
        return todo

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority.value,
            'category': self.category.value,
            'due_date': self.due_date.strftime("%Y-%m-%d") if self.due_date is not None else None,
            'completed': self.completed,
            'created_date': self.created_date.strftime("%Y-%m-%d")
        }

    def complete(self) -> bool:
        """ 
        Completes task if task is currently incomplete 
        
        :return True: Todo was successfully completed
        :return False: Todo was not completed
        """
        if not self.completed:
            self.completed = True
            return True
        return False

    def uncomplete(self) -> bool:
        """ 
        Sets completed back to False if task is currently completed 
        
        :return True: Todo was uncompleted successfully
        :return False: Todo was not uncompleted
        """
        if self.completed:
            self.completed = False
            return True
        return False

    def is_overdue(self) -> bool:
        """ 
        Returns true if current date is greater than due date else returns false 
        
        :return True: Due date exists and current date is after due date
        :return False: Due date doesn't exist or current date is before or equal to due date 
        """
        if self.due_date == None:
            return False

        return datetime.now() > self.due_date
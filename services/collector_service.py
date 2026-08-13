from enum import Enum
from datetime import datetime

class Collector:
    def collect_enum_value(self, prompt: str, classname: Enum) -> Enum:
        """
        Ensures input is valid when converted to a given enum class

        :param prompt: Prompt to display to the user
        :param classname: Enum class for which input mmust be valid
        """
        while True:
            try:
                return classname(input(prompt).lower())
            except ValueError:
                print("Invalid input.")

    def collect_non_blank(self, prompt: str):
        """
        Collects input from the user while ensuring input is not blank

        :params prompt: Prompt to display to user
        """
        while True:
            value = input(prompt).strip()
            if value: return value
            print("Input cannot be blank.")

    def collect_todo_id(self):
        """
        Collects ID value from user
        """
        while True:
            try:
                return int(input("\nEnter Todo ID: ").strip())
            except ValueError:
                print("Enter a valid ID.")

    def collect_due_date(self):
        """ Collects Due date value from user. If blank input returns None """
        due_date = input("Due Date (Optional): ").strip()
       
        # Modify Due Date
        return datetime.strptime(due_date, "%Y-%m-%d") if due_date else None

    def collect_menu_choice(self):
        return self.collect_non_blank("\n> ")

    def collect_keyword(self):
        return self.collect_non_blank("\nKeyword: ")
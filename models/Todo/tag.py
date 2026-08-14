from datetime import datetime

class Tag:
    """ Represents a Tag object to be added to a Todo """
    def __init__(self, text):
        self.text = text
        self.created_date = datetime.now()

    @classmethod
    def from_dict(cls, data):
        tag = cls(
            text = data['text']
        )
        tag.created_date = datetime.strptime(data['created_date'], "%Y-%m-%d")
        return tag

    def to_dict(self):
        return {
            'text': self.text,
            'created_date': self.created_date.strftime("%Y-%m-%d")
        }
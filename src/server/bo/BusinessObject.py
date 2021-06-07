from abc import ABC, abstractmethod
from datetime import datetime

class BusinessObject(ABC):

    def __init__(self):
        self._id = 0
        self._creation_date = datetime.now().isoformat()

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_creation_date(self):
        return self._creation_date

    def set_creation_date(self, new_date):
        self._creation_date = new_date

    @staticmethod
    def date_format(date_string):
        if date_string is not None:
            return datetime.fromisoformat(date_string.replace("Z", ""))
        return None
from abc import ABC, abstractmethod


class BusinessObject(ABC):

    def __init__(self):
        self._id = 0
        self._creation_date = 0

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_creation_date(self):
        return self._creation_date

    def set_creation_date(self, new_date):
        self._creation_date = new_date

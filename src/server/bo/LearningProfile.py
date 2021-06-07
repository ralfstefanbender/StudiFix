from src.server.bo import NamedBusinessObject as bo
from abc import ABC, abstractmethod
class LearningProfile(bo.NamedBusinessObject, ABC):

    def __init__(self):
        super().__init__()
        self._prev_knowledge = 0
        self._extroversion = 0
        self._study_state = 0
        self._frequency = 0
        self._learntyp = 0  # Lerntypen sind kategorisiert nach Nummern
        self._semester = 0
        self._interest = ""
        self._degree_course = ""

    def get_frequency(self):
        return self._frequency

    def set_frequency(self, value):
        self._frequency = value

    def get_study_state(self):
        return self._study_state

    def set_study_state(self, value):
        self._study_state = value

    def get_extroversion(self):
        return self._extroversion

    def set_extroversion(self, value):
        self._extroversion = value

    def get_prev_knowledge(self):
        return self._prev_knowledge

    def set_prev_knowledge(self, value):
        self._prev_knowledge = value

    def get_learntyp(self):
        return self._learntyp

    def set_learntyp(self, value):
        self._learntyp = value

    def get_interest(self):
        return self._interest

    def set_interest(self, value):
        self._interest = value

    def get_semester(self):
        return self._semester

    def set_semester(self, value):
        self._semester = value

    def get_degree_course(self):
        return self._degree_course

    def set_degree_course(self, value):
        self._degree_course = value

    def get_group_id(self):
        return self._group_id

    def set_group_id(self, value):
        self._group_id = value




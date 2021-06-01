from src.server.bo import NamedBusinessObject as bo


class LearningProfileUser(bo.NamedBusinessObject):

    def __init__(self):
        super().__init__()
        self._user_id = 0
        self._prev_knowledge = 0
        self._extroversion = 0
        self._study_state = 0
        self._frequency = 0
        self._learntyp = 0  # Lerntypen sind kategorisiert nach Nummern
        self._semester = 0
        self._interest = ""
        self._degree_course = ""


    def get_user_id(self):
        return self._user_id

    def set_user_id(self, value):
        self._user_id = value

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

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Learningprofile Group()."""
        obj = LearningProfileUser()
        obj.set_id(dictionary["id"])
        obj.set_user_id(dictionary["user_id"])
        obj.set_name(dictionary["name"])
        obj.set_prev_knowledge(dictionary["prev_knowledge"])
        obj.set_extroversion(dictionary["extroversion"])
        obj.set_study_state(dictionary["study_state"])
        obj.set_frequency(dictionary["frequency"])
        obj.set_learntyp(dictionary["learntyp"])
        obj.set_semester(dictionary["semester"])
        obj.set_interest(dictionary["interest"])
        obj.set_degree_course(dictionary["degree_course"])
        obj.set_creation_date(LearningProfileUser.date_format(dictionary["creation_date"]))
        return obj
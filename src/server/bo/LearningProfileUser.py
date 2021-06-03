from src.server.bo import LearningProfile as bo


class LearningProfileUser(bo.LearningProfile):

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
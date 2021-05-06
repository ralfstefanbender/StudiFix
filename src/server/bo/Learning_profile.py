from src.server.bo import BusinessObject as bo


class LearningProfile(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._frequency = 0
        self._studystate = 0
        self._extroversion = 0
        self._profile_id = 0
        self._prev_knowledge = 0

    def get_frequency(self):
        return self._frequency

    def set_frequency(self, value):
        self._frequency = value

    def get_studystate(self):
        return self._studystate

    def set_studystate(self, value):
        self._studystate = value

    def get_extroversion(self):
        return self._extroversion

    def set_extroversion(self, value):
        self._extroversion = value

    def get_profile_id(self):
        return self._profile_id

    def set_profile_id(self, value):
        self._profile_id = value

    def get_prev_knowledge(self):
        return self._prev_knowledge

    def set_prev_knowledge(self, value):
        self._prev_knowledge = value

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen User()."""
        obj = LearningProfile()
        obj.set_id(dictionary["id"])
        obj.set_frequency(dictionary["frequency"])
        obj.set_studystate(dictionary["studystate"])
        obj.set_extroversion(dictionary["extroversion"])
        obj.set_profile_id(dictionary["profile_id"])
        obj.set_prev_knowledge(dictionary["prev_knowledge"])
        return obj

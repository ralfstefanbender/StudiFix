from src.server.bo import LearningProfile as bo


# Lernprofil für Gruppe Klasse
class LearningProfileGroup(bo.LearningProfile):

    def __init__(self):
        super().__init__()
        self._group_id = 0

    def get_group_id(self):
        return self._group_id

    def set_group_id(self, value):
        self._group_id = value

    # Lernprofil Gruppe aus einem Dict erstellen
    @staticmethod
    def from_dict(dictionary=dict()):
        obj = LearningProfileGroup()
        obj.set_id(dictionary["id"])
        obj.set_group_id(dictionary["group_id"])
        obj.set_name(dictionary["name"])
        obj.set_prev_knowledge(dictionary["prev_knowledge"])
        obj.set_extroversion(dictionary["extroversion"])
        obj.set_study_state(dictionary["study_state"])
        obj.set_frequency(dictionary["frequency"])
        obj.set_learntyp(dictionary["learntyp"])
        obj.set_semester(dictionary["semester"])
        obj.set_interest(dictionary["interest"])
        obj.set_degree_course(dictionary["degree_course"])
        obj.set_creation_date(LearningProfileGroup.date_format(dictionary["creation_date"]))
        return obj

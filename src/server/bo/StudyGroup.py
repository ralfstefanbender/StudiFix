from src.server.bo import NamedBusinessObject as bo


class StudyGroup(bo.NamedBusinessObject):

    "Realisierung der StudyGroup"

    def __init__(self):
        super().__init__()
        self._chat_id = 0
        self._learning_profile_id = 0


    def get_group_name(self):
        "Auslesen des Gruppennamens"
        return self._group_name

    def set_group_name(self, group_name):
        "Festlegen eines Gruppennamens"
        self._group_name = group_name

    def get_chat_id(self):
        "Auselesen der Chat-ID"
        return self._chat_id

    def set_chat_id(self, chat_id):
        "Festlegen einer Chat-ID"
        self._chat_id = chat_id

    def get_learning_profile_id(self):
        "Auselesen der learning_profile_id"
        return self._learning_profile_id

    def set_learning_profile_id(self, learning_profile_id):
        "Festlegen einer learning_profile_id"
        self._learning_profile_id = learning_profile_id

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen StudyGroup"""
        obj = StudyGroup()
        obj.set_id(dictionary["id"])
        obj.set_creation_date(dictionary["creation_date"])
        obj.set_name(dictionary["name"])
        obj.set_group_name(dictionary["group_name"])
        obj.set_chat_id(dictionary["chat_id"])
        obj.set_learning_profile_id(dictionary["learning_profile_id"])
        return obj
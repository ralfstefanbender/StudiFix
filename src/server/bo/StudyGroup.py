from src.server.bo import NamedBusinessObject as bo


class StudyGroup(bo.NamedBusinessObject):

    "Realisierung der StudyGroup"

    def __init__(self):
        super().__init__()
        self._chat_id = 0

    def get_chat_id(self):
        "Auselesen der Chat-ID"
        return self._chat_id

    def set_chat_id(self, chat_id):
        "Festlegen einer Chat-ID"
        self._chat_id = chat_id

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen StudyGroup"""
        obj = StudyGroup()
        obj.set_id(dictionary["id"])
        obj.set_name(dictionary["name"])
        obj.set_creation_date(StudyGroup.date_format(dictionary["creation_date"]))
        obj.set_chat_id(dictionary["chat_id"])
        return obj
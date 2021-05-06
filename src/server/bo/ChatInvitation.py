from src.server.bo.BusinessObject import BusinessObject

class ChatInvitation (BusinessObject):

    "Realisierung der ChatInvitation"

    def __init__(self):
        super().__init__()
        self._source_user = None
        self._target_user = None
        self._chat_id = ""
        self._is_accepted = False


    def get_source_user (self):
        "Auselsen des Absenders"
        return self._source_user

    def set_source_user (self, source_user):
        "Festlegen des Absenders"
        self._source_user = source_user

    def get_target_user (self):
        "Auslesen des Empfängers"
        return self._target_user

    def set_target_user (self, target_user):
        "Festlegen des Empfängers"
        self._target_user = target_user

    def get_chat_id (self):
        "Auslesen der Chat-ID"
        return self._chat_id

    def set_chat_id(self, chat_id):
        "Festlegen der Chat-ID"
        self._chat_id = chat_id

    def is_accepted(self):
        "Auslesen des Status"
        return self._is_accepted

    def set_accepted(self, value):
        "Akzeptieren der Einladung"
        self._is_accepted = value

    def switch_accepted(self):
        if self._is_accepted is True:
            self._is_accepted = False
        else:
            self._is_accepted = True



    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen StudyGroup"""
        obj = ChatInvitation()
        obj.set_id(dictionary["id"])
        obj.set_source_user(dictionary["source_user"])
        obj.set_target_user(dictionary["target_user"])
        obj.set_chat_id(dictionary["chat_id"])
        obj.set_accepted(dictionary["accepted"])
        return obj
from src.server.bo import BusinessObject as bo


class ChatInvitation (bo.BusinessObject):

    "Realisierung der ChatInvitation"

    def __init__(self):
        super().__init__()
        self._source_user = None
        self._target_user = None
        self._chat_id = 0
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

    def get_is_accepted(self):
        "Auslesen des Status"
        return self._is_accepted

    def set_is_accepted(self, value):
        "Akzeptieren der Einladung"
        self._is_accepted = value

    def switch_accepted(self):
        "Den Status umkehren"
        if self._is_accepted is True:
            self._is_accepted = False
        else:
            self._is_accepted = True



    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einer ChatInvitation"""
        obj = ChatInvitation()
        obj.set_id(dictionary["id"])
        obj.set_creation_date(dictionary["creation_date"])
        obj.set_source_user(dictionary["source_owner"])
        obj.set_target_user(dictionary["target_owner"])
        obj.set_chat_id(dictionary["chat_id"])
        obj.set_is_accepted(dictionary["is_accepted"])
        return obj
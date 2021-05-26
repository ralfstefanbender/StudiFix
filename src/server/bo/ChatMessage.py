from src.server.bo import BusinessObject as bo


class ChatMessage(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._chat_id = 0
        self._user_id = 0
        self._text = ""

    def get_chat_id(self):
        return self._chat_id

    def set_chat_id(self, value):
        self._chat_id = value

    def get_user_id(self):
        return self._user_id

    def set_user_id(self, value):
        self._user_id = value

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen User()."""
        obj = ChatMessage()
        obj.set_id(dictionary["id"])
        obj.set_chat_id(dictionary["chat_id"])
        obj.set_user_id(dictionary["user_id"])
        obj.set_text(dictionary["text"])
        obj.set_creation_date(ChatMessage.date_format(dictionary["creation_date"]))
        return obj

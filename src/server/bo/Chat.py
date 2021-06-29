from src.server.bo import NamedBusinessObject as bo

# Chat Klasse
class Chat(bo.NamedBusinessObject):
    def __init__(self):
        super().__init__()



    # Chat erstellung fon Dictionary
    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einer Chat"""
        obj = Chat()
        obj.set_id(dictionary["id"])
        obj.set_name(dictionary["name"])
        obj.set_creation_date(Chat.date_format(dictionary["creation_date"]))
        return obj
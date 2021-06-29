from src.server.bo import BusinessObject as bo


# Named Business Object Klasse (abstrakt)
class NamedBusinessObject(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._name = ""

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

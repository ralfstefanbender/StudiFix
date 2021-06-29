from src.server.bo import BusinessObject as bo


# User Klasse
class User(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._google_id = ""
        self._firstname = ""
        self._lastname = ""
        self._email = ""
        self._adress = ""

    def get_google_id(self):
        return self._google_id
    
    def set_google_id(self, value):
        self._google_id = value
    
    def get_firstname(self):
        return self._firstname
    
    def set_firstname(self, value):
        self._firstname = value

    def get_lastname(self):
        return self._lastname

    def set_lastname(self, value):
        self._lastname = value

    def get_email(self):
        return self._email

    def set_email(self, value):
        self._email = value

    def get_adress(self):
        return self._adress

    def set_adress(self, value):
        self._adress = value

    # User Object aus Dict erstellen
    @staticmethod
    def from_dict(dictionary=dict()):
        obj = User()
        obj.set_id(dictionary["id"])
        obj.set_creation_date(User.date_format(dictionary["creation_date"]))
        obj.set_google_id(dictionary["google_id"])
        obj.set_firstname(dictionary["firstname"])
        obj.set_lastname(dictionary["lastname"])
        obj.set_email(dictionary["email"])
        obj.set_adress(dictionary["adress"])
        return obj

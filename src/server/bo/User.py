from src.server.bo import NamedBusinessObject as bo


class User(bo.NamedBusinessObject):

    def __init__(self):
        super().__init__()
        self._google_id = ""
        self._firstname = ""
        self._lastname = ""
        self._email = ""
        self._learntyp = 0  # Lerntypen sind kategorisiert nach Nummern
        self._adress = ""
        self._interest = 0
        self._semester = 0
        self._degree_course = ""
                
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

    def get_learntyp(self):
        return self._learntyp

    def set_learntyp(self, value):
        self._learntyp = value

    def get_adress(self):
        return self._adress

    def set_adress(self, value):
        self._adress = value

    def get_interest(self):
        return self._interest

    def set_interest(self, value):
        self._interest = value

    def get_semester(self):
        return self._semester

    def set_semester(self, value):
        self._semester = value

    def get_degree_course(self):
        return self._degree_course

    def set_degree_course(self, value):
        self._degree_course = value

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen User()."""
        obj = User()
        obj.set_id(dictionary["id"])
        obj.set_creation_date(dictionary["creation_date"])
        obj.set_name(dictionary["name"])
        obj.set_google_id(dictionary["google_id"])
        obj.set_first_name(dictionary["first_name"])
        obj.set_last_name(dictionary["last_name"])
        obj.set_email(dictionary["email"])
        obj.set_lerntyp(dictionary["lerntyp"])
        obj.set_adress(dictionary["adress"])
        obj.set_interest(dictionary["interest"])
        obj.set_semester(dictionary["semester"])
        obj.set_degree_course(dictionary["degree_course"])
        return obj

from src.server.bo import BusinessObject as bo


class User(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._google_id = ""
        self._first_name = ""
        self._last_name = ""
        self._email = ""
        self._lerntyp = 0  # Lerntypen sind kategorisiert nach Nummern
        self._adress = ""
        self._interest = []
        self._semester = 0
        self._degree_course = ""
                
    def get_google_id(self):
        return self._google_id
    
    def set_google_id(self, value):
        self._google_id = value
    
    def get_first_name(self):
        return self._first_name
    
    def set_first_name(self, value):
        self._first_name = value

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, value):
        self._last_name = value

    def get_email(self):
        return self._email

    def set_email(self, value):
        self._email = value

    def get_lerntyp(self):
        return self._lerntyp

    def set_lerntyp(self, value):
        self._lerntyp = value

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

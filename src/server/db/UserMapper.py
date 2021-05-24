from src.server.db.Mapper import Mapper
from src.server.bo.User import User

"""User Objekte werden noch nicht erzeugt. 
   Business Objekte fehlen noch alle"""

"""Standartaktion: Erstellung des BO's kann in eigene Methode auslager --> zeilen sparen"""


class UserMapper(Mapper):

    def __init__(self):
        super().__init__()

    def build_bo(self, tuples):

        result = []

        if len(tuples) == 1:
            for (id, firstname, lastname, adress, email, google_id, creation_date, learning_profile_id) in tuples:

                user = User()
                user.set_id(id)
                user.set_firstname(firstname)
                user.set_lastname(lastname)
                user.set_adress(adress)
                user.set_email(email)
                user.set_google_id(google_id)
                user.set_creation_date(creation_date)
                user.set_learning_profile_id(learning_profile_id)
                result = user
        else:
            for (id, firstname, lastname, adress, email, google_id, creation_date, learning_profile_id) in tuples:

                user = User()
                user.set_id(id)
                user.set_firstname(firstname)
                user.set_lastname(lastname)
                user.set_adress(adress)
                user.set_email(email)
                user.set_google_id(google_id)
                user.set_creation_date(creation_date)
                user.set_learning_profile_id(learning_profile_id)
                result.append(user)

        return result

    def find_all(self):

        result = []

        cursor = self._cnx.cursor()
        command = "SELECT * FROM user"
        cursor.execute(command)
        tuples = cursor.fetchall()

        result = (self.build_bo(tuples))

        self._cnx.commit()
        cursor.close()

        return result

    def find_user_by_email(self, email):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, firstname, lastname, adress, email, " \
                  "google_id, creation_date, learning_profile_id FROM user WHERE email LIKE '{}'".format(email)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)
        except IndexError:
            """Falls kein User mit der angegebenen email gefunden werden konnte,
            wird hier None als Rückgabewert deklariert"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_user_by_google_id(self, google_id):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, firstname, lastname, adress, email, " \
                  "google_id, creation_date, learning_profile_id FROM user WHERE google_id LIKE '{}' ".format(google_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        """Haben wir einen Tuple gefunden ? -> ja BO bauen -> nein nix zurück geben. """
        if len(tuples) != 0:
            try:
                result = self.build_bo(tuples)
            except IndexError:
                """Falls kein User mit der angegebenen email gefunden werden konnte,
                wird hier None als Rückgabewert deklariert"""
                result = None
        else:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_user_by_firstname(self, firstname):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, firstname, lastname, adress, email, " \
                  "google_id, creation_date, learning_profile_id FROM user WHERE firstname LIKE '{}' ".format(firstname)
        cursor.execute(command)
        tuples = cursor.fetchall()

        """Haben wir einen Tuple gefunden ? -> ja BO bauen -> nein nix zurück geben. """
        if len(tuples) != 0:
            try:
                result = self.build_bo(tuples)
            except IndexError:
                """Falls kein User mit dem angegebenen Vornamen gefunden werden konnte,
                wird hier None als Rückgabewert deklariert"""
                result = None
        else:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_user_by_lastname(self, lastname):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, firstname, lastname, adress, email, " \
                  "google_id, creation_date, learning_profile_id FROM user WHERE lastname LIKE '{}' ".format(lastname)
        cursor.execute(command)
        tuples = cursor.fetchall()

        """Haben wir einen Tuple gefunden ? -> ja BO bauen -> nein nix zurück geben. """
        if len(tuples) != 0:
            try:
                result = self.build_bo(tuples)
            except IndexError:
                """Falls kein User mit der angegebenenm Nachnamen gefunden werden konnte,
                wird hier None als Rückgabewert deklariert"""
                result = None
        else:
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, id):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, firstname, lastname, adress, email," \
                  " google_id, creation_date, learning_profile_id FROM user WHERE id LIKE '{}' ".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)
        except IndexError:
            """Falls kein User mit der angegebenen id gefunden werden konnte,
            wird hier None als Rückgabewert deklariert"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_user_by_learning_profile_id(self, learning_profile_id):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, firstname, lastname, adress, email, " \
                  "google_id, creation_date, learning_profile_id FROM user " \
                  "WHERE learning_profile_id LIKE '{}' ".format(learning_profile_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)
        except IndexError:
            """Falls kein User mit der angegebenen learning_profile_id gefunden werden konnte,
            wird hier None als Rückgabewert deklariert"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, user):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as maxid from user")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                user.set_id(1)
            else:
                user.set_id(maxid[0]+1)

        command = "INSERT INTO user (id, firstname, lastname, adress, " \
                  "email, google_id, creation_date, learning_profile_id)" \
                  "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')"\
                .format(user.get_id(), user.get_firstname(), user.get_lastname(), user.get_adress(), user.get_email(),
                        user.get_google_id(), user.get_creation_date(), user.get_learning_profile_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def update(self, user):

        cursor = self._cnx.cursor()
        command = "UPDATE user SET firstname = ('{}'), lastname = ('{}'), adress = ('{}')," \
                  " email = ('{}'), google_id = ('{}'),"\
                  " creation_date = ('{}'), learning_profile_id = ('{}'),"\
                  "WHERE id = ('{}')"\
            .format(user.get_firstname(), user.get_lastname(), user.get_adress(), user.get_email(),
                    user.get_google_id(), user.get_creation_date(), user.get_learning_profile_id(), user.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, user):

        cursor = self._cnx.cursor()
        try:
            cursor.execute("DELETE FROM user WHERE id LIKE ('{}');".format(user.get_id()))
        except:
            print("User konnte nicht gefunden werden!")

        self._cnx.commit()
        cursor.close()


if __name__ == "__main__":
    with UserMapper() as mapper:
        # Nach mapper jegliche Methode dieser Klasse
        user = User()
        user.set_firstname("Hans")
        user.set_lastname("Müller")
        user.set_google_id("dfasdfasdfasdf")
        user.set_email("dfasdfasdfasdf")
        user.set_learning_profile_id(1)
        mapper.insert(user)
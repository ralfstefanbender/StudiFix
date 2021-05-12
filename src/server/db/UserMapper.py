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
            for (id, firstname, lastname, adress, semester, degree_course, interest,
                 learntyp, email, google_id, creation_date) in tuples:

                user = User()
                user.set_id(id)
                user.set_firstname(firstname)
                user.set_lastname(lastname)
                user.set_adress(adress)
                user.set_semester(semester)
                user.set_degree_course(degree_course)
                user.set_interest(interest)
                user.set_learntyp(learntyp)
                user.set_email(email)
                user.set_google_id(google_id)
                user.set_creation_date(creation_date)
                result = user
        else:
            for (id, firstname, lastname, adress, semester, degree_course, interest,
                 learntyp, email, google_id, creation_date) in tuples:

                user = User()
                user.set_id(id)
                user.set_firstname(firstname)
                user.set_lastname(lastname)
                user.set_adress(adress)
                user.set_semester(semester)
                user.set_degree_course(degree_course)
                user.set_interest(interest)
                user.set_learntyp(learntyp)
                user.set_email(email)
                user.set_google_id(google_id)
                user.set_creation_date(creation_date)
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
        command = "SELECT id, firstname, lastname, adress, semester, degree_course, interest, learntyp, email, google_id, creation_date FROM user WHERE email LIKE '{}' ".format(email)
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
        command = "SELECT id, firstname, lastname, adress, semester, degree_course, interest, learntyp, email, google_id, creation_date FROM user WHERE google_id LIKE '{}' ".format(google_id)
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

    def find_by_id(self, id):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, firstname, lastname, adress, semester, degree_course, interest, learntyp, email," \
                  " google_id, creation_date FROM user WHERE id LIKE '{}' ".format(id)
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

    def insert(self, user):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as maxid from user")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                user.set_id(1)
            else:
                user.set_id(maxid[0]+1)

        command = "INSERT INTO user (id, firstname, lastname, adress, semester, degree_course, interest, learntyp," \
                  "email, google_id, creation_date) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"\
                .format(user.get_id(), user.get_firstname(), user.get_lastname(), user.get_adress(), user.get_semester()
                        , user.get_degree_course(), user.get_interest(), user.get_learntyp(), user.get_email(),
                        user.get_google_id(), user.get_creation_date())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def update(self, user):

        cursor = self._cnx.cursor()
        command = "UPDATE user SET firstname = ('{}'), lastname = ('{}'), adress = ('{}'), semester = ('{}')," \
                  " degree_course = ('{}'), interest = ('{}'), learntyp = ('{}'), email = ('{}'), google_id = ('{}'),"\
                  " creation_date = ('{}'),"\
                  "WHERE id = ('{}')"\
            .format(user.get_firstname(), user.get_lastname(), user.get_adress(), user.get_semester(),
                    user.get_degree_course(), user.get_interest(), user.get_learntyp(), user.get_email(),
                    user.get_google_id(), user.get_creation_date(), user.get_id())
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
        user.set_name("Hallo")
        user.set_google_id("dfasdfasdfasdf")
        user.set_email("dfasdfasdfasdf")
        mapper.insert(user)
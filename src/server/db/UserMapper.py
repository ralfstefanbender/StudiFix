from src.server.db.Mapper import Mapper
from src.server.bo.User import User


class UserMapper(Mapper):
    """Mapper-Klasse, die User-Objekte auf eine relationale
    Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur Verfügung
    gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und
    gelöscht werden können. Das Mapping ist bidirektional. D.h., Objekte können
    in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    """

    def __init__(self):
        super().__init__()


    def build_bo(self, tuples):
        """BO wird aufgebaut und in späteren Methoden aufgegriffen.
        So spart man sich das immer wieder aufbauen des BOs später"""

        result = []

        if len(tuples) == 1:
            "Baue nur einen"

            for (id, firstname, lastname, adress, email, google_id, creation_date) in tuples:

                user = User()
                user.set_id(id)
                user.set_firstname(firstname)
                user.set_lastname(lastname)
                user.set_adress(adress)
                user.set_email(email)
                user.set_google_id(google_id)
                user.set_creation_date(creation_date)
                result = user

        else:
            "Baue mehrere"

            for (id, firstname, lastname, adress, email, google_id, creation_date) in tuples:

                user = User()
                user.set_id(id)
                user.set_firstname(firstname)
                user.set_lastname(lastname)
                user.set_adress(adress)
                user.set_email(email)
                user.set_google_id(google_id)
                user.set_creation_date(creation_date)
                result.append(user)

        return result


    def find_all(self):
        """Auslesen aller User in unserem System.

        :return Eine Sammlung mit User-Objekten.
        """

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
        """Auslesen aller User anhand der zugeordneten E-Mail-Adresse.

        :param email, E-Mail-Adresse der zugehörigen Benutzer.
        :return Eine Sammlung mit User-Objekten, die sämtliche User
            mit der gewünschten E-Mail-Adresse enthält.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, firstname, lastname, adress, email, " \
                  "google_id, creation_date FROM user WHERE email LIKE '{}'".format(email)
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
        """Suchen eines Users mit vorgegebener Google ID. Da diese eindeutig ist,
        wird genau ein Objekt zurückgegeben.

        :param google_id, die Google ID des gesuchten Users.
        :return User-Objekt, das die übergebene Google ID besitzt,
            None bei nicht vorhandenem DB-Tupel.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, firstname, lastname, adress, email, " \
                  "google_id, creation_date FROM user WHERE google_id LIKE '{}' ".format(google_id)
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
        """Auslesen aller Kunden anhand des FirstNames.

        :param firstname
        :return Eine Sammlung mit User-Objekten, die sämtliche User
            mit dem gewünschten FirstName enthält.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, firstname, lastname, adress, email, " \
                  "google_id, creation_date FROM user WHERE firstname LIKE '{}' ".format(firstname)
        cursor.execute(command)
        tuples = cursor.fetchall()

        """Haben wir einen Tuple gefunden ? -> ja BO bauen -> nein nix zurück geben. """
        if len(tuples) != 0:
            try:
                result = self.build_bo(tuples)

            except IndexError:
                """Falls kein User mit dem angegebenen FirstName gefunden werden konnte,
                wird hier None als Rückgabewert deklariert"""

                result = None

        else:
            result = None

        self._cnx.commit()
        cursor.close()

        return result


    def find_user_by_lastname(self, lastname):
        """Auslesen aller User anhand des LastName.

        :param lastname 
        :return Eine Sammlung mit User-Objekten, die sämtliche Kunden
            mit dem gewünschten Nachnamen enthält.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, firstname, lastname, adress, email, " \
                  "google_id, creation_date FROM user WHERE lastname LIKE '{}' ".format(lastname)
        cursor.execute(command)
        tuples = cursor.fetchall()

        """Haben wir einen Tuple gefunden ? -> ja BO bauen -> nein nix zurück geben. """
        if len(tuples) != 0:
            try:
                result = self.build_bo(tuples)

            except IndexError:
                """Falls kein User mit dem angegebenenm LastName gefunden werden konnte,
                wird hier None als Rückgabewert deklariert"""

                result = None
        else:
            result = None

        self._cnx.commit()
        cursor.close()

        return result


    def find_by_id(self, id):
        """Suchen eines Users mit vorgegebener ID. Da diese eindeutig ist,
        wird genau ein Objekt zurückgegeben.

        :param id Primärschlüsselattribut (->DB)
        :return User-Objekt, das dem übergebenen Schlüssel entspricht, None bei
                nicht vorhandenem DB-Tupel.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, firstname, lastname, adress, email," \
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
        """Einfügen eines User-Objekts in die Datenbank.

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf.
        berichtigt.

        :param user das zu speichernde Objekt
        :return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as maxid from user")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die ChatInvitation-Tabelle leer ist und wir mit der ID 1 beginnen können."""

                user.set_id(1)

            else:
                """Wenn wir eine maximale ID festellen konnten, zählen wir diese
                um 1 hoch und weisen diesen Wert als ID dem ChatInvitation-Objekt zu."""

                user.set_id(maxid[0]+1)

        command = "INSERT INTO user (id, firstname, lastname, adress, " \
                  "email, google_id, creation_date)" \
                  "VALUES ('{}','{}','{}','{}','{}','{}','{}')"\
                .format(user.get_id(),
                        user.get_firstname(),
                        user.get_lastname(),
                        user.get_adress(),
                        user.get_email(),
                        user.get_google_id(),
                        user.get_creation_date()
                        )
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


    def update(self, user):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.

        :param user das Objekt, das in die DB geschrieben werden soll
        """

        cursor = self._cnx.cursor()
        command = "UPDATE user SET firstname = ('{}'), lastname = ('{}'), adress = ('{}')," \
                  " email = ('{}'), google_id = ('{}'), creation_date = ('{}') WHERE id = ('{}')"\
            .format(user.get_firstname(),
                    user.get_lastname(),
                    user.get_adress(),
                    user.get_email(),
                    user.get_google_id(),
                    user.get_creation_date(),
                    user.get_id()
                    )
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


    def delete(self, user):
        """Löschen der Daten eines ChatInvitation-Objekts aus der Datenbank.

        :param user das aus der DB zu löschende "Objekt"
        """

        cursor = self._cnx.cursor()
        try:
            cursor.execute("DELETE FROM user WHERE id LIKE ('{}');".format(user.get_id()))
        except:
            print("User konnte nicht gefunden werden!")

        self._cnx.commit()
        cursor.close()


# Zum Testen ausführen
if __name__ == "__main__":
    with UserMapper() as mapper:

        user = User()
        user.set_firstname("Hans")
        user.set_lastname("Müller")
        user.set_google_id("dfasdfasdfasdf")
        user.set_email("dfasdfasdfasdf")
        mapper.insert(user)
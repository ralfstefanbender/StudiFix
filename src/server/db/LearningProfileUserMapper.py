from src.server.db.Mapper import Mapper
from src.server.bo.LearningProfileUser import LearningProfileUser


class LearningProfileUserMapper(Mapper):
    """Mapper-Klasse, die LearningProfileUser-Objekte auf eine relationale
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

            for (id, user_id, name, prev_knowledge, extroversion, study_state, frequency,
                 learntyp, semester, interest, degree_course, creation_date) in tuples:
                learning_profile_user = LearningProfileUser()
                learning_profile_user.set_id(id)
                learning_profile_user.set_user_id(user_id)
                learning_profile_user.set_name(name)
                learning_profile_user.set_prev_knowledge(prev_knowledge)
                learning_profile_user.set_extroversion(extroversion)
                learning_profile_user.set_study_state(study_state)
                learning_profile_user.set_frequency(frequency)
                learning_profile_user.set_learntyp(learntyp)
                learning_profile_user.set_semester(semester)
                learning_profile_user.set_interest(interest)
                learning_profile_user.set_degree_course(degree_course)
                learning_profile_user.set_creation_date(creation_date)
                result = learning_profile_user

        else:
            "Baue mehrere"

            for (id, user_id, name, prev_knowledge, extroversion, study_state, frequency,
                 learntyp, semester, interest, degree_course, creation_date) in tuples:
                learning_profile_user = LearningProfileUser()
                learning_profile_user.set_id(id)
                learning_profile_user.set_user_id(user_id)
                learning_profile_user.set_name(name)
                learning_profile_user.set_prev_knowledge(prev_knowledge)
                learning_profile_user.set_extroversion(extroversion)
                learning_profile_user.set_study_state(study_state)
                learning_profile_user.set_frequency(frequency)
                learning_profile_user.set_learntyp(learntyp)
                learning_profile_user.set_semester(semester)
                learning_profile_user.set_interest(interest)
                learning_profile_user.set_degree_course(degree_course)
                learning_profile_user.set_creation_date(creation_date)
                result.append(learning_profile_user)

        return result


    def find_all(self):
        """Auslesen aller LearningProfileUser in unserem System.

        :return Eine Sammlung mit LearningProfileUser-Objekten.
        """

        result = []

        cursor = self._cnx.cursor()
        command = "SELECT * FROM learning_profile_user"
        cursor.execute(command)
        tuples = cursor.fetchall()

        result = self.build_bo(tuples)

        self._cnx.commit()
        cursor.close()

        return result


    def find_by_id(self, id):
        """Suchen eines LearningProfileUsers mit vorgegebener ID. Da diese eindeutig ist,
        wird genau ein Objekt zurückgegeben.

        :param id Primärschlüsselattribut (->DB)
        :return LearningProfileUser-Objekt, das dem übergebenen Schlüssel entspricht, None bei
                nicht vorhandenem DB-Tupel.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, user_id, name, prev_knowledge, extroversion, study_state, frequency," \
                  "learntyp, semester, interest, degree_course, creation_date FROM learning_profile_user " \
                  "WHERE id LIKE '{}' ".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""

            result = None

        self._cnx.commit()
        cursor.close()

        return result


    def find_by_user_id(self, user_id):
        """Suchen eines LearningProfileUsers mit vorgegebener user_id. Da diese eindeutig ist,
        wird genau ein Objekt zurückgegeben.

        :param user_id 
        :return LearningProfileUser-Objekt, das dem übergebenen Schlüssel entspricht, None bei
                nicht vorhandenem DB-Tupel.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, user_id, name, prev_knowledge, extroversion, study_state, frequency," \
                  "learntyp, semester, interest, degree_course, creation_date FROM learning_profile_user " \
                  "WHERE user_id LIKE '{}' ".format(user_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""

            result = None

        self._cnx.commit()
        cursor.close()

        return result


    def get_user_id_by_learningprofile_id(self, id):
        """Suchen eines LearningProfileUsers mit vorgegebener id. Da diese eindeutig ist,
        wird genau ein Objekt zurückgegeben.

        :param id 
        :return LearningProfileUser-Objekt, das dem übergebenen Schlüssel entspricht, None bei
                nicht vorhandenem DB-Tupel.
        """


        cursor = self._cnx.cursor()
        command = "SELECT user_id FROM learning_profile_user WHERE id LIKE '{}' ".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = tuples[0][0]

        except IndexError:
            """Falls kein LearningProfileUser mit der angegebenen user_id gefunden werden konnte,
                wird hier None als Rückgabewert deklariert"""
                
            result = None

        self._cnx.commit()
        cursor.close()

        return result


    def find_by_name(self, name):
        """Auslesen aller LearningProfileUser anhand des UserNames.

        :param name 
        :return Eine Sammlung mit LearningProfileUser-Objekten, die sämtliche LearningProfileGroups
            mit dem gewünschten Namen enthält.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, user_id, name, prev_knowledge, extroversion, study_state, frequency," \
                  "learntyp, semester, interest, degree_course, creation_date FROM learning_profile_user " \
                  "WHERE name LIKE '{}' ".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""

            result = None

        self._cnx.commit()
        cursor.close()

        return result


    def insert(self, learning_profile_user):
        """Einfügen eines LearningProfileUser-Objekts in die Datenbank.

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf.
        berichtigt.

        :param learning_profile_user das zu speichernde Objekt
        :return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM learning_profile_user ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            learning_profile_user.set_id(maxid[0] + 1)

        command = "INSERT INTO learning_profile_user (id, user_id, name, prev_knowledge, extroversion, study_state, " \
                  "frequency, " \
                  "learntyp, semester, interest, degree_course, creation_date) VALUES" \
                  " (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        data = (learning_profile_user.get_id(),
                learning_profile_user.get_user_id(),
                learning_profile_user.get_name(),
                learning_profile_user.get_prev_knowledge(),
                learning_profile_user.get_extroversion(),
                learning_profile_user.get_study_state(),
                learning_profile_user.get_frequency(),
                learning_profile_user.get_learntyp(),
                learning_profile_user.get_semester(),
                learning_profile_user.get_interest(),
                learning_profile_user.get_degree_course(),
                learning_profile_user.get_creation_date()
                )
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return learning_profile_user


    def update(self, learning_profile):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.

        :param learning_profile ist das Objekt, das in die DB geschrieben werden soll
        """

        cursor = self._cnx.cursor()

        command = "UPDATE learning_profile_user SET name = ('{}'), user_id = ('{}'), prev_knowledge = ('{}'), extroversion = ('{}')," \
                  " study_state = ('{}'), frequency = ('{}'), learntyp = ('{}'), semester = ('{}')," \
                  " interest = ('{}'), degree_course = ('{}'), creation_date = ('{}') WHERE id = ('{}')" \
            .format(
                    learning_profile.get_name(),
                    learning_profile.get_user_id(),
                    learning_profile.get_prev_knowledge(),
                    learning_profile.get_extroversion(),
                    learning_profile.get_study_state(),
                    learning_profile.get_frequency(),
                    learning_profile.get_learntyp(),
                    learning_profile.get_semester(),
                    learning_profile.get_interest(),
                    learning_profile.get_degree_course(),
                    learning_profile.get_creation_date(),
                    learning_profile.get_id()
                    )

        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


    def delete(self, learning_profile_user):
        """Löschen der Daten eines LearningProfileUser-Objekts aus der Datenbank.

        :param learning_profile_user ist das aus der DB zu löschende "Objekt"
        """

        cursor = self._cnx.cursor()
        command = "DELETE FROM learning_profile_user WHERE id = ('{}')".format(learning_profile_user.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


# Zum Testen ausführen
if (__name__ == "__main__"):
    with LearningProfileUserMapper() as mapper:
        learning_profile = LearningProfileUser()
        learning_profile.set_name("Informatik")
        learning_profile.set_user_id(1)
        learning_profile.set_prev_knowledge("Garkeine")
        learning_profile.set_extroversion(2)
        learning_profile.set_study_state(3)
        learning_profile.set_frequency(4)
        learning_profile.set_learntyp(5)
        learning_profile.set_semester(6)
        learning_profile.set_degree_course("Wirtschaftsinformatik")

        mapper.insert(learning_profile)
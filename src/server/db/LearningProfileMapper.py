from src.server.db.Mapper import Mapper
from src.server.bo.LearningProfile import LearningProfile


class LearningProfileMapper(Mapper):
    """Mapper-Klasse, die LearningProfile-Objekte auf eine relationale
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

            for (id, name, prev_knowledge, extroversion, study_state, frequency,
                 learntyp, semester, interest, degree_course, creation_date) in tuples:
                learning_profile = LearningProfile()
                learning_profile.set_id(id)
                learning_profile.set_name(name)
                learning_profile.set_prev_knowledge(prev_knowledge)
                learning_profile.set_extroversion(extroversion)
                learning_profile.set_study_state(study_state)
                learning_profile.set_frequency(frequency)
                learning_profile.set_learntyp(learntyp)
                learning_profile.set_semester(semester)
                learning_profile.set_interest(interest)
                learning_profile.set_degree_course(degree_course)
                learning_profile.set_creation_date(creation_date)
                result = learning_profile

        else:
            "Baue mehrere"

            for (id, name, prev_knowledge, extroversion, study_state, frequency,
                 learntyp, semester, interest, degree_course, creation_date) in tuples:
                learning_profile = LearningProfile()
                learning_profile.set_id(id)
                learning_profile.set_name(name)
                learning_profile.set_prev_knowledge(prev_knowledge)
                learning_profile.set_extroversion(extroversion)
                learning_profile.set_study_state(study_state)
                learning_profile.set_frequency(frequency)
                learning_profile.set_learntyp(learntyp)
                learning_profile.set_semester(semester)
                learning_profile.set_interest(interest)
                learning_profile.set_degree_course(degree_course)
                learning_profile.set_creation_date(creation_date)
                result.append(learning_profile)

        return result


    def find_all(self):
        """Auslesen aller LearningProfiles in unserem System.

        :return Eine Sammlung mit LearningProfile-Objekten.
        """

        result = []

        cursor = self._cnx.cursor()
        command = "SELECT * FROM learning_profile"
        cursor.execute(command)
        tuples = cursor.fetchall()

        result = self.build_bo(tuples)

        self._cnx.commit()
        cursor.close()

        return result


    def find_by_id(self, id):
        """Suchen einer LearningProfile mit vorgegebener ID. Da diese eindeutig ist,
        wird genau ein Objekt zurückgegeben.

        :param id Primärschlüsselattribut (->DB)
        :return LearningProfile-Objekt, das dem übergebenen Schlüssel entspricht, None bei
                nicht vorhandenem DB-Tupel.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, prev_knowledge, extroversion, study_state, frequency," \
                  "learntyp, semester, interest, degree_course, creation_date FROM learning_profile " \
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


    def find_by_name(self, name):
        """Auslesen aller LearningProfile anhand des names.

        :param name 
        :return Eine Sammlung mit LearningProfile-Objekten, die sämtliche LearningProfile
            mit dem gewünschten Namen enthält.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, prev_knowledge, extroversion, study_state, frequency," \
                  "learntyp, semester, interest, degree_course, creation_date FROM learning_profile " \
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


    def insert(self, learning_profile):
        """Einfügen eines LearningProfile-Objekts in die Datenbank.

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf.
        berichtigt.

        :param learning_profile das zu speichernde Objekt
        :return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as maxid from learning_profile")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                learning_profile.set_id(1)
            else:
                learning_profile.set_id(maxid[0] + 1)

        command = "INSERT INTO learning_profile (id, name, prev_knowledge, extroversion, study_state, frequency," \
                  "learntyp, semester, interest, degree_course, creation_date) VALUES " \
                  "('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')" \
            .format(learning_profile.get_id(),
                    learning_profile.get_name(),
                    learning_profile.get_prev_knowledge(),
                    learning_profile.get_extroversion(),
                    learning_profile.get_study_state(),
                    learning_profile.get_frequency(),
                    learning_profile.get_learntyp(),
                    learning_profile.get_semester(),
                    learning_profile.get_interest(),
                    learning_profile.get_degree_course(),
                    learning_profile.get_creation_date()
                    )
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

        return learning_profile


    def update(self, learning_profile):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.

        :param learning_profile ist das Objekt, das in die DB geschrieben werden soll
        """

        cursor = self._cnx.cursor()
        command = "UPDATE learning_profile SET name = ('{}'), prev_knowledge = ('{}'), extroversion = ('{}')," \
                  " study_state = ('{}'), frequency = ('{}'), learntyp = ('{}'), semester = ('{}')," \
                  " interest = ('{}'), degree_course = ('{}'), creation_date = ('{}') WHERE id = ('{}')" \
            .format(learning_profile.get_name(),
                    learning_profile.get_prev_knowledge(),
                    learning_profile.get_extroversion(),
                    learning_profile.get_study_state(),
                    learning_profile.get_frequency(),
                    learning_profile.get_learntyp(),
                    learning_profile.get_semester(),
                    learning_profile.get_interest(),
                    learning_profile.get_degree_course(),
                    learning_profile.get_creation_date(),
                    learning_profile.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


    def delete(self, learning_profile):
        """Löschen der Daten eines LearningProfileUser-Objekts aus der Datenbank.

        :param learning_profile ist das aus der DB zu löschende "Objekt"
        """

        cursor = self._cnx.cursor()
        command = "DELETE FROM learning_profile WHERE id = ('{}')".format(learning_profile.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


# Zum Testen ausführen
if (__name__ == "__main__"):
    with LearningProfileMapper() as mapper:
        learning_profile = LearningProfile()
        learning_profile.set_name("Informatik")
        learning_profile.set_prev_knowledge("Garkeine")
        learning_profile.set_extroversion(2)
        learning_profile.set_study_state(3)
        learning_profile.set_frequency(4)
        learning_profile.set_learntyp(5)
        learning_profile.set_semester(6)
        learning_profile.set_degree_course("Wirtschaftsinformatik")

        mapper.insert(learning_profile)
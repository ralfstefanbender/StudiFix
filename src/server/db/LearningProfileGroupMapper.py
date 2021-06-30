from src.server.db.Mapper import Mapper
from src.server.bo.LearningprofileGroup import LearningProfileGroup


class LearningProfileGroupMapper(Mapper):
    """Mapper-Klasse, die LearningProfileGroup-Objekte auf eine relationale
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

            for (id, group_id, name, prev_knowledge, extroversion, study_state, frequency,
                 learntyp, semester, interest, degree_course, creation_date) in tuples:
                learning_profile_group = LearningProfileGroup()
                learning_profile_group.set_id(id)
                learning_profile_group.set_group_id(group_id)
                learning_profile_group.set_name(name)
                learning_profile_group.set_prev_knowledge(prev_knowledge)
                learning_profile_group.set_extroversion(extroversion)
                learning_profile_group.set_study_state(study_state)
                learning_profile_group.set_frequency(frequency)
                learning_profile_group.set_learntyp(learntyp)
                learning_profile_group.set_semester(semester)
                learning_profile_group.set_interest(interest)
                learning_profile_group.set_degree_course(degree_course)
                learning_profile_group.set_creation_date(creation_date)
                result = learning_profile_group

        else:
            "Baue mehrere"

            for (id, group_id, name, prev_knowledge, extroversion, study_state, frequency,
                 learntyp, semester, interest, degree_course, creation_date) in tuples:
                learning_profile_group = LearningProfileGroup()
                learning_profile_group.set_id(id)
                learning_profile_group.set_group_id(group_id)
                learning_profile_group.set_name(name)
                learning_profile_group.set_prev_knowledge(prev_knowledge)
                learning_profile_group.set_extroversion(extroversion)
                learning_profile_group.set_study_state(study_state)
                learning_profile_group.set_frequency(frequency)
                learning_profile_group.set_learntyp(learntyp)
                learning_profile_group.set_semester(semester)
                learning_profile_group.set_interest(interest)
                learning_profile_group.set_degree_course(degree_course)
                learning_profile_group.set_creation_date(creation_date)
                result.append(learning_profile_group)

        return result


    def find_all(self):
        """Auslesen aller LearningProfileGroups in unserem System.

        :return Eine Sammlung mit LearningProfileGroup-Objekten.
        """

        result = []

        cursor = self._cnx.cursor()
        command = "SELECT * FROM learning_profile_group"
        cursor.execute(command)
        tuples = cursor.fetchall()

        result = self.build_bo(tuples)

        self._cnx.commit()
        cursor.close()

        return result


    def find_by_id(self, id):
        """Suchen einer LearningProfileGroup mit vorgegebener ID. Da diese eindeutig ist,
        wird genau ein Objekt zurückgegeben.

        :param id Primärschlüsselattribut (->DB)
        :return LearningProfileGroup-Objekt, das dem übergebenen Schlüssel entspricht, None bei
                nicht vorhandenem DB-Tupel.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, group_id, name, prev_knowledge, extroversion, study_state, frequency," \
                  "learntyp, semester, interest, degree_course, creation_date FROM learning_profile_group " \
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


    def find_by_group_id(self, group_id):
        """Suchen einer LearningProfileGroup mit vorgegebener group_id. Da diese eindeutig ist,
        wird genau ein Objekt zurückgegeben.

        :param group_id 
        :return LearningProfileGroup-Objekt, das dem übergebenen Schlüssel entspricht, None bei
                nicht vorhandenem DB-Tupel.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, group_id, name, prev_knowledge, extroversion, study_state, frequency," \
                  "learntyp, semester, interest, degree_course, creation_date FROM learning_profile_group " \
                  "WHERE group_id LIKE '{}' ".format(group_id)
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
        """Auslesen aller LearningProfileGroups anhand des GroupNames.

        :param name 
        :return Eine Sammlung mit LearningProfileGroup-Objekten, die sämtliche LearningProfileGroups
            mit dem gewünschten Namen enthält.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, group_id, name, prev_knowledge, extroversion, study_state, frequency," \
                  "learntyp, semester, interest, degree_course, creation_date FROM learning_profile_group " \
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


    def insert(self, learning_profile_group):
        """Einfügen eines LearningProfileGroup-Objekts in die Datenbank.

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf.
        berichtigt.

        :param learning_profile_group das zu speichernde Objekt
        :return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM learning_profile_group ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            learning_profile_group.set_id(maxid[0] + 1)

        command = "INSERT INTO learning_profile_group (id, group_id, name, prev_knowledge, extroversion, study_state, " \
                  "frequency, " \
                  "learntyp, semester, interest, degree_course, creation_date) VALUES" \
                  " (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        data = (learning_profile_group.get_id(),
                learning_profile_group.get_group_id(),
                learning_profile_group.get_name(),
                learning_profile_group.get_prev_knowledge(),
                learning_profile_group.get_extroversion(),
                learning_profile_group.get_study_state(),
                learning_profile_group.get_frequency(),
                learning_profile_group.get_learntyp(),
                learning_profile_group.get_semester(),
                learning_profile_group.get_interest(),
                learning_profile_group.get_degree_course(),
                learning_profile_group.get_creation_date()
                )
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return learning_profile_group


    def update(self, learning_profile_group):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.

        :param learning_profile_group ist das Objekt, das in die DB geschrieben werden soll
        """

        cursor = self._cnx.cursor()

        command = "UPDATE learning_profile_group SET  group_id = ('{}'), name = ('{}'), prev_knowledge = ('{}'), extroversion = ('{}')," \
                  " study_state = ('{}'), frequency = ('{}'), learntyp = ('{}'), semester = ('{}')," \
                  " interest = ('{}'), degree_course = ('{}'), creation_date = ('{}') WHERE id = ('{}')" \
            .format(learning_profile_group.get_group_id(),
                    learning_profile_group.get_name(),
                    learning_profile_group.get_prev_knowledge(),
                    learning_profile_group.get_extroversion(),
                    learning_profile_group.get_study_state(),
                    learning_profile_group.get_frequency(),
                    learning_profile_group.get_learntyp(),
                    learning_profile_group.get_semester(),
                    learning_profile_group.get_interest(),
                    learning_profile_group.get_degree_course(),
                    learning_profile_group.get_creation_date(),
                    learning_profile_group.get_id())

        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


    def delete(self, learning_profile_group):
        """Löschen der Daten eines LearningProfileGroup-Objekts aus der Datenbank.

        :param learning_profile_group ist das aus der DB zu löschende "Objekt"
        """

        cursor = self._cnx.cursor()
        command = "DELETE FROM learning_profile_group WHERE id = ('{}')".format(learning_profile_group.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


# Zum Testen auzführen
if (__name__ == "__main__"):
    with LearningProfileGroupMapper() as mapper:
        learning_profile = LearningProfileGroup()
        learning_profile.set_name("Informatik")
        learning_profile.set_group_id(1)
        learning_profile.set_prev_knowledge("Garkeine")
        learning_profile.set_extroversion(2)
        learning_profile.set_study_state(3)
        learning_profile.set_frequency(4)
        learning_profile.set_learntyp(5)
        learning_profile.set_semester(6)
        learning_profile.set_degree_course("Wirtschaftsinformatik")

        mapper.insert(learning_profile)
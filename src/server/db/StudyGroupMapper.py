from src.server.db.Mapper import Mapper
from src.server.bo.StudyGroup import StudyGroup


class StudyGroupMapper(Mapper):
    """Mapper-Klasse, die StudyGroup-Objekte auf eine relationale
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

            for (id, name, creation_date, chat_id) in tuples:
                studygroup = StudyGroup()
                studygroup.set_id(id)
                studygroup.set_name(name)
                studygroup.set_creation_date(creation_date)
                studygroup.set_chat_id(chat_id)
                result = studygroup

        else:
            "Baue mehrere"

            for (id, name, creation_date, chat_id,) in tuples:
                studygroup = StudyGroup()
                studygroup.set_id(id)
                studygroup.set_name(name)
                studygroup.set_creation_date(creation_date)
                studygroup.set_chat_id(chat_id)
                result.append(studygroup)

        return result


    def find_all(self):
        """Auslesen aller StudyGroups in unserem System.

        :return Eine Sammlung mit ChatInvitation-Objekten.
        """

        result = []

        cursor = self._cnx.cursor()
        command = "SELECT * FROM studygroup"
        cursor.execute(command)
        tuples = cursor.fetchall()

        result = self.build_bo(tuples)

        self._cnx.commit()
        cursor.close()

        return result


    def find_by_id(self, id):
        """Suchen einer StudyGroup mit vorgegebener ID. Da diese eindeutig ist,
        wird genau ein Objekt zurückgegeben.

        :param id Primärschlüsselattribut (->DB)
        :return StudyGroup-Objekt, das dem übergebenen Schlüssel entspricht, None bei
                nicht vorhandenem DB-Tupel.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, creation_date, chat_id FROM studygroup " \
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


    def find_by_chat_id(self, chat_id):
        """Suchen einer StudyGroup mit vorgegebener chat_id. Da diese eindeutig ist,
        wird genau ein Objekt zurückgegeben.

        :param chat_id 
        :return StudyGroup-Objekt, das dem übergebenen Schlüssel entspricht, None bei
                nicht vorhandenem DB-Tupel.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, creation_date, chat_id FROM studygroup " \
                  "WHERE chat_id LIKE '{}' ".format(chat_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Falls keine StudyGroup mit der angegebenen id gefunden werden konnte,
                wird hier None als Rückgabewert deklariert"""

            result = None

        self._cnx.commit()
        cursor.close()

        return result


    def find_by_group_name(self, name):
        """Auslesen aller StudyGroups anhand des names.

        :param name 
        :return Eine Sammlung mit StudyGroup-Objekten, die sämtliche Groups
            mit dem gewünschten Namen enthält.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, creation_date, chat_id FROM studygroup " \
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


    def insert(self, studygroup):
        """Einfügen eines StudyGroup-Objekts in die Datenbank.

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf.
        berichtigt.

        :param studygroup das zu speichernde Objekt
        :return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as maxid from studygroup")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die ChatInvitation-Tabelle leer ist und wir mit der ID 1 beginnen können."""

                studygroup.set_id(1)

            else:
                """Wenn wir eine maximale ID festellen konnten, zählen wir diese
                um 1 hoch und weisen diesen Wert als ID dem ChatInvitation-Objekt zu."""

                studygroup.set_id(maxid[0] + 1)

        command = "INSERT INTO studygroup (id, name, creation_date, chat_id) VALUES " \
                  "('{}','{}','{}','{}')"\
                .format(studygroup.get_id(),
                        studygroup.get_name(),
                        studygroup.get_creation_date(),
                        studygroup.get_chat_id()
                        )
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

        return studygroup


    def update(self, studygroup):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.

        :param studygroup das Objekt, das in die DB geschrieben werden soll
        """

        cursor = self._cnx.cursor()
        command = "UPDATE studygroup SET name = ('{}'), creation_date = ('{}'), chat_id = ('{}')" \
                  "WHERE id = ('{}')" \
            .format(studygroup.get_name(),
                    studygroup.get_creation_date(),
                    studygroup.get_chat_id(),
                    studygroup.get_id()
                    )

        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


    def delete(self, studygroup):
        """Löschen der Daten eines ChatInvitation-Objekts aus der Datenbank.

        :param studygroup das aus der DB zu löschende "Objekt"
        """

        cursor = self._cnx.cursor()
        command = "DELETE FROM studygroup WHERE id = ('{}')".format(studygroup.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


# Zum Testen ausführen
if (__name__ == "__main__"):
    with StudyGroupMapper() as mapper:
        studygroup = StudyGroup()
        studygroup.set_name("Studifix1")
        studygroup.set_chat_id(1)

        mapper.insert(studygroup)
        mapper.find_by_group_name("Studifix1")
        print(mapper)
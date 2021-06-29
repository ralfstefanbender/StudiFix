from src.server.db.Mapper import Mapper
from src.server.bo.ChatMessage import ChatMessage


class ChatMessageMapper(Mapper):
    """Mapper-Klasse, die ChatMessage-Objekte auf eine relationale
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

            for (id, text, creation_date, chat_id, user_id) in tuples:
                chat_message = ChatMessage()
                chat_message.set_id(id)
                chat_message.set_text(text)
                chat_message.set_chat_id(chat_id)
                chat_message.set_user_id(user_id)
                result = chat_message

        else:
            "Baue mehrere"

            for (id, text, creation_date, chat_id, user_id) in tuples:
                chat_message = ChatMessage()
                chat_message.set_id(id)
                chat_message.set_text(text)
                chat_message.set_chat_id(chat_id)
                chat_message.set_user_id(user_id)
                result.append(chat_message)

        return result


    def find_all(self):
        """Auslesen aller ChatMessages in unserem System.

        :return Eine Sammlung mit ChatMessage-Objekten.
        """

        result = []

        cursor = self._cnx.cursor()
        command = "SELECT * FROM chat_message"
        cursor.execute(command)
        tuples = cursor.fetchall()

        result = self.build_bo(tuples)

        self._cnx.commit()
        cursor.close()

        return result


    def find_by_id(self, id):
        """Suchen einer Message mit vorgegebener ID. Da diese eindeutig ist,
        wird genau ein Objekt zurückgegeben.

        :param id Primärschlüsselattribut (->DB)
        :return ChatMessage-Objekt, das dem übergebenen Schlüssel entspricht, None bei
                nicht vorhandenem DB-Tupel.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, text, creation_date, chat_id, user_id FROM chat_message " \
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


    def find_all_by_chat_id(self, chat_id):
        """Auslesen aller Messages mit vorgegebener chat_id.

        :param chat_id der gesuchten Messages.
        :return ChatMessage-Objekt, das die übergebene chat_id besitzt,
            None bei nicht vorhandenem DB-Tupel.
        """

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, text, creation_date, chat_id, user_id FROM chat_message " \
                  "WHERE chat_id LIKE '{}' ".format(chat_id)
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


    def insert(self, chat_message):
        """Einfügen eines ChatMessage-Objekts in die Datenbank.

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf.
        berichtigt.

        :param chat_message das zu speichernde Objekt
        :return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as maxid from chat_message")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""

                chat_message.set_id(1)

            else:
                """Wenn wir eine maximale ID festellen konnten, zählen wir diese
                um 1 hoch und weisen diesen Wert als ID dem Participation-Objekt zu."""

                chat_message.set_id(maxid[0] + 1)

        command = "INSERT INTO chat_message (id, text, creation_date, chat_id, user_id) VALUES " \
                  "('{}','{}','{}','{}','{}')".format(
                      chat_message.get_id(),
                      chat_message.get_text(),
                      chat_message.get_creation_date(),
                      chat_message.get_chat_id(),
                      chat_message.get_user_id()
                      )
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

        return chat_message


    def update(self, chat_message):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.

        :param chat_message ist das Objekt, das in die DB geschrieben werden soll
        """

        cursor = self._cnx.cursor()
        command = "UPDATE chat_message SET text = ('{}'), creation_date = ('{}'), chat_id = ('{}')," \
                  " user_id = ('{}') WHERE id = ('{}')".format(
                      chat_message.get_text(),
                      chat_message.get_creation_date(),
                      chat_message.get_chat_id(),
                      chat_message.get_user_id(),
                      chat_message.get_id()
                      )
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


    def delete(self, chat_message):
        """Löschen der Daten eines ChatMessage-Objekts aus der Datenbank.

        :param chat_message ist das aus der DB zu löschende "Objekt"
        """

        cursor = self._cnx.cursor()
        try:
            command = "DELETE FROM chat_message WHERE id = ('{}')".format(chat_message.get_id())
            cursor.execute(command)

            self._cnx.commit()
            cursor.close()
        except:
            pass


# Zum Testen ausführen
if (__name__ == "__main__"):
    with ChatMessageMapper() as mapper:
        chat_message = ChatMessage()
        chat_message.set_text("")
        chat_message.set_chat_id(1)
        chat_message.set_user_id(1)

        mapper.insert(chat_message)

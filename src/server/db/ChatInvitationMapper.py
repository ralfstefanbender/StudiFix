from src.server.db.Mapper import Mapper
from src.server.bo.ChatInvitation import ChatInvitation


class ChatInvitationMapper(Mapper):
    """Mapper-Klasse, die ChatInvitation-Objekte auf eine relationale
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

            for (id, creation_date, is_accepted, chat_id, target_user, source_user) in tuples:
                chat_invitation = ChatInvitation()
                chat_invitation.set_id(id)
                chat_invitation.set_creation_date(creation_date)
                chat_invitation.set_is_accepted(is_accepted)
                chat_invitation.set_chat_id(chat_id)
                chat_invitation.set_target_user(target_user)
                chat_invitation.set_source_user(source_user)
                result = chat_invitation
                
        else:
            "Baue mehrere"

            for (id, creation_date, is_accepted, chat_id, target_user, source_user) in tuples:
                chat_invitation = ChatInvitation()
                chat_invitation.set_id(id)
                chat_invitation.set_creation_date(creation_date)
                chat_invitation.set_is_accepted(is_accepted)
                chat_invitation.set_chat_id(chat_id)
                chat_invitation.set_target_user(target_user)
                chat_invitation.set_source_user(source_user)
                result.append(chat_invitation)

        return result


    def set_source_user_one(self, chat_invitation):
        """Source_User wird geupdatet"""

        cursor = self._cnx.cursor()
        command = "UPDATE chat_invitation SET source_user = 1 WHERE id LIKE ('{}')".format(chat_invitation.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


    def find_all(self):
        """Auslesen aller ChatInvitations in unserem System.

        :return Eine Sammlung mit ChatInvitation-Objekten.
        """

        cursor = self._cnx.cursor()
        command = "SELECT * FROM chat_invitation"
        cursor.execute(command)
        tuples = cursor.fetchall()
        result = self.build_bo(tuples)

        self._cnx.commit()
        cursor.close()

        return result


    def find_by_id(self, id):
        """Suchen einer ChatInvitation mit vorgegebener ID. Da diese eindeutig ist,
        wird genau ein Objekt zurückgegeben.

        :param id Primärschlüsselattribut (->DB)
        :return ChatInvitation-Objekt, das dem übergebenen Schlüssel entspricht, None bei
                nicht vorhandenem DB-Tupel.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation WHERE id LIKE '{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()
        print(tuples)

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            
            result = None

        self._cnx.commit()
        cursor.close()

        return result


    def find_all_invites_by_target_user(self, target_user):
        """Auslesen aller ChatInvitations mit vorgegebenem target_user.

        :param target_user
        :return ChatInvitation-Objekt, das den übergebenen target_user besitzt,
            None bei nicht vorhandenem DB-Tupel.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation WHERE target_user LIKE '{}'".format(target_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""

            result = None

        return result


    def find_all_invites_by_source_user(self, source_user):
        """Auslesen aller ChatInvitations mit vorgegebenem source_user.

        :param source_user
        :return ChatInvitation-Objekt, das den übergebenen source_user besitzt,
            None bei nicht vorhandenem DB-Tupel.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation WHERE source_user LIKE '{}'".format(source_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""

            result = None

        return result


    def find_all_accepted_user_in_chat(self, chat_id):
        """Alle User eines Chats auslesen, gibt nur die ID zurück

         :return Eine Sammlung mit ChatInvitation-Objekten, die sämtliche User des
                betreffenden Chats repräsentieren.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation WHERE chat_id LIKE '{}' AND is_accepted = 1".format(chat_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""

            result = None

        return result


    def find_all_pend_invites(self):
        """Auslesen aller noch nicht akzeptierten ChatInvites.

        :return Eine Sammlung mit ChatInvitation-Objekten.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation WHERE is_accepted = 0 "
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""

            result = None

        return result


    def find_pend_invites_by_target_user(self, target_user):
        """Nicht angenommene ChatInvites mit entsprechendem target_user finden

        :return Eine Sammlung mit ChatInvitation-Objekten, die sämtliche nicht angenommene ChatInvites des
                betreffenden target_user repräsentieren.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation WHERE target_user LIKE '{}' AND is_accepted = 0".format(target_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""

            result = None

        return result


    def find_pend_invites_by_source_user(self, source_user):
        """Nicht angenommene ChatInvites mit entsprechendem source_user finden

        :return Eine Sammlung mit ChatInvitation-Objekten, die sämtliche nicht angenommene ChatInvites des
                betreffenden source_user repräsentieren.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation WHERE source_user LIKE '{}' AND is_accepted = 0".format(source_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""

            result = None

        return result


    def find_accepted_invites_by_source_user(self, source_user):
        """Angenommene ChatInvites mit entsprechendem source_user auslesen

        :return Eine Sammlung mit ChatInvitation-Objekten, die sämtliche angenommene ChatInvites des
                betreffenden source_user repräsentieren.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation WHERE source_user LIKE '{}' AND is_accepted = 1 ".format(source_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""

            result = None

        return result


    def find_accepted_invites_by_target_user(self, target_user):
        """Angenommene ChatInvites mit entsprechendem target_user auslesen

        :return Eine Sammlung mit ChatInvitation-Objekten, die sämtliche angenommene ChatInvites des
                betreffenden target_user repräsentieren.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation WHERE target_user LIKE '{}' AND is_accepted = 1".format(target_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""

            result = None

        return result


    def insert(self, chatinvitation):
        """Einfügen eines ChatInvitation-Objekts in die Datenbank.

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf.
        berichtigt.

        :param chatinvitation das zu speichernde Objekt
        :return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM chat_invitation ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                """Wenn wir eine maximale ID festellen konnten, zählen wir diese
                um 1 hoch und weisen diesen Wert als ID dem ChatInvitation-Objekt zu."""

                chatinvitation.set_id(maxid[0] + 1)

            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die ChatInvitation-Tabelle leer ist und wir mit der ID 1 beginnen können."""

                chatinvitation.set_id(1)

            command = "INSERT INTO chat_invitation (id, creation_date, is_accepted, chat_id, target_user, source_user) VALUES (%s,%s,%s,%s,%s,%s)"
            data = (chatinvitation.get_id(),
                    chatinvitation.get_creation_date(),
                    chatinvitation.get_is_accepted(),
                    chatinvitation.get_chat_id(),
                    chatinvitation.get_target_user(),
                    chatinvitation.get_source_user())

            cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return chatinvitation


    def update(self, chat_invitation):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.

        :param chat_invitation das Objekt, das in die DB geschrieben werden soll
        """

        cursor = self._cnx.cursor()
        command = "UPDATE chat_invitation SET creation_date = ('{}'), is_accepted = ('{}'), chat_id = ('{}'), " \
                  "target_user = ('{}'), source_user = ('{}') WHERE id = ('{}')".format(
                      chat_invitation.get_creation_date(),
                      chat_invitation.get_is_accepted(),
                      chat_invitation.get_chat_id(),
                      chat_invitation.get_target_user(),
                      chat_invitation.get_source_user(),
                      chat_invitation.get_id()
                      )

        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


    def delete(self, chatinvitation):
        """Löschen der Daten eines ChatInvitation-Objekts aus der Datenbank.

        :param chatinvitation das aus der DB zu löschende "Objekt"
        """

        cursor = self._cnx.cursor()
        command = "DELETE FROM chat_invitation WHERE id = ('{}')".format(chatinvitation.get_id())
        cursor.execute(command)
        self._cnx.commit()


# Zum Testen ausführen
if (__name__ == "__main__"):
    with ChatInvitationMapper() as mapper:

        invi = ChatInvitation()
        invi.set_id(1)
        invi.set_is_accepted(0)
        invi.set_chat_id(1)
        invi.set_source_user(1)
        invi.set_target_user(3)
        mapper.insert(invi)
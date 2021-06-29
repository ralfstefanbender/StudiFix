from src.server.db.Mapper import Mapper
from src.server.bo.GroupInvitation import GroupInvitation


class GroupInvitationMapper(Mapper):
    """Mapper-Klasse, die GroupInvitation-Objekte auf eine relationale
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

            for (id, creation_date, is_accepted, study_group_id, target_user, source_user) in tuples:
                groupinvitation = GroupInvitation()
                groupinvitation.set_id(id)
                groupinvitation.set_creation_date(creation_date)
                groupinvitation.set_is_accepted(is_accepted)
                groupinvitation.set_study_group_id(study_group_id)
                groupinvitation.set_target_user(target_user)
                groupinvitation.set_source_user(source_user)
                result = groupinvitation
        else:
            "Baue mehrere"

            for (id, creation_date, accepted, study_group_id, target_user, source_user) in tuples:
                groupinvitation = GroupInvitation()
                groupinvitation.set_id(id)
                groupinvitation.set_creation_date(creation_date)
                groupinvitation.set_is_accepted(accepted)
                groupinvitation.set_study_group_id(study_group_id)
                groupinvitation.set_target_user(target_user)
                groupinvitation.set_source_user(source_user)
                result.append(groupinvitation)

        return result


    def set_source_user_one(self, groupinvitation):
        """source_user wird geupdatet"""

        cursor = self._cnx.cursor()
        command = "UPDATE group_invitation SET source_user = 1 WHERE id LIKE ('{}')".format(groupinvitation.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


    def find_all(self):
        """Auslesen aller GroupInvitations in unserem System.

        :return Eine Sammlung mit GroupInvitation-Objekten.
        """

        cursor = self._cnx.cursor()
        command = "SELECT * FROM group_invitation"
        cursor.execute(command)
        tuples = cursor.fetchall()
        result = self.build_bo(tuples)

        self._cnx.commit()
        cursor.close()

        return result


    def find_by_id(self, id):
        """Suchen einer GroupInvitation mit vorgegebener ID. Da diese eindeutig ist,
        wird genau ein Objekt zurückgegeben.

        :param id Primärschlüsselattribut (->DB)
        :return GroupInvitation-Objekt, das dem übergebenen Schlüssel entspricht, None bei
                nicht vorhandenem DB-Tupel.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation WHERE id LIKE '{}' ".format(id)
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


    def find_all_group_invitations_by_StudyGroup(self, study_group_id):
        """Auslesen aller GroupInvitations eines durch Fremdschlüssel gegebenen StudyGroups.

        :param study_group_id
        :return Eine Sammlung mit GroupInvitation-Objekten.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation WHERE study_group_id LIKE '{}'".format(study_group_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""

            result = None

        return result


    def find_all_group_invitations_by_target_user(self, target_user):
        """Auslesen aller GroupInvitations mit vorgegebenem target_user.

        :param target_user
        :return GroupInvitation-Objekt, das den übergebenen target_user besitzt,
            None bei nicht vorhandenem DB-Tupel.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation WHERE target_user LIKE '{}'".format(target_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""

            result = None

        return result


    def find_all_group_invitations_by_source_user(self, source_user):
        """Auslesen aller GroupInvitations mit vorgegebenem source_user.

        :param source_user
        :return GroupInvitation-Objekt, das den übergebenen source_user besitzt,
            None bei nicht vorhandenem DB-Tupel.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation WHERE source_user LIKE '{}'".format(source_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""

            result = None

        return result


    def find_all_pend_user_in_study_group(self, study_group_id):
        """Alle User einer StudyGroup auslesen die noch nicht akzeptiert haben, gibt nur die ID zurück"""

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation WHERE study_group_id LIKE '{}' AND is_accepted = 0".format(study_group_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        return result

    def find_all_accepted_user_in_study_group(self, study_group_id):
        """Alle User einer StudyGroup auslesen, gibt nur die ID zurück 
        
        :return Eine Sammlung mit GroupInvitation-Objekten, die sämtliche User der
                betreffenden StudyGroup repräsentieren.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation WHERE study_group_id LIKE '{}' AND is_accepted = 1".format(study_group_id)
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
        """Nicht angenommene invites mit entsprechendem target_user finden

        :return Eine Sammlung mit GroupInvitation-Objekten, die sämtliche nicht angenommene GroupInvites des
                betreffenden target_user repräsentieren.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation WHERE target_user LIKE '{}' AND is_accepted = 0".format(target_user)
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
        """Nicht angenommene GroupInvites mit entsprechendem source_user finden

        :return Eine Sammlung mit GroupInvitation-Objekten, die sämtliche nicht angenommene GroupInvites des
                betreffenden source_user repräsentieren.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation WHERE source_user LIKE '{}' AND is_accepted = 0".format(source_user)
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
        """Angenommene GroupInvites mit entsprechendem source_user auslesen

        :return Eine Sammlung mit GroupInvitation-Objekten, die sämtliche angenommene GroupInvites des
                betreffenden source_user repräsentieren.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation WHERE source_user LIKE '{}' AND is_accepted = 1 ".format(source_user)
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
        """Angenommene Invites mit entsprechendem target_user auslesen

        :return Eine Sammlung mit GroupInvitation-Objekten, die sämtliche angenommene GroupInvites des
                betreffenden target_user repräsentieren.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation WHERE target_user LIKE '{}' AND is_accepted = 1".format(target_user)
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
        """Auslesen aller noch nicht akzeptierten Invites.

        :return Eine Sammlung mit GroupInvitation-Objekten.
        """

        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation WHERE is_accepted = 0 "
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf self.build_bo(tuples) auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""

            result = None

        return result


    def insert(self, groupinvitation):
        """Einfügen eines GroupInvitation-Objekts in die Datenbank.

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft und ggf.
        berichtigt.

        :param groupinvitation das zu speichernde Objekt
        :return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM group_invitation ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                """Wenn wir eine maximale ID festellen konnten, zählen wir diese
                um 1 hoch und weisen diesen Wert als ID dem Participation-Objekt zu."""

                groupinvitation.set_id(maxid[0] + 1)

            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""

                groupinvitation.set_id(1)

            command = "INSERT INTO group_invitation (id, creation_date, is_accepted, study_group_id, target_user, source_user) VALUES (%s,%s,%s,%s,%s,%s)"
            data = (groupinvitation.get_id(),
                    groupinvitation.get_creation_date(),
                    groupinvitation.get_is_accepted(),
                    groupinvitation.get_study_group_id(),
                    groupinvitation.get_target_user(),
                    groupinvitation.get_source_user()
                    )
            cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return groupinvitation


    def update(self, group_invitation):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.

        :param group_invitation ist das Objekt, das in die DB geschrieben werden soll
        """

        cursor = self._cnx.cursor()
        command = "UPDATE group_invitation SET creation_date = ('{}'), is_accepted = ('{}'), study_group_id = ('{}'), " \
                  "target_user = ('{}'), source_user = ('{}') WHERE id = ('{}')".format(
                      group_invitation.get_creation_date(),
                      group_invitation.get_is_accepted(),
                      group_invitation.get_study_group_id(),
                      group_invitation.get_target_user(),
                      group_invitation.get_source_user(),
                      group_invitation.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


    def delete(self, group_invitation):
        """Löschen der Daten eines GroupInvitation-Objekts aus der Datenbank.

        :param group_invitation ist das aus der DB zu löschende "Objekt"
        """

        cursor = self._cnx.cursor()
        command = "DELETE FROM group_invitation WHERE id = ('{}')".format(group_invitation.get_id())
        cursor.execute(command)
        self._cnx.commit()


# Zum Testen ausführen
if (__name__ == "__main__"):
    with GroupInvitationMapper() as mapper:
        #Nach mapper jegliche Methode dieser Klasse

        invi = GroupInvitation()
        invi.set_id(1)
        invi.set_is_accepted(0)
        invi.set_source_user(1)
        invi.set_target_user(3)
        invi.set_study_group_id(3)
        mapper.insert(invi)


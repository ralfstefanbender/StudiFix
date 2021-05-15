from src.server.db.Mapper import Mapper
from src.server.bo.ChatInvitation import ChatInvitation


class ChatInvitationMapper(Mapper):

    def __init__(self):
        super().__init__()

    def build_bo(self, tuples):

        result = []

        if len(tuples) == 1:
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
        cursor = self._cnx.cursor()
        command = "UPDATE chat_invitation SET source_user = 1 WHERE id LIKE ('{}')".format(chat_invitation.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def find_all(self):
        cursor = self._cnx.cursor()
        command = "SELECT * FROM chat_invitation"
        cursor.execute(command)
        tuples = cursor.fetchall()
        result = self.build_bo(tuples)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, id):
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM group_invitation WHERE id LIKE '{}' ".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()
        print(tuples)

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Falls kein Chat mit der angegebenen id gefunden werden konnte,
                wird hier None als Rückgabewert deklariert"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_all_invites_by_target_user(self, target_user):
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation " \
                  "WHERE " \
                  "target_user LIKE '{}'".format(target_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)
        except IndexError:
            result = None
        return result

    def find_all_invites_by_source_user(self, source_user):
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation " \
                  "WHERE " \
                  "source_user LIKE '{}'".format(source_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)
        except IndexError:
            result = None
        return result

    def find_all_accepted_user_in_chat(self, chat_id):
        """Alle User eines Chats auslesen, gibt nur die ID zurück """
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation" \
                  " WHERE " \
                  "chat_id LIKE '{}' AND is_accepted = 1".format(chat_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)
        except IndexError:
            result = None
        return result

    def find_all_pend_invites(self):
        """Alle Invites die noch nicht akzeptiert wurden auslesen"""
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation" \
                  " WHERE " \
                  " is_accepted = 0 "
        cursor.execute(command)
        tuples = cursor.fetchall()
        try:
            result = self.build_bo(tuples)
        except IndexError:
            result = None
        return result

    def find_pend_invites_by_target_user(self, target_user):
        """Nicht angenommene invites mit entsprechendem target user finden"""
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation " \
                  "WHERE " \
                  "target_user LIKE '{}' AND is_accepted = 0".format(target_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)
        except IndexError:
            result = None
        return result

    def find_pend_invites_by_source_user(self, source_user):
        """Invite mit dem entsprechenden source user finden"""
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation" \
                  " WHERE " \
                  "source_user LIKE '{}' AND is_accepted = 0".format(source_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)
        except IndexError:
            result = None
        return result

    def find_accepted_invites_by_source_user(self, source_user):
        """Invite mit entsprechendem source_user finden"""
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation" \
                  " WHERE " \
                  "source_user LIKE '{}' AND is_accepted = 1 ".format(source_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)
        except IndexError:
            result = None
        return result

    def find_accepted_invites_by_target_user(self, target_user):
        """Invite mit entsprechendem target user finden"""
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, chat_id, target_user, source_user " \
                  "FROM chat_invitation " \
                  "WHERE " \
                  "target_user LIKE '{}' AND is_accepted = 1".format(target_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)
        except IndexError:
            result = None
        return result

    def insert(self, chat_invitation):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as maxid from chat_invitation")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                chat_invitation.set_id(1)
            else:
                chat_invitation.set_id(maxid[0] + 1)

        command = "INSERT INTO chat_invitation (id, creation_date, is_accepted, chat_id, target_user, source_user) " \
                  "VALUES ('{}','{}','{}','{}', '{}', '{}' )" \
                  .format(chat_invitation.get_id(),
                          chat_invitation.get_creation_date(),
                          chat_invitation.get_is_accepted(),
                          chat_invitation.get_chat_id(),
                          chat_invitation.get_target_user(),
                          chat_invitation.get_source_user())
        cursor.execute(command)
        self._cnx.commit()
        cursor.close()

    def update(self, chat_invitation):
        cursor = self._cnx.cursor()
        command = "UPDATE chat_invitation SET creation_date = ('{}'), is_accepted = ('{}'), chat_id = ('{}'), " \
                  "target_user = ('{}'), source_user = ('{}') WHERE id = ('{}')" \
            .format(chat_invitation.get_id(),
                    chat_invitation.get_creation_date(),
                    chat_invitation.get_is_accepted(),
                    chat_invitation.get_chat_id(),
                    chat_invitation.get_target_user(),
                    chat_invitation.get_source_user())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, chat_invitation):
        cursor = self._cnx.cursor()
        command = "DELETE FROM chat_invitation WHERE id = ('{}')".format(chat_invitation.get_id())
        cursor.execute(command)
        self._cnx.commit()

if (__name__ == "__main__"):
    with ChatInvitationMapper() as mapper:
        #Nach mapper jegliche Methode dieser Klasse

        invi = ChatInvitation()
        invi.set_id(1)
        invi.set_is_accepted(0)
        invi.set_chat_id(1)
        invi.set_source_user(1)
        invi.set_target_user(3)
        mapper.insert(invi)
from src.server.db.Mapper import Mapper
from src.server.bo.GroupInvitation import GroupInvitation


class GroupInvitationMapper(Mapper):

    def __init__(self):
        super().__init__()

    def build_bo(self, tuples):
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
        cursor = self._cnx.cursor()
        command = "UPDATE group_invitation SET source_user = 1 WHERE id LIKE ('{}')".format(groupinvitation.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def find_all(self):
        cursor = self._cnx.cursor()
        command = "SELECT * FROM group_invitation"
        cursor.execute(command)
        tuples = cursor.fetchall()
        result = self.build_bo(tuples)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, id):
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation WHERE id LIKE '{}' ".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()
        print(tuples)

        try:
            result = self.build_bo(tuples)

        except IndexError:
            """Falls keine StudyGroup mit der angegebenen id gefunden werden konnte,
                wird hier None als Rückgabewert deklariert"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_all_group_invitations_by_StudyGroup(self, study_group_id):
        """Alle Invitations auslesen, bei denen der FK = study_group_id ist """
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation" \
                  " WHERE " \
                  "study_group_id LIKE '{}'".format(study_group_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)
        except IndexError:
            result = None
        return result

    def find_all_group_invitations_by_target_user(self, target_user):
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation " \
                  "WHERE " \
                  "target_user LIKE '{}'".format(target_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)
        except IndexError:
            result = None
        return result

    def find_all_group_invitations_by_source_user(self, source_user):
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation " \
                  "WHERE " \
                  "source_user LIKE '{}'".format(source_user)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)
        except IndexError:
            result = None
        return result

    def find_all_pend_user_in_study_group(self, study_group_id):
        """Alle User einer StudyGroup auslesen, gibt nur die ID zurück """
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation " \
                  "WHERE " \
                  "study_group_id LIKE '{}' AND is_accepted = 0".format(study_group_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            result = self.build_bo(tuples)
        except IndexError:
            result = None
        return result

    def find_all_accepted_user_in_study_group(self, study_group_id):
        """Alle User einer party auslesen, gibt nur die ID zurück """
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation" \
                  " WHERE " \
                  "study_group_id LIKE '{}' AND is_accepted = 1".format(study_group_id)
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
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation " \
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
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation" \
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
        """Invite mit entsprechendem source user finden"""
        cursor = self._cnx.cursor()
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation" \
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
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation " \
                  "WHERE " \
                  "target_user LIKE '{}' AND is_accepted = 1".format(target_user)
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
        command = "SELECT id, creation_date, is_accepted, study_group_id, target_user, source_user " \
                  "FROM group_invitation" \
                  " WHERE " \
                  " is_accepted = 0 "
        cursor.execute(command)
        tuples = cursor.fetchall()
        try:
            result = self.build_bo(tuples)
        except IndexError:
            result = None
        return result

    def insert(self, group_invitation):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as maxid from group_invitation")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                group_invitation.set_id(1)
            else:
                group_invitation.set_id(maxid[0] + 1)

        command = "INSERT INTO group_invitation (id, creation_date, is_accepted, study_group_id, target_user, source_user) " \
                  "VALUES ('{}','{}','{}','{}', '{}', '{}' )" \
                  .format(group_invitation.get_id(),
                          group_invitation.get_creation_date(),
                          group_invitation.get_is_accepted(),
                          group_invitation.get_study_group_id(),
                          group_invitation.get_target_user(),
                          group_invitation.get_source_user())
        cursor.execute(command)
        self._cnx.commit()
        cursor.close()



    def update(self, group_invitation):
        cursor = self._cnx.cursor()
        command = "UPDATE group_invitation SET creation_date = ('{}'), is_accepted = ('{}'), study_group_id = ('{}'), " \
                  "target_user = ('{}'), source_user = ('{}') WHERE id = ('{}')" \
            .format(group_invitation.get_creation_date(), group_invitation.get_is_accepted(),
                    group_invitation.get_study_group_id(),
                    group_invitation.get_target_user(), group_invitation.get_source_user(), group_invitation.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, group_invitation):
        cursor = self._cnx.cursor()
        command = "DELETE FROM group_invitation WHERE id = ('{}')".format(group_invitation.get_id())
        cursor.execute(command)
        self._cnx.commit()

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


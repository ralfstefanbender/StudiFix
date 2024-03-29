from .bo.User import User
from .bo.Chat import Chat
from .bo.ChatInvitation import ChatInvitation
from .bo.ChatMessage import ChatMessage
from .bo.LearningprofileGroup import LearningProfileGroup
from .bo.LearningProfileUser import LearningProfileUser
from .bo.StudyGroup import StudyGroup
from .bo.GroupInvitation import GroupInvitation

from .db.UserMapper import *
from .db.ChatMapper import *
from .db.ChatInvitationMapper import *
from .db.ChatMessageMapper import *
from .db.LearningProfileGroupMapper import *
from .db.LearningProfileUserMapper import *
from .db.StudyGroupMapper import *
from .db.GroupInvitationMapper import *



class Administration(object):
    
    """Diese Klasse aggregiert nahezu sämtliche Applikationslogik (engl. Business Logic).
    Sie ist wie eine Spinne, die sämtliche Zusammenhänge in ihrem Netz (in unserem
    Fall die Daten der Applikation) überblickt und für einen geordneten Ablauf und
    dauerhafte Konsistenz der Daten und Abläufe sorgt.

    Die Applikationslogik findet sich in den Methoden dieser Klasse. Jede dieser
    Methoden kann als *Transaction Script* bezeichnet werden. Dieser Name
    lässt schon vermuten, dass hier analog zu Datenbanktransaktion pro
    Transaktion gleiche mehrere Teilaktionen durchgeführt werden, die das System
    von einem konsistenten Zustand in einen anderen, auch wieder konsistenten
    Zustand überführen. Wenn dies zwischenzeitig scheitern sollte, dann ist das
    jeweilige Transaction Script dafür verwantwortlich, eine Fehlerbehandlung
    durchzuführen.
    Diese Klasse steht mit einer Reihe weiterer Datentypen in Verbindung. Diese
    sind:
    - die Klassen BusinessObject und deren Subklassen,
    - die Mapper-Klassen für den DB-Zugriff."""

    def __init__(self):
        pass


    # User Methoden

    def create_user(self, google_id, first_name, last_name, email, adress):
        """Einen User anlegen"""

        user = User()  # Name von NamedBusinessObject
        user.set_google_id(google_id)
        user.set_firstname(first_name)
        user.set_lastname(last_name)
        user.set_email(email)
        user.set_adress(adress)
        user.set_id(1)

        with UserMapper() as mapper:
            mapper.insert(user)

        user_id = self.get_user_by_google_id(google_id)
        self.create_learningprofile_user(user_id.get_id(), "profile", 1, 1, 1, 1, 1, 1, "interest preset", "degreecourse preset")

    def get_user_by_name(self, name):
        """Alle User mit Namen name auslesen."""

        with UserMapper() as mapper:
            return mapper.find_by_name(name)

    def get_user_by_id(self, number):
        """Den User mit der gegebenen ID auslesen."""

        with UserMapper() as mapper:
            return mapper.find_by_id(number)

    def get_user_by_email(self, email):
        """Alle User mit gegebener E-Mail-Adresse auslesen."""

        with UserMapper() as mapper:
            return mapper.find_user_by_email(email)

    def get_user_by_google_id(self, id):
        """Den User mit der gegebenen Google ID auslesen."""

        with UserMapper() as mapper:
            return mapper.find_user_by_google_id(id)

    def get_user_by_firstname(self, first_name):
        """Den User mit der gegebenen FirstName auslesen"""

        with UserMapper() as mapper:
            return mapper.find_user_by_firstname(first_name)

    def get_user_by_lastname(self, last_name):
        """Den User mit der gegebenen LastName auslesen"""

        with UserMapper() as mapper:
            return mapper.find_user_by_lastname(last_name)

    def get_all_users(self):
        """Alle User auslesen."""

        with UserMapper() as mapper:
            return mapper.find_all()

    def get_user_by_learning_profile_id(self,learning_profile_id):
        """Den User mit der gegebenen LearningProfileID auslesen"""

        with UserMapper() as mapper:
            return mapper.find_user_by_learning_profile_id(learning_profile_id)

    def save_user(self, user):
        """Den gegebenen User speichern."""

        with UserMapper() as mapper:
            mapper.update(user)

    def delete_user(self, user):
        """Den gegebenen User aus unserem System löschen."""

        with UserMapper() as mapper:
            mapper.delete(user)


    # LearningProfile Group Methoden

    def create_learningprofile_group(self, group_id, name, frequency, study_state, extroversion, prev_knowledge,
                                     learntyp, semester, interest, degree_course):
        """LearningProfileGruppe wird erstellt"""

        learningprofilegroup = LearningProfileGroup()
        learningprofilegroup.set_group_id(group_id)
        learningprofilegroup.set_name(name)
        learningprofilegroup.set_frequency(frequency)
        learningprofilegroup.set_study_state(study_state)
        learningprofilegroup.set_extroversion(extroversion)
        learningprofilegroup.set_prev_knowledge(prev_knowledge)
        learningprofilegroup.set_learntyp(learntyp)
        learningprofilegroup.set_semester(semester)
        learningprofilegroup.set_interest(interest)
        learningprofilegroup.set_degree_course(degree_course)
        learningprofilegroup.set_id(1)

        with LearningProfileGroupMapper() as mapper:
            return mapper.insert(learningprofilegroup)

    def get_learningprofile_group_by_name(self, name):
        """Die LearningProfileGroup mit gegebenem Namen Auslesen"""
        with LearningProfileGroupMapper() as mapper:
            return mapper.find_by_name(name)

    def get_learningprofile_group_by_id(self, number):
        """Die LearningProfileGroup mit gegebener ID Auslesen"""

        with LearningProfileGroupMapper() as mapper:
            return mapper.find_by_id(number)

    def get_learningprofile_group_by_group_id(self, group_id):
        """Den LearningProfileGroup mit gegebener GroupID Auslesen"""

        with LearningProfileGroupMapper() as mapper:
            return mapper.find_by_group_id(group_id)

    def get_all_learningprofiles_group(self):
        """Alle LearningProfileGroup auslesen."""

        with LearningProfileGroupMapper() as mapper:
            return mapper.find_all()

    def save_learningprofile_group(self, learningprofile):
        """Die gegebene LearningProfileGroup speichern."""

        with LearningProfileGroupMapper() as mapper:
            mapper.update(learningprofile)

    def delete_learningprofile_group(self, learningprofile):
        """Die gegebene LearningProfileGroup aus unserem System löschen."""

        with LearningProfileGroupMapper() as mapper:
            mapper.delete(learningprofile)


    # LearningProfile User Methoden

    def create_learningprofile_user(self, user_id, name, frequency, study_state, extroversion, prev_knowledge,
                                         learntyp, semester, interest, degree_course):
        """LearningProfileUser wird erstellt"""

        learningprofileuser = LearningProfileUser()
        learningprofileuser.set_user_id(user_id)
        learningprofileuser.set_name(name)
        learningprofileuser.set_frequency(frequency)
        learningprofileuser.set_study_state(study_state)
        learningprofileuser.set_extroversion(extroversion)
        learningprofileuser.set_prev_knowledge(prev_knowledge)
        learningprofileuser.set_learntyp(learntyp)
        learningprofileuser.set_semester(semester)
        learningprofileuser.set_interest(interest)
        learningprofileuser.set_degree_course(degree_course)
        learningprofileuser.set_id(1)

        with LearningProfileUserMapper() as mapper:
            return mapper.insert(learningprofileuser)

    def get_learningprofile_user_by_name(self, name):
        """Den LearningProfileUser über den gegebenen Namen Auslesen"""

        with LearningProfileUserMapper() as mapper:
            return mapper.find_by_name(name)

    def get_learningprofile_user_by_id(self, number):
        """Die LearningProfileUser mit gegebener ID Auslesen"""

        with LearningProfileUserMapper() as mapper:
            return mapper.find_by_id(number)

    def get_learningprofile_user_by_user_id(self, user_id):
        """Die LearningProfileUser mit gegebener ID Auslesen"""

        with LearningProfileUserMapper() as mapper:
            return mapper.find_by_user_id(user_id)

    def get_all_learningprofiles_user(self):
        """Alle LearningProfileUser auslesen."""

        with LearningProfileUserMapper() as mapper:
            return mapper.find_all()

    def save_learningprofile_user(self, learningprofile):
        """Den gegebenen LearningProfileUser speichern."""

        with LearningProfileUserMapper() as mapper:
            mapper.update(learningprofile)

    def get_user_id_by_learningprofile_id(self, id):
        """Die UserID über die gegebene ID Auslesen"""

        with LearningProfileUserMapper() as mapper:
            return mapper.get_user_id_by_learningprofile_id(id)


    def delete_learningprofile_user(self, learningprofile):
        """Den gegebenen LearningProfileUser aus unserem System löschen."""

        with LearningProfileUserMapper() as mapper:
            mapper.delete(learningprofile)


    # ChatInvitation Methoden

    def create_chatinvitation(self, source_user, target_user, chat_id, is_accepted):
        """ChatInvitation wird erstellt"""

        chatinvitation = ChatInvitation()
        chatinvitation.set_source_user(source_user)
        chatinvitation.set_target_user(target_user)
        chatinvitation.set_chat_id(chat_id)
        chatinvitation.set_is_accepted(is_accepted)
        chatinvitation.set_id(1)

        with ChatInvitationMapper() as mapper:
            return mapper.insert(chatinvitation)

    def get_chatinvitation_by_id(self, number):
        """Die ChatInvitation mit gegebener ID Auslesen"""

        with ChatInvitationMapper() as mapper:
            return mapper.find_by_id(number)

    def get_all_invites_by_target_user(self, target_user):
        """Alle ChatInvitations über einen gegebenen TargetUser Auslesen"""

        with ChatInvitationMapper() as mapper:
            return mapper.find_all_invites_by_target_user(target_user)

    def get_all_invites_by_source_user(self, source_user):
        """Alle ChatInvitations über einen gegebenen SourceUser Auslesen"""

        with ChatInvitationMapper() as mapper:
            return mapper.find_all_invites_by_source_user(source_user)

    def get_all_accepted_user_in_chat(self, chat_id):
        """Alle User eines Chats über die gegebene ChatID Auslesen"""

        with ChatInvitationMapper() as mapper:
            return mapper.find_all_accepted_user_in_chat(chat_id)

    def get_all_pend_invites(self):
        """Auslesen aller nicht akzeptierten oder gelöschten ChatInvitations"""

        with ChatInvitationMapper() as mapper:
            return mapper.find_all_pend_invites()

    def get_pend_invites_by_target_user(self, target_user):
        """Auslesen aller nicht akzeptierten oder gelöschten ChatInvitations des TargetUsers"""

        with ChatInvitationMapper() as mapper:
            return mapper.find_pend_invites_by_target_user(target_user)

    def get_pend_invites_by_source_user(self, source_user):
        """Auslesen aller nicht akzeptierten oder gelöschten ChatInvitations des SourceUsers"""

        with ChatInvitationMapper() as mapper:
            return mapper.find_pend_invites_by_source_user(source_user)

    def get_accepted_invites_by_source_user(self, source_user):
        """Auslesen aller akzeptierten ChatInvitations des gegebenen SourceUsers"""

        with ChatInvitationMapper() as mapper:
            return mapper.find_accepted_invites_by_source_user(source_user)

    def get_accepted_invites_by_target_user(self, target_user):
        """Auslesen aller akzeptierten ChatInvitations des gegebenen TargetUsers"""

        with ChatInvitationMapper() as mapper:
            return mapper.find_accepted_invites_by_target_user(target_user)

    def get_friend_requests_by_google_id(self, google_id):
        """Freundschaftsanfragen über die gegebene GoogleID Auslesen"""

        user = self.get_user_by_google_id(google_id)
        user_id = user.get_id()
        request_ids = []

        friend_requests = self.get_pend_invites_by_target_user(user_id)

        if type(friend_requests) != list:
            request_ids.append(friend_requests.get_source_user())
        else:
            for obj in friend_requests:
                request_ids.append(obj.get_source_user())

        friend_request_objects = []
        for num in request_ids:
            friend_request_objects.append(self.get_user_by_id(num))

        return friend_request_objects

    def get_friends_by_google_id(self, google_id):
        """Freunde über die gegebene GoogleID Auslesen"""

        user = self.get_user_by_google_id(google_id)
        user_id = user.get_id()
        friends_ids = []

        # Wo SourceUser

        friends_by_target = self.get_accepted_invites_by_target_user(user_id)
        if type(friends_by_target) != list:
            friends_ids.append(friends_by_target.get_source_user())
        else:
            for obj in friends_by_target:
                friends_ids.append(obj.get_source_user())

        # Wo TargetUser

        friends_by_source = self.get_accepted_invites_by_source_user(user_id)
        if type(friends_by_source) != list:
            friends_ids.append(friends_by_source.get_target_user())
        else:
            for obj in friends_by_source:
                friends_ids.append(obj.get_target_user())

        friends_objects = []
        for num in friends_ids:
            friends_objects.append(self.get_user_by_id(num))

        return friends_objects

    def accept_friend_request(self, target_id, source_id):
        """Freundschaftsanfrage akzeptieren und automatisch einen Chat erstellen"""

        friend_request = self.get_pend_invites_by_target_user(target_id)

        if type(friend_request) != list:
            if friend_request.get_source_user() == source_id:
                chat = self.create_chat(self.get_user_by_id(target_id).get_firstname() + " - " + self.get_user_by_id(source_id).get_firstname())
                friend_request.set_is_accepted(1)
                friend_request.set_chat_id(chat.get_id())
                self.save_chatinvitation(friend_request)


        else:
            for obj in friend_request:

                if obj.get_source_user() == source_id:
                    chat = self.create_chat(self.get_user_by_id(target_id).get_firstname() + " - " + self.get_user_by_id(source_id).get_firstname())
                    obj.set_is_accepted(1)
                    obj.set_chat_id(chat.get_id())
                    obj.set_is_accepted(1)
                    self.save_chatinvitation(obj)

    def decline_friend_request(self, target_id, source_id):
        """Freundschaftsanfragen ablehnen"""

        friend_request = self.get_pend_invites_by_target_user(target_id)

        if type(friend_request) != list:
            if friend_request.get_source_user() == source_id:
                self.delete_chatinvitation(friend_request)


        else:
            for obj in friend_request:
                if obj.get_source_user() == source_id:
                    self.delete_chatinvitation(obj)

    def remove_friend(self, target_id, source_id):
        """Freund entfernen und automatisch den dazugehörigen Chat löschen"""

        friends = self.get_accepted_invites_by_target_user(target_id)

        if type(friends) != list:
            friends = [friends]

        for chatinvite in friends:
            if chatinvite.get_source_user() == source_id:
                chat = self.get_chat_by_id(chatinvite.get_chat_id())
                self.delete_chatinvitation(chatinvite)

                msgs = self.get_chatmessages_by_chat_id(chat.get_id())
                if type(msgs) != list:
                    msgs = [msgs]
                for msg in msgs:
                    self.delete_chatmessage(msg)

                self.delete_chat(chat)

        friends = self.get_accepted_invites_by_source_user(target_id)

        if type(friends) != list:
            friends = [friends]

        for chatinvite in friends:
            if chatinvite.get_target_user() == source_id:
                chat = self.get_chat_by_id(chatinvite.get_chat_id())
                self.delete_chatinvitation(chatinvite)

                msgs = self.get_chatmessages_by_chat_id(chat.get_id())
                if type(msgs) != list:
                    msgs = [msgs]
                for msg in msgs:
                    self.delete_chatmessage(msg)

                self.delete_chat(chat)

    def leave_group(self, user_id, group_id):
        """Eine Gruppe verlassen"""

        groups = self.get_accepted_groupinvites_by_target_user(user_id)

        if type(groups) != list:
            groups = [groups]

        for group in groups:
            if group.get_study_group_id() == group_id:
                self.delete_groupinvitation(group)

        groups = self.get_accepted_groupinvites_by_source_user(user_id)

        if type(groups) != list:
            groups = [groups]

        for group in groups:
            if group.get_study_group_id() == group_id:
                self.delete_groupinvitation(group)


    def get_all_chatinvitations(self):
        """Alle ChatInvitations auslesen."""

        with ChatInvitationMapper() as mapper:
            return mapper.find_all()

    def save_chatinvitation(self, invite):
        """Die gegebene ChatInvitation speichern."""

        with ChatInvitationMapper() as mapper:
            mapper.update(invite)

    def delete_chatinvitation(self, id):
        """Die gegebene ChatInvitation aus unserem System löschen."""

        with ChatInvitationMapper() as mapper:
            mapper.delete(id)


    # StudyGroup Methoden

    def create_studygroup (self, name):
        """StudyGroup wird erstellt"""

        studygroup = StudyGroup()
        studygroup.set_name(name)
        chat = self.create_chat(name)
        studygroup.set_chat_id(chat.get_id())
        studygroup.set_id(1)

        with StudyGroupMapper() as mapper:
            return mapper.insert(studygroup)

    def create_studygroup_package (self, name, user_id):
        """StudyGroup wird zusammen mit LearninProfileGroup, GoogleID und einer GroupInvitation kreiert"""

        studygroup = self.create_studygroup(name)
        self.create_learningprofile_group(studygroup.get_id(),studygroup.get_name(),
            1, 1, 1, 1, 1, 1, "interest_preset", "degree_course_preset"
            )
        print(studygroup)

        user = self.get_user_by_google_id(user_id)
        print(user)

        self.create_groupinvitation(user.get_id(), user.get_id(), studygroup.get_id(),1)

    def get_studygroup_by_name(self, name):
        """Den StudyGroup über den gegebenen Namen Auslesen"""

        with StudyGroupMapper() as mapper:
            return mapper.find_by_group_name(name)

    def get_studygroup_by_id(self, id):
        """StudyGroup mit gegebener ID Auslesen"""

        with StudyGroupMapper() as mapper:
            return mapper.find_by_id(id)

    def get_studygroup_by_learning_profile_id(self, learning_profile_id):
        """StudyGroup über die gegebene LearningProfileID auslesen"""

        with StudyGroupMapper() as mapper:
            return mapper.find_group_by_learning_profile_id(learning_profile_id)

    def get_all_studygroups(self):
        """Auslesen aller StudyGroups in unserem System"""

        with StudyGroupMapper() as mapper:
            return mapper.find_all()

    def save_studygroup(self, studygroup):
        """Die gegebene StudyGroup speichern."""

        with StudyGroupMapper() as mapper:
            mapper.update(studygroup)

    def delete_studygroup(self, studygroup):
        """Die gegebene StudyGroup aus unserem System löschen."""

        with StudyGroupMapper() as mapper:
            mapper.delete(studygroup)


    # GroupInvitation Methoden

    def create_groupinvitation(self, source_user, target_user, studygroup_id, is_accepted):
        """GroupInvitation wird erstellt"""

        groupinvitation = GroupInvitation()
        groupinvitation.set_source_user(source_user)
        groupinvitation.set_target_user(target_user)
        groupinvitation.set_study_group_id(studygroup_id)
        groupinvitation.set_is_accepted(is_accepted)
        groupinvitation.set_id(1)

        with GroupInvitationMapper() as mapper:
            return mapper.insert(groupinvitation)

    def get_groupinvitation_by_id(self,id):
        """GroupInvitation mit gegebener ID Auslesen"""

        with GroupInvitationMapper() as mapper:
            return mapper.find_by_id(id)

    def get_groupinvitations_by_source_user(self, source_user):
        """Alle GroupInvitations über den gegebenen SourceUser Auslesen"""

        with GroupInvitationMapper() as mapper:
            return mapper.find_all_group_invitations_by_source_user(source_user)

    def get_groupinvitations_by_target_user(self, target_user):
        """Alle GroupInvitations über den gegebenen TargetUser Auslesen"""

        with GroupInvitationMapper() as mapper:
            return mapper.find_all_group_invitations_by_target_user(target_user)

    def get_all_pend_groupinvites(self):
        """Auslesen aller nicht akzeptierten oder gelöschten GroupInvitations in unserem System"""

        with GroupInvitationMapper() as mapper:
            return mapper.find_all_pend_invites()

    def get_pend_groupinvites_by_target_user(self, target_user):
        """Auslesen aller nicht akzeptierten oder gelöschten GroupInvitations des TargetUsers"""

        with GroupInvitationMapper() as mapper:
            return mapper.find_pend_invites_by_target_user(target_user)

    def get_pend_groupinvites_by_source_user(self, source_user):
        """Auslesen aller nicht akzeptierten oder gelöschten GroupInvitations des SourceUsers"""

        with GroupInvitationMapper() as mapper:
            return mapper.find_pend_invites_by_source_user(source_user)

    def get_accepted_groupinvites_by_source_user(self, source_user):
        """Auslesen von akzeptierten GroupInvitations des gegebenen SourceUsers"""

        with GroupInvitationMapper() as mapper:
            return mapper.find_accepted_invites_by_source_user(source_user)

    def get_accepted_groupinvites_by_target_user(self, target_user):
        """Auslesen von akzeptierten GroupInvitations des gegebenen TargetUsers"""

        with GroupInvitationMapper() as mapper:
            return mapper.find_accepted_invites_by_target_user(target_user)

    def get_groupinvitation_by_study_group_id(self, study_group_id):
        """Auslesen von GroupInvitations über die StudyGroupID"""

        with GroupInvitationMapper() as mapper:
            return mapper.find_all_group_invitations_by_StudyGroup(study_group_id)

    def get_accepted_groupinvitation_by_study_group_id(self, study_group_id):
        """Auslesen von akzeptierten GroupInvitations über die StudyGroupID"""

        with GroupInvitationMapper() as mapper:
            return mapper.find_all_accepted_user_in_study_group(study_group_id)

    def get_groupinvitation_pend_invites_by_study_group(self, study_group):
        """Auslesen aller nicht akzeptierten oder gelöschten GroupInvitations über die StudyGroup"""

        with GroupInvitationMapper() as mapper:
            return mapper.find_all_pend_user_in_study_group(study_group)

    def get_all_groupinvitations(self):
        """Alle GroupInvitations in unserem System Auslesen."""

        with GroupInvitationMapper() as mapper:
            return mapper.find_all()

    def save_groupinvitation(self, group_invite):
        """Die gegebene GroupInvitation speichern."""

        with GroupInvitationMapper() as mapper:
            mapper.update(group_invite)

    def delete_groupinvitation(self, group_invite):
        """Die gegebene GroupInvitation aus unserem System löschen."""

        with GroupInvitationMapper() as mapper:
            mapper.delete(group_invite)

    def get_groups_by_google_id(self, google_id):
        """Groups über die gegebene GoogleID Auslesen"""

        user = self.get_user_by_google_id(google_id)
        user_id = user.get_id()
        groupPart_ids = []

        # Wo SourceUser

        groupInv_by_target = self.get_accepted_groupinvites_by_target_user(user_id)
        if type(groupInv_by_target) != list:
            groupInv_by_target = [groupInv_by_target]
        for obj in groupInv_by_target:
            groupPart_ids.append(obj.get_study_group_id())

        # Wo TargetUser

        groupInv_by_source = self.get_accepted_groupinvites_by_source_user(user_id)
        if type(groupInv_by_source) != list:
            groupInv_by_source = [groupInv_by_source]

        for obj in groupInv_by_source:
            groupPart_ids.append(obj.get_study_group_id())

        groupPart_ids = list(dict.fromkeys(groupPart_ids))

        group_objects = []
        for num in groupPart_ids:
            group_objects.append(self.get_studygroup_by_id(num))

        return group_objects

    def get_user_pending_invites_groups_by_google_id(self, google_id):
        """Nicht akzeptierte oder gelöschte GroupInvitations über die gegebene GoogleID Auslesen"""

        invites_and_groups = []
        groups = self.get_groups_by_google_id(google_id)

        if type(groups) != list:
            groups = [groups]

        for x in groups:
            invs = self.get_groupinvitation_pend_invites_by_study_group(x.get_id())
            if type(invs) != list:
                invs = [invs]
            for inv in invs:
                group = self.get_studygroup_by_id(inv.get_study_group_id())
                invites_and_groups.append([inv, group])

        result = []

        for x in invites_and_groups:
            source_user_id = x[0].get_source_user()
            source_user = self.get_user_by_id(source_user_id)
            result.append([source_user, x[1]])

        return result


    # ChatMessage Methoden

    def create_chatmessage(self, chat_id, user_id, text):
        """ChatMessage wird erstellt"""

        chatmessage = ChatMessage()
        chatmessage.set_chat_id(chat_id)
        chatmessage.set_user_id(user_id)
        chatmessage.set_text(text)
        chatmessage.set_id(1)

        with ChatMessageMapper() as mapper:
            return mapper.insert(chatmessage)

    def get_chatmessage_by_id(self,id):
        """ChatMessage mit gegebener ID Auslesen"""

        with ChatMessageMapper() as mapper:
            return mapper.find_by_id(id)

    def get_chatmessages_by_chat_id(self, chat_id):
        """ChatMessage mit gegebener ChatID Auslesen"""

        with ChatMessageMapper() as mapper:
            return mapper.find_all_by_chat_id(chat_id)

    def get_all_chatmessages(self):
        """Auslesen aller ChatMessages in unserem System"""

        with ChatMessageMapper() as mapper:
            return mapper.find_all()

    def get_chatmessages_by_user_id(self,user_id):
        """ChatMessage über die gegebene UserID Auslesen"""

        with ChatMessageMapper() as mapper:
            return mapper.find_all_by_user_id(user_id)

    def save_chatmessage(self, chatmessage):
        """Die gegebene ChatMessage speichern"""

        with ChatMessageMapper() as mapper:
            mapper.update(chatmessage)

    def delete_chatmessage(self, chatmessage):
        """Die gegebene ChatMessage löschen"""

        with ChatMessageMapper() as mapper:
            mapper.delete(chatmessage)


    # Chat Methoden

    def create_chat(self, name):
        """Chat wird erstellt"""

        chat = Chat()
        chat.set_name(name)
        chat.set_id(1)

        with ChatMapper() as mapper:
            return mapper.insert(chat)

    def get_chat_by_id(self, id):
        """ChatMessage mit gegebener ID Auslesen"""

        with ChatMapper() as mapper:
            return mapper.find_by_id(id)

    def get_chat_by_name(self, name):
        """Auslesen des Chats über den gegebenen Namen"""

        with ChatMapper() as mapper:
            return mapper.find_by_name(name)

    def get_all_chats(self):
        """Auslesen aller Chats in unserem System"""

        with ChatMapper() as mapper:
            return mapper.find_all()

    def save_chat(self, chat):
        """Den gegebenen Chat speichern"""

        with ChatMapper() as mapper:
            mapper.update(chat)

    def delete_chat(self, single_chat):
        """Den gegebenen Chat löschen"""

        with ChatMapper() as mapper:
            mapper.delete(single_chat)

    def get_chat_by_user_id(self, user_id):
        """Auslesen des Chats über die gegebene UserID"""

        acc_invites_source = self.get_accepted_invites_by_source_user(user_id)
        acc_invites_target = self.get_accepted_invites_by_target_user(user_id)

        if type(acc_invites_source) != list:
            acc_invites_source = [acc_invites_source]

        if type(acc_invites_target) != list:
            acc_invites_target = [acc_invites_target]

        acc_invites = acc_invites_source + acc_invites_target

        chat_ids = []
        for i in acc_invites:
            if i.get_chat_id() != 1: # Id 1 ist eine platzhalter id
                chat_ids.append(i.get_chat_id())

        chat_objs = []
        for i in chat_ids:
            chat_objs.append(self.get_chat_by_id(i))

        return chat_objs

    def get_studygroup_by_chat_id(self, chat_id):
        """Auslesen der StudyGroup über die gegebene ChatID"""

        with StudyGroupMapper() as mapper:
            return mapper.find_by_chat_id(chat_id)

    def get_group_users_by_chat(self, current_user_id, chat_id):
        """Auslesen aller User in der Group über den Chat"""

        group = self.get_studygroup_by_chat_id(chat_id)
        group_ID = group.get_id()

        invites = self.get_groupinvitation_by_study_group_id(group_ID)

        if type(invites) != list:
            invites = [invites]

        acc_invites = []
        for i in invites:
            if i.get_is_accepted() == 1:
                acc_invites.append(i)
        user_ids = []

        for i in acc_invites:
            if i.get_source_user() == i.get_target_user():
                user_ids.append(i.get_source_user())
            else:
                user_ids.append(i.get_source_user())
                user_ids.append(i.get_target_user())
        users = []
        for i in user_ids:
            users.append(self.get_user_by_id(i))

        filtered_users = []
        known_ids = []
        for user in users:
            if user.get_id() not in known_ids and user.get_id() != current_user_id:
                known_ids.append(user.get_id())
                filtered_users.append(user)
            else:
                pass

        return filtered_users

    def isgroupchat(self, chat_id):
        """Schaut ob es sich hier um einen GroupChat handelt"""

        all_study_groups = self.get_all_studygroups()
        result = False

        if type(all_study_groups) != list:
            all_study_groups = [all_study_groups]

        for group in all_study_groups:
            if group.get_chat_id() == chat_id:
                result = True
                break

        return result


    def get_other_user_by_chat_id(self,user_id, chat_id):
        """Auslesen anderer User über die ChatID"""

        acc_invites_source = self.get_accepted_invites_by_source_user(user_id)
        acc_invites_target = self.get_accepted_invites_by_target_user(user_id)

        if type(acc_invites_source) != list:
            acc_invites_source = [acc_invites_source]

        if type(acc_invites_target) != list:
            acc_invites_target = [acc_invites_target]

        acc_invites = acc_invites_source + acc_invites_target

        for i in acc_invites:
            if i.get_chat_id() == chat_id:
                if i.get_source_user() == user_id:
                    other_user = i.get_target_user()
                    return self.get_user_by_id(other_user)
                else:
                    other_user = i.get_source_user()
                    return self.get_user_by_id(other_user)

    def get_group_chat_by_user_id(self, user_id):
        """Auslesen des GroupChats über die UserID"""

        acc_invites_source = self.get_accepted_groupinvites_by_source_user(user_id)
        acc_invites_target = self.get_accepted_groupinvites_by_target_user(user_id)
        print(acc_invites_source)
        print(acc_invites_target)
        if type(acc_invites_source) != list:
            acc_invites_source = [acc_invites_source]

        if type(acc_invites_target) != list:
            acc_invites_target = [acc_invites_target]

        acc_invites = acc_invites_source + acc_invites_target

        group_ids = []

        for i in acc_invites:
            group_ids.append(i.get_study_group_id())

        group_ids = list(set(group_ids))

        group_objects = []

        for i in group_ids:
            group_objects.append(Administration().get_studygroup_by_id(i))

        chat_ids = []
        for i in group_objects:
            if i.get_chat_id() != 1:  # Id 1 ist eine platzhalter id
                chat_ids.append(i.get_chat_id())

        chat_objs = []
        for i in chat_ids:
            chat_objs.append(self.get_chat_by_id(i))
        return chat_objs

    def get_group_users_by_group_id(self, group_id):
        """Auslesen aller GroupUsers über die GroupID"""

        invites = self.get_groupinvitation_by_study_group_id(group_id)
        if type(invites) != list:
            invites = [invites]
        acc_invites = []
        for i in invites:
            if i.get_is_accepted() == True:
                acc_invites.append(i)
        user_ids = []
        for i in acc_invites:
            if i.get_source_user() == i.get_target_user():
                user_ids.append(i.get_source_user())
            else:
                user_ids.append(i.get_source_user())
                user_ids.append(i.get_target_user())
        users = []
        for i in user_ids:
            users.append(self.get_user_by_id(i))

        return users

    def accept_group_request(self, group_id, user_id):
        """Gruppeneinladung akzeptieren"""

        group_requests_source = self.get_pend_groupinvites_by_source_user(user_id)
        group_requests_target = self.get_pend_groupinvites_by_target_user(user_id)

        if type(group_requests_source) != list:
            group_requests_source = [group_requests_source]

        if type(group_requests_target) != list:
            group_requests_target = [group_requests_target]

        group_requests = group_requests_source + group_requests_target

        for req in group_requests:
            if req.get_study_group_id() == group_id:
                req.set_is_accepted(1)
                self.save_groupinvitation(req)

    def decline_group_request(self, group_id, user_id):
        """Gruppeneinladung ablehnen"""

        group_requests_source = self.get_pend_groupinvites_by_source_user(user_id)
        group_requests_target = self.get_pend_groupinvites_by_target_user(user_id)

        if type(group_requests_source) != list:
            group_requests_source = [group_requests_source]

        if type(group_requests_target) != list:
            group_requests_target = [group_requests_target]

        group_requests = group_requests_source + group_requests_target

        for req in group_requests:
            if req.get_study_group_id() == group_id:
                self.delete_groupinvitation(req)


    # Matching Algorithmus

    def get_matches_user(self, user_id, threshhold):
        """Output: {profile_id : 0,54, profile_id : 0,34}"""

        # Matches für anderen User
        user = self.get_user_by_google_id(user_id)
        self_profile = self.get_learningprofile_user_by_user_id(user.get_id())
        all_profiles = self.get_all_learningprofiles_user()
        other_profiles = []
        for profile in all_profiles:
            if not profile.get_user_id() == user.get_id():
                other_profiles.append(profile)

        # Dict mit allen User Learnprofile Id und Similarity Score, welche über dem Threshhold sind
        matches = {}
        for profile in other_profiles:
            """Alle Vergleichswerte (Range von 0 bis 1) 0 = Verschieden; 1 = Gleich"""
            """Reihenfolge: Prev_Knowledge, Extroversion, Study State, Frequency, Learntyp, Semester, Interest, Degree_course"""

            similarity = []
            weights = [1, 1, 1, 1, 1, 1, 1, 1]

            # Prev Knowledge
            max_input = 5

            score = max_input - (((self_profile.get_prev_knowledge() - profile.get_prev_knowledge())**2)**.5)
            if score != 0:
                score = score / max_input

            similarity.append(score)

            # Extroversion
            max_input = 5

            score = max_input - (((self_profile.get_extroversion() - profile.get_extroversion())**2)**.5)
            if score != 0:
                score = score / max_input

            similarity.append(score)

            # Study State
            max_input = 2

            score = max_input - (((self_profile.get_study_state() - profile.get_study_state())**2)**.5)
            if score != 0:
                score = score / max_input

            similarity.append(score)

            # Frequency
            max_input = 5

            score = max_input - (((self_profile.get_frequency() - profile.get_frequency())**2)**.5)
            if score != 0:
                score = score / max_input

            similarity.append(score)

            # Learntyp
            max_input = 5

            score = max_input - (((self_profile.get_learntyp() - profile.get_learntyp())**2)**.5)
            if score != 0:
                score = score / max_input

            similarity.append(score)

            # Semester
            max_input = 12

            score = max_input - (((self_profile.get_semester() - profile.get_semester())**2)**.5)
            if score != 0:
                score = score / max_input

            similarity.append(score)

            # Interest
            score = 0
            if self_profile.get_interest().lower() == profile.get_interest().lower():
                score = 1

            similarity.append(score)

            # Degree Course
            score = 0
            if self_profile.get_degree_course().lower() == profile.get_degree_course().lower():
                score = 1

            similarity.append(score)

            # Erstellung des Similarity Score (0-1)
            sim_score = 0
            for attr in range(len(similarity)):
                sim_score += similarity[attr] * weights[attr]

            sim_score /= len(similarity)

            # Bei direkter Übereinstimmung nur 99 prozent speichern
            if sim_score == 1:
                sim_score = .99

            # Wenn Similarity Score über dem Threshhold ist, zum dict hinzufügen
            if sim_score >= threshhold:
                matches[profile.get_id()] = sim_score

        return matches

    def get_matches_group(self, user_id, threshhold):
        """Output: {group_profile_id : 0,54, group_profile_id : 0,34}"""

        user = self.get_user_by_google_id(user_id)
        self_profile = self.get_learningprofile_user_by_user_id(user.get_id())
        group_profiles = self.get_all_learningprofiles_group()
        other_profiles = []

        for profile in group_profiles:
            other_profiles.append(profile)

        # Dict mit allen User Learnprofile Id und Similarity Score, welche über dem Threshhold sind
        matches = {}

        for profile in other_profiles:
            """Alle Vergleichswerte (Range von 0 bis 1) 0 = Verschieden; 1 = Gleich"""
            """Reihenfolge: Prev_Knowledge, Extroversion, Study State, Frequency, Learntyp, Semester, Interest, Degree_course"""
            
            similarity = []
            weights = [1, 1, 1, 1, 1, 1, 1, 1]

            # Prev Knowledge
            max_input = 5

            score = max_input - (((self_profile.get_prev_knowledge() - profile.get_prev_knowledge())**2)**.5)
            if score != 0:
                score = score / max_input

            similarity.append(score)

            # Extroversion
            max_input = 5

            score = max_input - (((self_profile.get_extroversion() - profile.get_extroversion())**2)**.5)
            if score != 0:
                score = score / max_input

            similarity.append(score)

            # Study State
            max_input = 2

            score = max_input - (((self_profile.get_study_state() - profile.get_study_state())**2)**.5)
            if score != 0:
                score = score / max_input

            similarity.append(score)

            # Frequency
            max_input = 5

            score = max_input - (((self_profile.get_frequency() - profile.get_frequency())**2)**.5)
            if score != 0:
                score = score / max_input

            similarity.append(score)

            # Learntyp
            max_input = 5

            score = max_input - (((self_profile.get_learntyp() - profile.get_learntyp())**2)**.5)
            if score != 0:
                score = score / max_input

            similarity.append(score)

            # Semester
            max_input = 12

            score = max_input - (((self_profile.get_semester() - profile.get_semester())**2)**.5)
            if score != 0:
                score = score / max_input

            similarity.append(score)

            # Interest
            score = 0
            if self_profile.get_interest().lower() == profile.get_interest().lower():
                score = 1

            similarity.append(score)

            # Degree Course
            score = 0
            if self_profile.get_degree_course().lower() == profile.get_degree_course().lower():
                score = 1

            similarity.append(score)

            # Erstellung des Similarity Score (0-1)
            sim_score = 0
            for attr in range(len(similarity)):
                sim_score += similarity[attr] * weights[attr]

            sim_score /= len(similarity)

            # Bei direkter Übereinstimmung nur 99 prozent speichern
            if sim_score == 1:
                sim_score = .99

            # Wenn Similarity Score über dem Threshhold ist, zum dict hinzufügen
            if sim_score >= threshhold:
                matches[profile.get_id()] = sim_score

        return matches
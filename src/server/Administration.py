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

    Diese Klasse steht mit einer Reihe weiterer Datentypen in Verbindung. Dies
    sind:
    - die Klassen BusinessObject und deren Subklassen,
    - die Mapper-Klassen für den DB-Zugriff.

    BankAdministration bilden nur die Server-seitige Sicht der
    Applikationslogik ab. Diese basiert vollständig auf synchronen
    Funktionsaufrufen.

    **Wichtiger Hinweis:** Diese Klasse bedient sich sogenannter
    Mapper-Klassen. Sie gehören der Datenbank-Schicht an und bilden die
    objektorientierte Sicht der Applikationslogik auf die relationale
    organisierte Datenbank ab. Zuweilen kommen "kreative" Zeitgenossen auf die
    Idee, in diesen Mappern auch Applikationslogik zu realisieren. Siehe dazu
    auch die Hinweise in der Methode zum Löschen von Customer-Objekten.
    Einzig nachvollziehbares Argument für einen solchen Ansatz ist die Steigerung
    der Performance umfangreicher Datenbankoperationen. Doch auch dieses Argument
    zieht nur dann, wenn wirklich große Datenmengen zu handhaben sind. In einem
    solchen Fall würde man jedoch eine entsprechend erweiterte Architektur realisieren,
    die wiederum sämtliche Applikationslogik in der Applikationsschicht isolieren
    würde. Also: keine Applikationslogik in die Mapper-Klassen "stecken" sondern
    dies auf die Applikationsschicht konzentrieren!

    Es gibt sicherlich noch viel mehr über diese Klasse zu schreiben. Weitere
    Infos erhalten Sie in der Lehrveranstaltung.
    """
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
            return mapper.insert(user)


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
        with UserMapper() as mapper:
            return mapper.find_user_by_firstname(first_name)

    def get_user_by_lastname(self, last_name):
        with UserMapper() as mapper:
            return mapper.find_user_by_lastname(last_name)

    def get_all_users(self):
        """Alle User auslesen."""
        with UserMapper() as mapper:
            return mapper.find_all()

    def get_user_by_learning_profile_id(self,learning_profile_id):
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
        with LearningProfileGroupMapper() as mapper:
            return mapper.find_by_name(name)

    def get_learningprofile_group_by_id(self, number):
        with LearningProfileGroupMapper() as mapper:
            return mapper.find_by_id(number)

    def get_learningprofile_group_by_group_id(self, group_id):
        with LearningProfileGroupMapper() as mapper:
            return mapper.find_by_group_id(group_id)

    def get_all_learningprofiles_group(self):
        """Alle Learningprofiles group auslesen."""
        with LearningProfileGroupMapper() as mapper:
            return mapper.find_all()

    def save_learningprofile_group(self, learningprofile):
        """Das gegebene Learningprofile group speichern."""
        with LearningProfileGroupMapper() as mapper:
            mapper.update(learningprofile)

    def delete_learningprofile_group(self, learningprofile):
        """Das gegebene LearningProfile group aus unserem System löschen."""
        with LearningProfileGroupMapper() as mapper:
            mapper.delete(learningprofile)

    # LearningProfile User Methoden
    def create_learningprofile_user(self, user_id, name, frequency, study_state, extroversion, prev_knowledge,
                                         learntyp, semester, interest, degree_course):
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
        with LearningProfileUserMapper() as mapper:
            return mapper.find_by_name(name)

    def get_learningprofile_user_by_id(self, number):
        with LearningProfileUserMapper() as mapper:
            return mapper.find_by_id(number)

    def get_learningprofile_user_by_user_id(self, user_id):
        with LearningProfileUserMapper() as mapper:
            return mapper.find_by_user_id(user_id)

    def get_all_learningprofiles_user(self):
        """Alle Learningprofiles user auslesen."""
        with LearningProfileUserMapper() as mapper:
            return mapper.find_all()

    def save_learningprofile_user(self, learningprofile):
        """Das gegebene Learningprofile user speichern."""
        with LearningProfileUserMapper() as mapper:
            mapper.update(learningprofile)

    def get_user_id_by_learningprofile_id(self, id):
        with LearningProfileUserMapper() as mapper:
            return mapper.get_user_id_by_learningprofile_id(id)


    def delete_learningprofile_user(self, learningprofile):
        """Das gegebene LearningProfile user aus unserem System löschen."""
        with LearningProfileUserMapper() as mapper:

            mapper.delete(learningprofile)

    # ChatInvitation Methoden
    def create_chatinvitation(self, source_user, target_user, chat_id, is_accepted):
        chatinvitation = ChatInvitation()
        chatinvitation.set_source_user(source_user)
        chatinvitation.set_target_user(target_user)
        chatinvitation.set_chat_id(chat_id)
        chatinvitation.set_is_accepted(is_accepted)
        chatinvitation.set_id(1)

        with ChatInvitationMapper() as mapper:
            return mapper.insert(chatinvitation)

    def get_chatinvitation_by_id(self, number):
        with ChatInvitationMapper() as mapper:
            return mapper.find_by_id(number)

    def get_all_invites_by_target_user(self, target_user):
        with ChatInvitationMapper() as mapper:
            return mapper.find_all_invites_by_target_user(target_user)

    def get_all_invites_by_source_user(self, source_user):
        with ChatInvitationMapper() as mapper:
            return mapper.find_all_invites_by_source_user(source_user)

    def get_all_accepted_user_in_chat(self, chat_id):
        with ChatInvitationMapper() as mapper:
            return mapper.find_all_accepted_user_in_chat(chat_id)

    def get_all_pend_invites(self):
        with ChatInvitationMapper() as mapper:
            return mapper.find_all_pend_invites()

    def get_pend_invites_by_target_user(self, target_user):
        with ChatInvitationMapper() as mapper:
            return mapper.find_pend_invites_by_target_user(target_user)

    def get_pend_invites_by_source_user(self, source_user):
        with ChatInvitationMapper() as mapper:
            return mapper.find_pend_invites_by_source_user(source_user)

    def get_accepted_invites_by_source_user(self, source_user):
        with ChatInvitationMapper() as mapper:
            return mapper.find_accepted_invites_by_source_user(source_user)

    def get_accepted_invites_by_target_user(self, target_user):
        with ChatInvitationMapper() as mapper:
            return mapper.find_accepted_invites_by_target_user(target_user)

    def get_all_chatinvitations(self):
        """Alle Chatinvitations auslesen."""
        with ChatInvitationMapper() as mapper:
            return mapper.find_all()

    def save_chatinvitation(self, invite):
        """Die gegebene chatinvitation speichern."""
        with ChatInvitationMapper() as mapper:
            mapper.update(invite)

    def delete_chatinvitation(self, id):
        """Die gegebene chatinvitation aus unserem System löschen."""
        with ChatInvitationMapper() as mapper:
            mapper.delete(id)

    # StudyGroup Methoden
    def create_studygroup (self, name, chat_id):
        studygroup = StudyGroup()
        studygroup.set_name(name)
        studygroup.set_chat_id(chat_id)
        studygroup.set_id(1)

        with StudyGroupMapper() as mapper:
            return mapper.insert(studygroup)

    def get_studygroup_by_name(self, name):
        with StudyGroupMapper() as mapper:
            return mapper.find_by_group_name(name)

    def get_studygroup_by_id(self, id):
        with StudyGroupMapper() as mapper:
            return mapper.find_by_id(id)

    def get_studygroup_by_learning_profile_id(self, learning_profile_id):
        with StudyGroupMapper() as mapper:
            return mapper.find_group_by_learning_profile_id(learning_profile_id)

    def get_all_studygroups(self):
        with StudyGroupMapper() as mapper:
            return mapper.find_all()

    def save_studygroup(self, studygroup):
        with StudyGroupMapper() as mapper:
            mapper.update(studygroup)

    def delete_studygroup(self, studygroup):
        with StudyGroupMapper() as mapper:
            mapper.delete(studygroup)


    # GroupInvitation Methoden


    def create_groupinvitation(self, source_user, target_user, chat_id, is_accepted):
        groupinvitation = GroupInvitation()
        groupinvitation.set_source_user(source_user)
        groupinvitation.set_target_user(target_user)
        groupinvitation.set_study_group_id(chat_id)
        groupinvitation.set_is_accepted(is_accepted)
        groupinvitation.set_id(1)

        with GroupInvitationMapper() as mapper:
            return mapper.insert(groupinvitation)

    def get_groupinvitation_by_id(self,id):
        with GroupInvitationMapper() as mapper:
            return mapper.find_by_id(id)

    def get_groupinvitations_by_source_user(self, source_user):
        with GroupInvitationMapper() as mapper:
            return mapper.find_all_group_invitations_by_source_user(source_user)

    def get_groupinvitations_by_target_user(self, target_user):
        with GroupInvitationMapper() as mapper:
            return mapper.find_all_group_invitations_by_target_user(target_user)

    def get_all_pend_groupinvites(self):
        with GroupInvitationMapper() as mapper:
            return mapper.find_all_pend_invites()

    def get_pend_groupinvites_by_target_user(self, target_user):
        with GroupInvitationMapper() as mapper:
            return mapper.find_pend_invites_by_target_user(target_user)

    def get_pend_groupinvites_by_source_user(self, source_user):
        with GroupInvitationMapper() as mapper:
            return mapper.find_pend_invites_by_source_user(source_user)

    def get_accepted_groupinvites_by_source_user(self, source_user):
        with GroupInvitationMapper() as mapper:
            return mapper.find_accepted_invites_by_source_user(source_user)

    def get_accepted_groupinvites_by_target_user(self, target_user):
        with GroupInvitationMapper() as mapper:
            return mapper.find_accepted_invites_by_target_user(target_user)

    def get_groupinvitation_by_study_group_id(self, study_group_id):
        with GroupInvitationMapper() as mapper:
            return mapper.find_all_group_invitations_by_StudyGroup(study_group_id)


    def get_accepted_groupinvitation_by_study_group_id(self, study_group_id):
        with GroupInvitationMapper() as mapper:
            return mapper.find_all_accepted_user_in_study_group(study_group_id)

    def get_groupinvitation_pend_invites_by_study_group(self, study_group):
        with GroupInvitationMapper() as mapper:
            return mapper.find_all_pend_user_in_study_group(study_group)

    def get_all_groupinvitations(self):
        """Alle Chatinvitations auslesen."""
        with GroupInvitationMapper() as mapper:
            return mapper.find_all()

    def save_groupinvitation(self, group_invite):
        """Die gegebene chatinvitation speichern."""
        with GroupInvitationMapper() as mapper:
            mapper.update(group_invite)

    def delete_groupinvitation(self, group_invite):
        """Die gegebene chatinvitation aus unserem System löschen."""
        with GroupInvitationMapper() as mapper:
            mapper.delete(group_invite)


    # ChatMessage Methoden
    def create_chatmessage(self, chat_id, user_id, text):
        chatmessage = ChatMessage()
        chatmessage.set_chat_id(chat_id)
        chatmessage.set_user_id(user_id)
        chatmessage.set_text(text)
        chatmessage.set_id(1)

        with ChatMessageMapper() as mapper:
            return mapper.insert(chatmessage)

    def get_chatmessage_by_id(self,id):
        with ChatMessageMapper() as mapper:
            return mapper.find_by_id(id)

    def get_chatmessages_by_chat_id(self, chat_id):
        with ChatMessageMapper() as mapper:
            return mapper.find_all_by_chat_id(chat_id)

    def get_all_chatmessages(self):
        with ChatMessageMapper() as mapper:
            return mapper.find_all()

    def get_chatmessages_by_user_id(self,user_id):
        with ChatMessageMapper() as mapper:
            #### find by user_id fehlt? brauchen wir das?
            return mapper.find_all_by_user_id(user_id)

    def save_chatmessage(self, chatmessage):
        with ChatMessageMapper() as mapper:
            mapper.update(chatmessage)

    def delete_chatmessage(self, chatmessage):
        with ChatMessageMapper() as mapper:
            mapper.delete(chatmessage)

    # Chat Methoden

    def create_chat(self, name):
        chat = Chat()
        chat.set_name(name)
        chat.set_id(1)

        with ChatMapper() as mapper:
            return mapper.insert(chat)

    def get_chat_by_id(self, id):
        with ChatMapper() as mapper:
            return mapper.find_by_id(id)

    def get_chat_by_name(self, name):
        with ChatMapper() as mapper:
            return mapper.find_by_name(name)

    def get_all_chats(self):
        with ChatMapper() as mapper:
            return mapper.find_all()

    def save_chat(self, chat):
        with ChatMapper() as mapper:
            mapper.update(chat)

    def delete_chat(self, single_chat):
        with ChatMapper() as mapper:
            mapper.delete(single_chat)

    # Matching Algorithmus

    def get_matches_user(self, user_id, threshhold):
        """Output: {profile_id : 0,54, profile_id : 0,34}"""

        # Matches for other Users
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
            max_input = 5

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
            max_input = 5

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

            # Wenn Similarity Score über dem Threshhold ist, zum dict hinzufügen
            if sim_score >= threshhold:
                matches[profile.get_id()] = sim_score

        return matches

    def get_matches_group(self, user_id, threshhold):
        """Output: {group_profile_id : 0,54, group_profile_id : 0,34}"""

        # Matches for Groups
        self_profile = self.get_learningprofile_user_by_id(user_id)
        group_profiles = self.get_all_learningprofiles_group()
        # Dict mit allen User Learnprofile Id und Similarity Score, welche über dem Threshhold sind
        matches = {}
        other_profiles = []
        if group_profiles != list():
            other_profiles.append(group_profiles)
        else:
            for profile in group_profiles:
                other_profiles.append(profile)

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
            max_input = 5

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
            max_input = 5

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

            # Wenn Similarity Score über dem Threshhold ist, zum dict hinzufügen
            if sim_score >= threshhold:
                matches[profile.get_id()] = sim_score

        return matches

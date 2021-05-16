from .bo.User import User
from .bo.Chat import Chat
from .bo.ChatInvitation import ChatInvitation
from .bo.ChatMessage import ChatMessage
from .bo.LearningProfile import LearningProfile
from .bo.StudyGroup import StudyGroup
from .bo.GroupInvitation import GroupInvitation

from .db.UserMapper import *
from .db.ChatMapper import *
from .db.ChatInvitationMapper import *
from .db.ChatMessageMapper import *
from .db.LearningProfileMapper import *
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
    def create_user(self, name, google_id, first_name, last_name, email, adress):
        """Einen Benutzer anlegen"""
        user = User()
        user.set_name(name)  # Name von NamedBusinessObject
        user.set_google_id(google_id)
        user.set_firstname(first_name)
        user.set_lastname(last_name)
        user.set_email(email)
        user.set_adress(adress)
        user.set_id(1)

    def get_user_by_name(self, name):
        """Alle Benutzer mit Namen name auslesen."""
        with UserMapper() as mapper:
            return mapper.find_by_name(name)

    def get_user_by_id(self, number):
        """Den Benutzer mit der gegebenen ID auslesen."""
        with UserMapper() as mapper:
            return mapper.find_by_id(number)

    def get_user_by_email(self, email):
        """Alle Benutzer mit gegebener E-Mail-Adresse auslesen."""
        with UserMapper() as mapper:
            return mapper.find_user_by_email(email)

    def get_user_by_google_id(self, id):
        """Den Benutzer mit der gegebenen Google ID auslesen."""
        with UserMapper() as mapper:
            return mapper.find_user_by_google_id(id)

    def get_user_by_firstname(self, first_name):
        with UserMapper() as mapper:
            return mapper.find_user_by_firstname(first_name)

    def get_user_by_lastname(self, last_name):
        with UserMapper() as mapper:
            return mapper.find_user_by_lastname(last_name)

    def get_all_users(self):
        """Alle Benutzer auslesen."""
        with UserMapper() as mapper:
            return mapper.find_all()

    def save_user(self, user):
        """Den gegebenen Benutzer speichern."""
        with UserMapper() as mapper:
            mapper.update(user)

    def delete_user(self, user):
        """Den gegebenen Benutzer aus unserem System löschen."""
        with UserMapper() as mapper:
            mapper.delete(user)

    # LearningProfile Methoden
    def create_learningprofile(self, name, frequency, study_state, extroversion, prev_knowledge,
                               learntype, interest, semester, degree_course):
        learningprofile = LearningProfile()
        learningprofile.set_name(name)
        learningprofile.set_frequency(frequency)
        learningprofile.set_study_state(study_state)
        learningprofile.set_extroversion(extroversion)
        learningprofile.set_prev_knowledge(prev_knowledge)
        learningprofile.set_learntyp(learntype)
        learningprofile.set_interest(interest)
        learningprofile.set_semester(semester)
        learningprofile.set_degree_course(degree_course)
        learningprofile.set_id(1)

    def get_learningprofile_by_name(self, name):
        with LearningProfileMapper() as mapper:
            return mapper.find_by_name(name)

    def get_learningprofile_by_id(self, number):
        with LearningProfileMapper() as mapper:
            return mapper.find_by_id(number)

    def get_learningprofile_by_user_id(self, user_id):
        with LearningProfileMapper() as mapper:
            return mapper.find_by_user_id(user_id)

    def get_learningprofile_by_group_id(self, group_id):
        with LearningProfileMapper() as mapper:
            return mapper.find_by_user_id(group_id)

    def get_all_learningprofiles(self):
        """Alle Learningprofiles auslesen."""
        with LearningProfileMapper() as mapper:
            return mapper.find_all()

    def save_learningprofile(self, learningprofile):
        """Das gegebene Learningprofile speichern."""
        with LearningProfileMapper() as mapper:
            mapper.update(learningprofile)

    def delete_learningprofile(self, learningprofile):
        """Das gegebene LearningProfile aus unserem System löschen."""
        with LearningProfileMapper() as mapper:
            mapper.delete(learningprofile)

    # ChatInvitation Methoden
    def create_chatinvitation(self, source_user, target_user, chat_id, is_accepted):
        chatinvitation = ChatInvitation()
        chatinvitation.set_source_user(source_user)
        chatinvitation.set_target_user(target_user)
        chatinvitation.set_chat_id(chat_id)
        chatinvitation.set_is_accepted(is_accepted)
        chatinvitation.set_id(1)

    def get_chatinvitation_by_id(self, number):
        with ChatInvitationMapper() as mapper:
            return mapper.find_by_id(number)

    def get_all_invites_by_target_user(self, target_user):
        with ChatInvitationMapper() as mapper:
            return mapper.find_all_invites_by_target_user(target_user)

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

    def delete_chatinvitation(self, invite):
        """Die gegebene chatinvitation aus unserem System löschen."""
        with ChatInvitationMapper() as mapper:
            mapper.delete(invite)
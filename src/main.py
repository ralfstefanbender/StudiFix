from flask import Flask
# Auf Flask aufbauend nutzen wir RestX
from flask_restx import Api, Resource, fields
# Wir benutzen noch eine Flask-Erweiterung für Cross-Origin Resource Sharing
from flask_cors import CORS

from src.server.Administration import Administration
from src.server.bo.ChatInvitation import ChatInvitation

from src.server.bo.ChatMessage import ChatMessage

from src.server.bo.GroupInvitation import GroupInvitation
from src.server.bo.LearningprofileGroup import LearningProfileGroup
from src.server.bo.LearningProfileUser import LearningProfileUser
from src.server.bo.StudyGroup import StudyGroup
from src.server.bo.User import User
from src.server.bo.Chat import Chat

"""
A. Allgemeine Hinweise zu diesem Module:
Normalerweise würde man eine Datei dieser Länge bzw. ein Module
dieser Größe in mehrere Dateien bzw. Modules untergliedern. So könnte
man z.B. pro Resource Class ein eigenes Module anlegen. Dadurch
ergäben sich erhebliche Vorteile bzgl. der Wartungsfreundlichkeit
dieses Modules. Es ergäben sich aber auch Nachteile! So haben Sie
etwa mit einer Reihe von Abhängigkeiten z.B. zwischen der API-Definition
und den Decorators zu tun. Außerdem verschlechtert sich aufgrund der Länge
der Datei die Übersichtlichkeit der Inhalte und Strukturen.
Abgesehen von Lehrbüchern und Vorlesungen müssen Sie in realen Projekten
häufig die Vor- und Nachteile von Entscheidungen abwägen und sich dann
bewusst für einen Weg entscheiden. Hier wurde die Entscheidung getroffen,
die Einfachheit und Verständlichkeit des Source Codes höher zu werten als
die Optimierung des Kopplungsgrads und damit die Wartbarkeit des Modules.
B. Konventionen für dieses Module:
    B.1. HTTP response status codes:
        Folgende Codes werden verwendet:
        200 OK           :      bei erfolgreichen requests. Af die Verwendung von
                                weiter differenzierenden Statusmeldungen wie etwa
                                '204 No Content' für erfolgreiche requests, die
                                außer evtl. im Header keine weiteren Daten zurückliefern,
                                wird in dieser Fallstudie auch aus Gründen einer
                                möglichst einfachen Umsetzung verzichtet.
        401 Unauthorized :      falls der User sich nicht gegenüber dem System
                                authentisiert hat und daher keinen Zugriff erhält.
        404 Not Found    :      falls eine angefragte Resource nicht verfügbar ist
        500 Internal Server Error : falls der Server einen Fehler erkennt,
                                diesen aber nicht genauer zu bearbeiten weiß.
    B.2. Name des Moduls:
        Der Name dieses Moduls lautet main.py. Grund hierfür ist, dass Google
        App Engine, diesen Namen bevorzugt und sich dadurch das Deployment
        einfacher gestaltet. Natürlich wären auch andere Namen möglich. Dies
        wäre aber mit zusätzlichem Konfigurationsaufwand in der Datei app.yaml
        verbunden.
"""

app = Flask(__name__)
"""
Instanzieren von Flask. Am Ende dieser Datei erfolgt dann erst der 'Start' von Flask.
"""

CORS(app, resources=r'/StudiFix/*')
"""
Alle Ressourcen mit dem Präfix /studifix für **Cross-Origin Resource Sharing** (CORS) freigeben.
Diese eine Zeile setzt die Installation des Package flask-cors voraus. 
"""

"""
In dem folgenden Abschnitt bauen wir ein Modell auf, das die Datenstruktur beschreibt, 
auf deren Basis Clients und Server Daten austauschen. Grundlage hierfür ist das Package flask-restx.
"""
api = Api(app, version='1.0', title='StudiFix API',
          description='Eine App zum auffinden von Lernpartnern und Lerngruppen.')

"""Anlegen eines Namespace
Namespaces erlauben uns die Strukturierung von APIs. In diesem Fall fasst dieser Namespace alle
StudiFix-relevanten Operationen unter dem Präfix /bank zusammen. Eine alternative bzw. ergänzende Nutzung
von Namespace könnte etwa sein, unterschiedliche API-Version voneinander zu trennen, um etwa 
Abwärtskompatibilität (vgl. Lehrveranstaltungen zu Software Engineering) zu gewährleisten. Dies ließe
sich z.B. umsetzen durch /bank/v1, /bank/v2 usw."""

studifix = api.namespace('StudiFix', description='Funktionen des StudiFix')

bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Unique id of a business object'),
    'creation_date': fields.DateTime(attribute='_creation_date', description='creation date of a business object',
                                     dt_format='iso8601')
})

nbo = api.inherit('NamedBusinessObject', bo, {
    'name': fields.String(attribute='_name', description='name of a named business object')
})

chat = api.inherit('Chat', nbo, {

})

chatinvitation = api.inherit('ChatInvitation', bo, {
    'source_user': fields.Integer(attribute='_source_user', description='Unique Id des Chatinhabers'),
    'target_user': fields.Integer(attribute='_target_user', description='Unique Id des Einzuladenden'),
    'chat_id': fields.Integer(attribute='_chat_id', description='Chat id des Chats'),
    'is_accepted': fields.Boolean(attribute='_is_accepted', description='Akzeptierte Chateinladungen')
})

chatmessage = api.inherit('ChatMessage', bo, {
    'chat_id': fields.Integer(attribute='_chat_id', description='Unique Id des Chats'),
    'user_id': fields.Integer(attribute='_user_id', description='Unique Id des Versenders'),
    'text': fields.String(attribute='_text', description='Inhalt der Nachricht')
})

groupinvitation = api.inherit('GroupInvitation', bo, {
    'study_group_id': fields.Integer(attribute='_study_group_id', description='Unique Id der Gruppe'),
    'source_user': fields.Integer(attribute='_source_user', description='Unique Id des Chatinhabers'),
    'target_user': fields.Integer(attribute='_target_user', description='Unique Id des Einzuladenden'),
    'is_accepted': fields.Boolean(attribute='_is_accepted', description='Akzeptiert')
})

learningprofilegroup = api.inherit('LearningProfileGroup', nbo, {
    'group_id': fields.Integer(attribute='_group_id', description='group_id'),
    'frequency': fields.Integer(attribute='_frequency', description='Häufigkeit'),
    'study_state': fields.Integer(attribute='_study_state', description='on oder offline'),
    'extroversion': fields.Integer(attribute='_extroversion', description='extrovertiertheit'),
    'prev_knowledge': fields.Integer(attribute='_study_group_id', description='bisherige Kentnisse'),
    'lerntyp': fields.Integer(attribute='_lerntyp', description='Lerntypdes Profilinhabers'),
    'interest': fields.String(attribute='_interest', description='Interessen des Profilinhabers'),
    'semester': fields.Integer(attribute='_semester', description='Semester'),
    'degree_course': fields.String(attribute='_degree_course', description='Studiengang'),

})

learningprofileuser = api.inherit('LearningProfileUser', nbo, {
    'user_id': fields.Integer(attribute='_user_id', description='user_id'),
    'frequency': fields.Integer(attribute='_frequency', description='Häufigkeit'),
    'study_state': fields.Integer(attribute='_study_state', description='on oder offline'),
    'extroversion': fields.Integer(attribute='_extroversion', description='extrovertiertheit'),
    'prev_knowledge': fields.Integer(attribute='_study_group_id', description='bisherige Kentnisse'),
    'lerntyp': fields.Integer(attribute='_lerntyp', description='Lerntypdes Profilinhabers'),
    'interest': fields.String(attribute='_interest', description='Interessen des Profilinhabers'),
    'semester': fields.Integer(attribute='_semester', description='Semester'),
    'degree_course': fields.String(attribute='_degree_course', description='Studiengang'),

})

studygroup = api.inherit('StudyGroup', nbo, {
    'learning_profile_id': fields.Integer(attribute='_learning_profile_id', description='FK Learningprofile id'),
    'chat_id': fields.Integer(attribute='_chat_id', description='Chat id ')

})

user = api.inherit('User', bo, {
    'google_id': fields.String(attribute='_google_id', description='Google Id des Profilinhabers'),
    'firstname': fields.String(attribute='_firstname', description='Vorname des Profilinhabers'),
    'lastname': fields.String(attribute='_lastname', description='Nachname des Profilinhabers'),
    'email': fields.String(attribute='_email', description='Email des Profilinhabers'),
    'adress': fields.String(attribute='_adress', description='Adresse des Profilinhabers')
})


# -----User-----

@studifix.route('/user')
@studifix.response(500, 'when server has problems')
class UserListOperations(Resource):
    """Reading out all user objects.
    If no user objects are available, an empty sequence is returned."""

    @studifix.marshal_list_with(user)
    def get(self):
        adm = Administration()
        users = adm.get_all_users()
        return users

    @studifix.marshal_with(user, code=200)
    @studifix.expect(user)  # We expect a user object from the client side.
    def post(self):
        """Create a new user object. We take the data sent by the client as a suggestion.
        For example, assigning the ID is not the responsibility of the client.
        Even if the client should assign an ID in the proposal, so
        it is up to the administration (business logic) to have a correct ID
        to forgive. * The corrected object will eventually be returned. *"""
        adm = Administration()
        prpl = User.from_dict(api.payload)
        """Check the references for valid values before using them."""
        if prpl is not None:
            """We only use the attributes of  user of the proposal for generation
            of a user object. The object created by the server is authoritative and
            is also returned to the client."""
            s = adm.create_user(prpl.get_google_id(), prpl.get_firstname(), prpl.get_lastname(),
                                prpl.get_email(), prpl.get_adress())

            return s, 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500


@studifix.route('/user/<int:id>')
@studifix.response(500, 'when server has problems')
class UserOperations(Resource):
    @studifix.marshal_with(user)
    def get(self, id):
        """reading out a specific userobject.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_user = adm.get_user_by_id(id)
        return single_user

    @studifix.marshal_with(user)
    @studifix.expect(user, validate=True)  # We expect a user object from the client side.
    def put(self, id):
        """ Update of a specific user object.
        The relevant id is the id provided by the URI and thus as a method parameter
        is used. This parameter overwrites the ID attribute of the transmitted in the payload of the request
        student object."""
        adm = Administration()
        user = User.from_dict(api.payload)
        print('main aufruf')

        if user is not None:
            """This sets the id of the user object to be overwritten (see update)."""
            user.set_id(id)
            adm.save_user(user)
            return '', 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500

    def delete(self, id):
        """Deletion of a specific user object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()
        single_user = adm.get_user_by_id(id)
        adm.delete_user(single_user)
        return '', 200


@studifix.route('/user/<string:lastname>')
@studifix.response(500, 'when server has problems')
class UserNameOperations(Resource):
    @studifix.marshal_with(user)
    def get(self, lastname):
        """Reading out user objects that are determined by the lastname.
        The objects to be read out are determined by '' name '' in the URI."""
        adm = Administration()
        user = adm.get_user_by_lastname(lastname)
        return user


@studifix.route('/user/<string:firstname>')
@studifix.response(500, 'when server has problems')
class UserFirstNameOperations(Resource):
    @studifix.marshal_with(user)
    def get(self, firstname):
        """Reading out user objects that are determined by the lastname.
        The objects to be read out are determined by '' name '' in the URI."""
        adm = Administration()
        user = adm.get_user_by_firstname(firstname)
        return user


@studifix.route('/user-by-mail/<string:email>')
@studifix.response(500, 'when server has problems')
class UserMailOperations(Resource):
    @studifix.marshal_with(user)
    def get(self, email):
        """Reading out user objects that are determined by the E-Mail.
        The objects to be read out are determined by '' mail '' in the URI."""
        adm = Administration()
        users = adm.get_user_by_email(email)
        return users


@studifix.route('/user-by-google-id/<string:google_id>')
@studifix.response(500, 'when server has problems')
class UserGoogleOperations(Resource):
    @studifix.marshal_with(user)
    def get(self, google_id):
        """Reading out user objects that are determined by the google id.
        The objects to be read out are determined by '' google_id '' in the URI."""
        adm = Administration()
        users = adm.get_user_by_google_id(google_id)
        return users


@studifix.route('/user-by-learning-profile-id/<int:learning_profile_id>')
@studifix.response(500, 'when server has problems')
class UserGoogleOperations(Resource):
    @studifix.marshal_with(user)
    def get(self, learning_profile_id):
        """Reading out user objects that are determined by the google id.
        The objects to be read out are determined by '' google_id '' in the URI."""
        adm = Administration()
        users = adm.get_user_by_learning_profile_id(learning_profile_id)
        return users


# ----ChatInvitation-----

@studifix.route('/chatinvitation')
@studifix.response(500, 'when server has problems')
class ChatInvitationListOperations(Resource):
    """Reading out all chatinvitation objects.
    If no user objects are available, an empty sequence is returned."""

    @studifix.marshal_list_with(chatinvitation)
    def get(self):
        adm = Administration()
        chatinvitations = adm.get_all_chatinvitations()
        return chatinvitations

    @studifix.marshal_with(chatinvitation, code=200)
    @studifix.expect(chatinvitation)  # We expect a user object from the client side.
    def post(self):
        """Create a new Chatinvitation object. We take the data sent by the client as a suggestion.
        For example, assigning the ID is not the responsibility of the client.
        Even if the client should assign an ID in the proposal, so
        it is up to the administration (business logic) to have a correct ID
        to forgive. * The corrected object will eventually be returned. *"""
        adm = Administration()
        prpl = ChatInvitation.from_dict(api.payload)
        """Check the references for valid values before using them."""
        if prpl is not None:
            """We only use the attributes of chatinvitation of the proposal for generation
            of a user object. The object created by the server is authoritative and
            is also returned to the client."""
            s = adm.create_chatinvitation(prpl.get_source_user(), prpl.get_target_user(), prpl.get_chat_id(),
                                          prpl.get_is_accepted())

            return s, 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500


@studifix.route('/chatinvitation/<int:id>')
@studifix.response(500, 'when server has problems')
class ChatInvitationOperations(Resource):
    @studifix.marshal_with(chatinvitation)
    def get(self, id):
        """reading out a specific chatinvitation object.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_chat_invitation = adm.get_chatinvitation_by_id(id)
        return single_chat_invitation

    def delete(self, id):
        """Deletion of a specific chatinvitation object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()
        single_chatinvitation = adm.delete_chatinvitation(id)
        adm.delete_chatinvitation(single_chatinvitation)
        return '', 200

    @studifix.marshal_with(chatinvitation)
    @studifix.expect(chatinvitation, validate=True)  # We expect a user object from the client side.
    def put(self, id):
        """ Update of a specific chatinvitation object.
        The relevant id is the id provided by the URI and thus as a method parameter
        is used. This parameter overwrites the ID attribute of the transmitted in the payload of the request
        student object."""
        adm = Administration()
        chatinvitation = ChatInvitation.from_dict(api.payload)
        print('main aufruf')

        if chatinvitation is not None:
            """This sets the id of the chatinvitation object to be overwritten (see update)."""
            chatinvitation.set_id(id)
            adm.save_chatinvitation(chatinvitation)
            return '', 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500


@studifix.route('/chatinvitation-by-target-user/<int:target_user>')
@studifix.response(500, 'when server has problems')
class ChatInvitationByTargetOperations(Resource):
    @studifix.marshal_list_with(chatinvitation)
    def get(self, target_user):
        """Reading out chatinvitation objects that are determined by the target user.
        The objects to be read out are determined by '' target_user'' in the URI."""
        adm = Administration()
        chatinvitation_target_user = adm.get_all_invites_by_target_user(target_user)
        return chatinvitation_target_user


@studifix.route('/chatinvitation-by-source-user/<int:source_user>')
@studifix.response(500, 'when server has problems')
class ChatInvitationBySourceOperations(Resource):
    @studifix.marshal_list_with(chatinvitation)
    def get(self, source_user):
        """Reading out chatinvitation objects that are determined by the source user.
        The objects to be read out are determined by '' source_user '' in the URI."""
        adm = Administration()
        chatinvitation_source_user = adm.get_all_invites_by_source_user(source_user)
        return chatinvitation_source_user


@studifix.route('/chatinvitation-accepted/<int:chat_id>')
@studifix.response(500, 'when server has problems')
class ChatInvitationsAcceptedOperations(Resource):
    @studifix.marshal_list_with(chatinvitation)
    def get(self, chat_id):
        """Reading out chatinvitations from the CHAT that are determined by the accepted Chatinvitations.
        The objects to be read out are determined by '' chat_id '' in the URI."""
        adm = Administration()
        chatinvitation_is_accepted = adm.get_all_accepted_user_in_chat(chat_id)
        return chatinvitation_is_accepted


@studifix.route('/chatinvitation-pend-invites/')
@studifix.response(500, 'when server has problems')
class ChatInvitationsPendInvitesOperations(Resource):
    @studifix.marshal_list_with(chatinvitation)
    def get(self):
        """Reading out all chatinvitation objects that are still pending."""
        adm = Administration()
        chatinvitation_pend_invites = adm.get_all_pend_invites()
        return chatinvitation_pend_invites


@studifix.route('/chatinvitation-pend-invites-target/<int:target_user>')
@studifix.response(500, 'when server has problems')
class ChatInvitationsPendInvitesByTargetUserOperations(Resource):
    @studifix.marshal_list_with(chatinvitation)
    def get(self, target_user):
        """Reading out chatinvitations objects that are pending determined by the target user.
        The objects to be read out are determined by '' target_user '' in the URI."""
        adm = Administration()
        chatinvitation_pend_invites_target_user = adm.get_pend_invites_by_target_user(target_user)
        return chatinvitation_pend_invites_target_user


@studifix.route('/chatinvitation-pend-invites-source/<int:source_user>')
@studifix.response(500, 'when server has problems')
class ChatInvitationsPendInvitesBySourceUserOperations(Resource):
    @studifix.marshal_list_with(chatinvitation)
    def get(self, source_user):
        """Reading out chatinvitations objects that are pending determined by the source user.
        The objects to be read out are determined by '' source_user '' in the URI."""
        adm = Administration()
        chatinvitation_pend_invites_source_user = adm.get_pend_invites_by_source_user(source_user)
        return chatinvitation_pend_invites_source_user


@studifix.route('/chatinvitation-accepted-invites-source/<int:source_user>')
@studifix.response(500, 'when server has problems')
class ChatInvitationsAcceptedInvitesBySourceUserOperations(Resource):
    @studifix.marshal_list_with(chatinvitation)
    def get(self, source_user):
        """Reading out chatinvitations objects that are accepted determined by the source_user.
        The objects to be read out are determined by '' source_user '' in the URI."""
        adm = Administration()
        chatinvitation_accepted_invites_source_user = adm.get_accepted_invites_by_source_user(source_user)
        return chatinvitation_accepted_invites_source_user


@studifix.route('/chatinvitation-accepted-invites-source/<int:target_user>')
@studifix.response(500, 'when server has problems')
class ChatInvitationsAcceptedInvitesByTargetUserOperations(Resource):
    @studifix.marshal_list_with(chatinvitation)
    def get(self, target_user):
        """Reading out chatinvitations objects that are accepted determined by the target user.
        The objects to be read out are determined by '' target_user '' in the URI."""
        adm = Administration()
        chatinvitation_accepted_invites_target_user = adm.get_accepted_invites_by_target_user(target_user)
        return chatinvitation_accepted_invites_target_user


# ---------Chatmessage--------

@studifix.route('/chatmessage')
@studifix.response(500, 'when server has problems')
class ChatMessageListOperations(Resource):
    """Reading out all chatmessage objects.
    If no user objects are available, an empty sequence is returned."""

    @studifix.marshal_list_with(chatmessage)
    def get(self):
        adm = Administration()
        chatmessages = adm.get_all_chatmessages()
        return chatmessages

    @studifix.marshal_with(chatmessage, code=200)
    @studifix.expect(chatmessage)  # We expect a user object from the client side.
    def post(self):
        """Create a new chatmessage object. We take the data sent by the client as a suggestion.
        For example, assigning the ID is not the responsibility of the client.
        Even if the client should assign an ID in the proposal, so
        it is up to the administration (business logic) to have a correct ID
        to forgive. * The corrected object will eventually be returned. *"""
        adm = Administration()
        prpl = ChatMessage.from_dict(api.payload)
        """Check the references for valid values before using them."""
        if prpl is not None:
            """We only use the attributes of chatmessage of the proposal for generation
            of a user object. The object created by the server is authoritative and
            is also returned to the client."""
            chatmessage = adm.create_chatmessage(prpl.get_chat_id(), prpl.get_user_id(), prpl.get_text())

            return chatmessage, 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500


@studifix.route('/chatmessage/<int:id>')
@studifix.response(500, 'when server has problems')
class ChatMessageOperations(Resource):
    @studifix.marshal_with(chatmessage)
    def get(self, id):
        """reading out a specific chatmessageobject.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_chatmessage = adm.get_chatmessage_by_id(id)
        return single_chatmessage

    @studifix.marshal_with(chatmessage)
    @studifix.expect(chatmessage, validate=True)  # We expect a chatmessage object from the client side.
    def put(self, id):
        """ Update of a specific chatmessage object.
        The relevant id is the id provided by the URI and thus as a method parameter
        is used. This parameter overwrites the ID attribute of the transmitted in the payload of the request
        student object."""
        adm = Administration()
        chatmessage = ChatMessage.from_dict(api.payload)
        print('main aufruf')

        if chatmessage is not None:
            """This sets the id of the chatmessage object to be overwritten (see update)."""
            chatmessage.set_id(id)
            adm.save_chatmessage(chatmessage)
            return '', 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500

    def delete(self, id):
        """Deletion of a specific chatmessage object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()
        single_chatmessage = adm.get_chatmessage_by_id(id)
        adm.delete_chatmessage(single_chatmessage)
        return '', 200


@studifix.route('/chatmessage-chat-id/<int:chat_id>')
@studifix.response(500, 'when server has problems')
class ChatMessageOperations(Resource):
    @studifix.marshal_list_with(chatmessage)
    def get(self, chat_id):
        """reading out a chatmessageobject by chat_id.
           The object to be read is determined by the '' chat_id '' in the URI."""
        adm = Administration()
        chatmessage_by_chat_id = adm.get_chatmessages_by_chat_id(chat_id)
        return chatmessage_by_chat_id


# -------Chat-------

@studifix.route('/chat')
@studifix.response(500, 'when server has problems')
class ChatListOperations(Resource):
    """Reading out all chat objects.
    If no user objects are available, an empty sequence is returned."""

    @studifix.marshal_list_with(chat)
    def get(self):
        adm = Administration()
        chats = adm.get_all_chats()
        return chats

    @studifix.marshal_with(chat, code=200)
    @studifix.expect(chat)  # We expect a user object from the client side.
    def post(self):
        """Create a new Chat object. We take the data sent by the client as a suggestion.
        For example, assigning the ID is not the responsibility of the client.
        Even if the client should assign an ID in the proposal, so
        it is up to the administration (business logic) to have a correct ID
        to forgive. * The corrected object will eventually be returned. *"""
        adm = Administration()
        prpl = Chat.from_dict(api.payload)
        """Check the references for valid values before using them."""
        if prpl is not None:
            """We only use the attributes of  of chat proposal for generation
            of a chat object. The object created by the server is authoritative and
            is also returned to the client."""
            c = adm.create_chat(prpl.get_name())
            return c, 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500


@studifix.route('/chat/<int:id>')
@studifix.response(500, 'when server has problems')
class ChatOperations(Resource):
    @studifix.marshal_with(chat)
    def get(self, id):
        """reading out a specific chatobject.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_chat = adm.get_chat_by_id(id)
        return single_chat

    @studifix.marshal_with(chat)
    @studifix.expect(chat, validate=True)  # We expect a user object from the client side.
    def put(self, id):
        """ Update of a specific chat object.
        The relevant id is the id provided by the URI and thus as a method parameter
        is used. This parameter overwrites the ID attribute of the transmitted in the payload of the request
        student object."""
        adm = Administration()
        chat = Chat.from_dict(api.payload)
        print('main aufruf')

        if chat is not None:
            """This sets the id of the chat object to be overwritten (see update)."""
            chat.set_id(id)
            adm.save_chat(chat)
            return '', 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500

    def delete(self, id):
        """Deletion of a specific chat object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()
        single_chat = adm.get_chat_by_id(id)
        adm.delete_chat(single_chat)
        return '', 200


# ----GroupInvitation--------

@studifix.route('/groupinvitation')
@studifix.response(500, 'when server has problems')
class GroupInvitationListOperations(Resource):
    """Reading out all groupinvitation objects.
    If no user objects are available, an empty sequence is returned."""

    @studifix.marshal_list_with(groupinvitation)
    def get(self):
        adm = Administration()
        groupinvitations = adm.get_all_groupinvitations()
        return groupinvitations

    @studifix.marshal_with(groupinvitation, code=200)
    @studifix.expect(groupinvitation)  # We expect a user object from the client side.
    def post(self):
        """Create a new groupinvitation object. We take the data sent by the client as a suggestion.
        For example, assigning the ID is not the responsibility of the client.
        Even if the client should assign an ID in the proposal, so
        it is up to the administration (business logic) to have a correct ID
        to forgive. * The corrected object will eventually be returned. *"""
        adm = Administration()
        prpl = GroupInvitation.from_dict(api.payload)
        """Check the references for valid values before using them."""
        if prpl is not None:
            """We only use the attributes of groupinvitation of the proposal for generation
            of a user object. The object created by the server is authoritative and
            is also returned to the client."""
            s = adm.create_groupinvitation(prpl.get_study_group_id(), prpl.get_source_user(), prpl.get_target_user())

            return s, 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500


@studifix.route('/groupinvitation/<int:id>')
@studifix.response(500, 'when server has problems')
class GroupInvitationOperations(Resource):
    @studifix.marshal_with(groupinvitation)
    def get(self, id):
        """reading out a specific groupinvitationobject.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_groupinvitation = adm.get_groupinvitation_by_id(id)
        return single_groupinvitation

    @studifix.marshal_with(groupinvitation)
    @studifix.expect(groupinvitation, validate=True)  # We expect a user object from the client side.
    def put(self, id):
        """ Update of a specific groupinvitation object.
        The relevant id is the id provided by the URI and thus as a method parameter
        is used. This parameter overwrites the ID attribute of the transmitted in the payload of the request
        student object."""
        adm = Administration()
        groupinvitation = GroupInvitation.from_dict(api.payload)
        print('main aufruf')

        if groupinvitation is not None:
            """This sets the id of the groupinvitation object to be overwritten (see update)."""
            groupinvitation.set_id(id)
            adm.save_groupinvitation(groupinvitation)
            return '', 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500

    def delete(self, id):
        """Deletion of a specific groupinvitation object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()
        single_groupinvitation = adm.get_user_by_id(id)
        adm.delete_groupinvitation(single_groupinvitation)
        return '', 200


@studifix.route('/groupinvitation-by-study-group/<int:study_group_id>')
@studifix.response(500, 'when server has problems')
class ChatInvitationByTargetOperations(Resource):
    @studifix.marshal_list_with(groupinvitation)
    def get(self, study_group_id):
        """Reading out groupinvitation objects that are determined by the study_group_id.
        The objects to be read out are determined by '' target_user'' in the URI."""
        adm = Administration()
        groupinvitation_by_study_group = adm.get_groupinvitation_by_study_group_id(study_group_id)
        return groupinvitation_by_study_group


@studifix.route('/groupinvitation-by-target-user/<int:target_user>')
@studifix.response(500, 'when server has problems')
class GroupInvitationByTargetOperations(Resource):
    @studifix.marshal_list_with(groupinvitation)
    def get(self, target_user):
        """Reading out groupinvitation objects that are determined by the target user.
        The objects to be read out are determined by '' target_user '' in the URI."""
        adm = Administration()
        groupinvitation_target_user = adm.get_groupinvitations_by_target_user(target_user)
        return groupinvitation_target_user


@studifix.route('/groupinvitation-by-source-user/<int:source_user>')
@studifix.response(500, 'when server has problems')
class GroupInvitationBySourceOperations(Resource):
    @studifix.marshal_list_with(groupinvitation)
    def get(self, source_user):
        """Reading out groupinvitation objects that are determined by the source user.
        The objects to be read out are determined by '' source_user '' in the URI."""
        adm = Administration()
        groupinvitation_source_user = adm.get_groupinvitations_by_source_user(source_user)
        return groupinvitation_source_user


@studifix.route('/groupinvitation-pend-invites/<int:study_group_id>')
@studifix.response(500, 'when server has problems')
class GroupInvitationsPendInvitesByStudyGroupOperations(Resource):
    @studifix.marshal_list_with(groupinvitation)
    def get(self, study_group_id):
        """Reading out all groupinvitation objects that are still pending by the study_group_id."""
        adm = Administration()
        groupinvitation_pend_invites_by_study_group = adm.get_groupinvitation_pend_invites_by_study_group(
            study_group_id)
        return groupinvitation_pend_invites_by_study_group


@studifix.route('/groupinvitation-accepted-by-study-group/<int:study_group_id>')
@studifix.response(500, 'when server has problems')
class GroupInvitationsAcceptedByStudyGroupOperations(Resource):
    @studifix.marshal_list_with(groupinvitation)
    def get(self, study_group_id):
        """Reading out chatinvitations from the CHAT that are determined by the accepted Chatinvitations.
        The objects to be read out are determined by '' chat_id '' in the URI."""
        adm = Administration()
        groupinvitation_is_accepted_by_study_group = adm.get_accepted_groupinvitation_by_study_group_id(study_group_id)
        return groupinvitation_is_accepted_by_study_group


@studifix.route('/groupinvitation-pend-invites-target/<int:target_user>')
@studifix.response(500, 'when server has problems')
class GroupInvitationsPendInvitesByTargetUserOperations(Resource):
    @studifix.marshal_list_with(groupinvitation)
    def get(self, target_user):
        """Reading out groupinvitations objects that are pending determined by the target user.
        The objects to be read out are determined by '' target_user '' in the URI."""
        adm = Administration()
        groupinvitation_pend_invites_target_user = adm.get_pend_invites_by_target_user(target_user)
        return groupinvitation_pend_invites_target_user


@studifix.route('/groupinvitation-pend-invites-source/<int:source_user>')
@studifix.response(500, 'when server has problems')
class GroupInvitationsPendInvitesBySourceUserOperations(Resource):
    @studifix.marshal_list_with(groupinvitation)
    def get(self, source_user):
        """Reading out chatinvitations objects that are pending determined by the source user.
        The objects to be read out are determined by '' source_user '' in the URI."""
        adm = Administration()
        groupinvitation_pend_invites_source_user = adm.get_pend_groupinvites_by_source_user(source_user)
        return groupinvitation_pend_invites_source_user


@studifix.route('/groupinvitation-accepted-invites-source/<int:source_user>')
@studifix.response(500, 'when server has problems')
class GroupInvitationsAcceptedInvitesBySourceUserOperations(Resource):
    @studifix.marshal_list_with(groupinvitation)
    def get(self, source_user):
        """Reading out groupinvitations objects that are accepted determined by the source_user.
        The objects to be read out are determined by '' source_user '' in the URI."""
        adm = Administration()
        groupinvitation_accepted_invites_source_user = adm.get_accepted_invites_by_source_user(source_user)
        return groupinvitation_accepted_invites_source_user


@studifix.route('/groupinvitation-accepted-invites-source/<int:target_user>')
@studifix.response(500, 'when server has problems')
class GroupInvitationsAcceptedInvitesByTargetUserOperations(Resource):
    @studifix.marshal_list_with(groupinvitation)
    def get(self, target_user):
        """Reading out groupinvitations objects that are accepted determined by the target user.
        The objects to be read out are determined by '' target_user '' in the URI."""
        adm = Administration()
        groupinvitation_accepted_invites_target_user = adm.get_accepted_invites_by_target_user(target_user)
        return groupinvitation_accepted_invites_target_user


@studifix.route('/groupinvitation-pend-invites/')
@studifix.response(500, 'when server has problems')
class GroupInvitationsPendInvitesOperations(Resource):
    @studifix.marshal_list_with(groupinvitation)
    def get(self):
        """Reading out all groupinvitation objects that are still pending."""
        adm = Administration()
        groupinvitation_pend_invites = adm.get_all_pend_invites()
        return groupinvitation_pend_invites


# -----StudyGroup---------

@studifix.route('/studygroup')
@studifix.response(500, 'when server has problems')
class StudyGroupListOperations(Resource):
    """Reading out all studygroup objects.
    If no user objects are available, an empty sequence is returned."""

    @studifix.marshal_list_with(studygroup)
    def get(self):
        adm = Administration()
        studygroups = adm.get_all_studygroups()
        return studygroups

    @studifix.marshal_with(studygroup, code=200)
    @studifix.expect(studygroup)  # We expect a user object from the client side.
    def post(self):
        """Create a new studygroup object. We take the data sent by the client as a suggestion.
        For example, assigning the ID is not the responsibility of the client.
        Even if the client should assign an ID in the proposal, so
        it is up to the administration (business logic) to have a correct ID
        to forgive. * The corrected object will eventually be returned. *"""
        adm = Administration()
        prpl = StudyGroup.from_dict(api.payload)
        """Check the references for valid values before using them."""
        if prpl is not None:
            """We only use the attributes of studygroup of the proposal for generation
            of a user object. The object created by the server is authoritative and
            is also returned to the client."""
            s = adm.create_studygroup(prpl.get_chat_id(), prpl.get_learning_profile_id())

            return s, 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500


@studifix.route('/studygroup/<int:id>')
@studifix.response(500, 'when server has problems')
class StudyGroupOperations(Resource):
    @studifix.marshal_with(user)
    def get(self, id):
        """reading out a specific studygroupobject.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_studygroup = adm.get_studygroup_by_id(id)
        return single_studygroup

    @studifix.marshal_with(studygroup)
    @studifix.expect(studygroup, validate=True)  # We expect a user object from the client side.
    def put(self, id):
        """ Update of a specific studygroup object.
        The relevant id is the id provided by the URI and thus as a method parameter
        is used. This parameter overwrites the ID attribute of the transmitted in the payload of the request
        student object."""
        adm = Administration()
        studygroup = StudyGroup.from_dict(api.payload)
        print('main aufruf')

        if studygroup is not None:
            """This sets the id of the studygroup object to be overwritten (see update)."""
            studygroup.set_id(id)
            adm.save_studygroup(studygroup)
            return '', 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500

    def delete(self, id):
        """Deletion of a specific studygroup object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()
        single_studygroup = adm.get_studygroup_by_id(id)
        adm.delete_studygroup(single_studygroup)
        return '', 200


@studifix.route('/studygroup/<string:name>')
@studifix.response(500, 'when server has problems')
class StudyGroupOperations(Resource):
    @studifix.marshal_with(studygroup)
    def get(self, name):
        """Reading out studygroup objects that are determined by the lastname.
        The objects to be read out are determined by '' name '' in the URI."""
        adm = Administration()
        studygroup = adm.get_studygroup_by_name(name)
        return studygroup


@studifix.route('/studygroup-by-learning-profile/<int:learning_profile_id>')
@studifix.response(500, 'when server has problems')
class StudyGroupLearningProfileOperations(Resource):
    @studifix.marshal_with(studygroup)
    def get(self, learning_profile):
        """Reading out studygroup objects that are determined by the lastname.
        The objects to be read out are determined by '' name '' in the URI."""
        adm = Administration()
        studygroup = adm.get_studygroup_by_learning_profile_id(learning_profile)
        return studygroup


# -------LearningProfileGroup---------


@studifix.route('/learningprofilegroup')
@studifix.response(500, 'when server has problems')
class LearningProfileGroupListOperations(Resource):
    """Reading out all learninprofile group objects.
    If no user objects are available, an empty sequence is returned."""

    @studifix.marshal_list_with(learningprofilegroup)
    def get(self):
        adm = Administration()
        learningprofiles = adm.get_all_learningprofiles_group()
        return learningprofiles

    @studifix.marshal_with(learningprofilegroup, code=200)
    @studifix.expect(learningprofilegroup)  # We expect a user object from the client side.
    def post(self):
        """Create a new learningprofile group object. We take the data sent by the client as a suggestion.
        For example, assigning the ID is not the responsibility of the client.
        Even if the client should assign an ID in the proposal, so
        it is up to the administration (business logic) to have a correct ID
        to forgive. * The corrected object will eventually be returned. *"""
        adm = Administration()
        prpl = LearningProfileGroup.from_dict(api.payload)
        """Check the references for valid values before using them."""
        if prpl is not None:
            """We only use the attributes of student of the proposal for generation
            of a learninprofile object. The object created by the server is authoritative and
            is also returned to the client."""
            s = adm.create_learningprofile_group(prpl.get_group_id(), prpl.get_frequency(), prpl.get_study_state(),
                                                 prpl.get_extroversion(),
                                                 prpl.get_prev_knowledge(),
                                                 prpl.get_learntyp(), prpl.get_interest(), prpl.get_semester(),
                                                 prpl.get_degree_course())

            return s, 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500


@studifix.route('/learningprofilegroup/<int:id>')
@studifix.response(500, 'when server has problems')
class LearningProfileGroupOperations(Resource):
    @studifix.marshal_with(learningprofilegroup)
    def get(self, id):
        """reading out a specific learninprofileobject.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_learningprofile = adm.get_learningprofile_group_by_id(id)
        return single_learningprofile

    @studifix.marshal_with(learningprofilegroup)
    @studifix.expect(learningprofilegroup, validate=True)  # We expect a learningprofile object from the client side.
    def put(self, id):
        """ Update of a specific learninprofile object.
        The relevant id is the id provided by the URI and thus as a method parameter
        is used. This parameter overwrites the ID attribute of the transmitted in the payload of the request
        student object."""
        adm = Administration()
        learningprofile = LearningProfileGroup.from_dict(api.payload)
        print('main aufruf')

        if learningprofile is not None:
            """This sets the id of the learninprofile object to be overwritten (see update)."""
            learningprofile.set_id(id)
            adm.save_learningprofile_group(learningprofile)
            return '', 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500

    def delete(self, id):
        """Deletion of a specific learninprofile object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()
        single_learningprofile = adm.get_learningprofile_group_by_id(id)
        adm.delete_learningprofile_group(single_learningprofile)
        return '', 200


@studifix.route('/learningprofilegroup-by-name/<string:name>')
@studifix.response(500, 'when server has problems')
class LearningProfileGroupByNameOperations(Resource):
    @studifix.marshal_with(learningprofilegroup)
    def get(self, name):
        """Reading out studygroup objects that are determined by the lastname.
        The objects to be read out are determined by '' name '' in the URI."""
        adm = Administration()
        learning_profile_by_name = adm.get_learningprofile_group_by_name(name)
        return learning_profile_by_name


# -------LearningProfileUser---------


@studifix.route('/learningprofileuser')
@studifix.response(500, 'when server has problems')
class LearningProfileUserListOperations(Resource):
    """Reading out all learninprofile user objects.
    If no user objects are available, an empty sequence is returned."""

    @studifix.marshal_list_with(learningprofileuser)
    def get(self):
        adm = Administration()
        learningprofiles = adm.get_all_learningprofiles_user()
        return learningprofiles

    @studifix.marshal_with(learningprofileuser, code=200)
    @studifix.expect(learningprofileuser)  # We expect a user object from the client side.
    def post(self):
        """Create a new learningprofile user object. We take the data sent by the client as a suggestion.
        For example, assigning the ID is not the responsibility of the client.
        Even if the client should assign an ID in the proposal, so
        it is up to the administration (business logic) to have a correct ID
        to forgive. * The corrected object will eventually be returned. *"""
        adm = Administration()
        prpl = LearningProfileUser.from_dict(api.payload)
        """Check the references for valid values before using them."""
        if prpl is not None:
            """We only use the attributes of student of the proposal for generation
            of a learninprofile object. The object created by the server is authoritative and
            is also returned to the client."""
            s = adm.create_learningprofile_user(prpl.get_user_id(), prpl.get_frequency(), prpl.get_study_state(),
                                                prpl.get_extroversion(),
                                                prpl.get_prev_knowledge(),
                                                prpl.get_learntyp(), prpl.get_interest(), prpl.get_semester(),
                                                prpl.get_degree_course())

            return s, 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500


@studifix.route('/learningprofileuser/<int:id>')
@studifix.response(500, 'when server has problems')
class LearningProfileUserOperations(Resource):
    @studifix.marshal_with(learningprofileuser)
    def get(self, id):
        """reading out a specific learninprofileobject.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_learningprofile = adm.get_learningprofile_user_by_id(id)
        return single_learningprofile

    @studifix.marshal_with(learningprofileuser)
    @studifix.expect(learningprofileuser, validate=True)  # We expect a learningprofile object from the client side.
    def put(self, id):
        """ Update of a specific learninprofile object.
        The relevant id is the id provided by the URI and thus as a method parameter
        is used. This parameter overwrites the ID attribute of the transmitted in the payload of the request
        student object."""
        adm = Administration()
        learningprofile = LearningProfileUser.from_dict(api.payload)
        print('main aufruf')

        if learningprofile is not None:
            """This sets the id of the learninprofile object to be overwritten (see update)."""
            learningprofile.set_id(id)
            adm.save_learningprofile_user(learningprofile)
            return '', 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500

    def delete(self, id):
        """Deletion of a specific learninprofile object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()
        single_learningprofile = adm.get_learningprofile_user_by_id(id)
        adm.delete_learningprofile_user(single_learningprofile)
        return '', 200


@studifix.route('/learningprofileuser-by-name/<string:name>')
@studifix.response(500, 'when server has problems')
class LearningProfileGroupByNameOperations(Resource):
    @studifix.marshal_with(learningprofilegroup)
    def get(self, name):
        """Reading out studygroup objects that are determined by the lastname.
        The objects to be read out are determined by '' name '' in the URI."""
        adm = Administration()
        learning_profile_by_name = adm.get_learningprofile_user_by_name(name)
        return learning_profile_by_name


"""
Nachdem wir nun sämtliche Resourcen definiert haben, die wir via REST bereitstellen möchten,
müssen nun die App auch tatsächlich zu starten.

Diese Zeile ist leider nicht Teil der Flask-Doku! In jener Doku wird von einem Start via Kommandozeile ausgegangen.
Dies ist jedoch für uns in der Entwicklungsumgebung wenig komfortabel. Deshlab kommt es also schließlich zu den 
folgenden Zeilen. 

**ACHTUNG:** Diese Zeile wird nur in der lokalen Entwicklungsumgebung ausgeführt und hat in der Cloud keine Wirkung!
"""
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
# Auf Flask aufbauend nutzen wir RestX
from flask_restx import Api, Resource, fields
# Wir benutzen noch eine Flask-Erweiterung für Cross-Origin Resource Sharing
from flask_cors import CORS

from src.server.Administration import Administration
from src.server.bo.ChatInvitation import ChatInvitation

from src.server.bo.ChatMessage import ChatMessage
from src.server.bo.LearningProfile import LearningProfile
from src.server.bo.GroupInvitation import GroupInvitation
from src.server.bo.LearningprofileGroup import LearningProfileGroup
from src.server.bo.LearningProfileUser import LearningProfileUser
from src.server.bo.StudyGroup import StudyGroup
from src.server.bo.User import User
from src.server.bo.Chat import Chat

from src.SecurityDecorator import secured

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
                                wird in dieser Fallstudye auch aus Gründen einer
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

CORS(app, resources=r'/studyfix/*')



"""
Alle Ressourcen mit dem Präfix /studyfix für **Cross-Origin Resource Sharing** (CORS) freigeben.
Diese eine Zeile setzt die Installation des Package flask-cors voraus. 
"""

"""
In dem folgenden Abschnitt bauen wir ein Modell auf, das die Datenstruktur beschreibt, 
auf deren Basis Clients und Server Daten austauschen. Grundlage hierfür ist das Package flask-restx.
"""
api = Api(app, version='1.0', title='studyFix API',
          description='Eine App zum auffinden von Lernpartnern und Lerngruppen.')

"""Anlegen eines Namespace
Namespaces erlauben uns die Strukturierung von APIs. In diesem Fall fasst dieser Namespace alle
studyFix-relevanten Operationen unter dem Präfix /bank zusammen. Eine alternative bzw. ergänzende Nutzung
von Namespace könnte etwa sein, unterschiedliche API-Version voneinander zu trennen, um etwa 
Abwärtskompatibilität (vgl. Lehrveranstaltungen zu Software Engineering) zu gewährleisten. Dies ließe
sich z.B. umsetzen durch /bank/v1, /bank/v2 usw."""

studyfix = api.namespace('studyfix', description='Funktionen des studyFix')



bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Unique id of a business object'),
    'creation_date': fields.DateTime(attribute='_creation_date', description='creation date of a business object',
                                     dt_format='iso8601')
})

nbo = api.inherit('NamedBusinessObject', bo, {
    'name': fields.String(attribute='_name', description='name of a named business object')
})


chat = api.inherit('Chat', nbo,{

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
    'target_user': fields.Integer(attribute='_target_user', description='Unique Id des Einzuladenden'),
    'source_user': fields.Integer(attribute='_source_user', description='Unique Id des Chatinhabers'),
    'study_group_id': fields.Integer(attribute='_study_group_id', description='Unique Id der Gruppe'),
    'is_accepted': fields.Boolean(attribute='_is_accepted', description='Akzeptiert')
})

learningprofile = api.inherit('LearningProfile', nbo, {
    'prev_knowledge': fields.Integer(attribute='_prev_knowledge', description='bisherige Kentnisse'),
    'extroversion': fields.Integer(attribute='_extroversion', description='extrovertiertheit'),
    'study_state': fields.Integer(attribute='_study_state', description='on oder offline'),
    'frequency': fields.Integer(attribute='_frequency', description='Häufigkeit'),
    'learntyp': fields.Integer(attribute='_learntyp', description='Learntyp des Profilinhabers'),
    'semester': fields.Integer(attribute='_semester', description='Semester'),
    'interest': fields.String(attribute='_interest', description='Interessen des Profilinhabers'),
    'degree_course': fields.String(attribute='_degree_course', description='studyengang')
})

learningprofilegroup = api.inherit('LearningProfileGroup', learningprofile, {
    'group_id': fields.Integer(attribute='_group_id', description='group_id')

})

learningprofileuser = api.inherit('LearningProfileUser', learningprofile, {
    'user_id': fields.Integer(attribute='_user_id', description='user_id')
})

studygroup = api.inherit('StudyGroup', nbo, {
    'chat_id':fields.Integer(attribute='_chat_id', description='Chat id ')
})

user = api.inherit('User', bo, {
    'google_id': fields.String(attribute='_google_id', description='Google Id des Profilinhabers'),
    'firstname': fields.String(attribute='_firstname', description='Vorname des Profilinhabers'),
    'lastname': fields.String(attribute='_lastname', description='Nachname des Profilinhabers'),
    'email': fields.String(attribute='_email', description='Email des Profilinhabers'),
    'adress': fields.String(attribute='_adress', description='Adresse des Profilinhabers')
})

# -----User-----


@studyfix.route('/user')
@studyfix.response(500, 'when server has problems')
class UserListOperations(Resource):
    """Reading out all user objects.
    If no user objects are available, an empty sequence is returned."""

    @studyfix.marshal_list_with(user)
    @secured
    def get(self):
        adm = Administration()
        users = adm.get_all_users()
        return users

    @studyfix.marshal_with(user, code=200)
    @studyfix.expect(user)  # We expect a user object from the client side.
    @secured
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


@studyfix.route('/user/<int:id>')
@studyfix.response(500, 'when server has problems')
class UserOperations(Resource):
    @studyfix.marshal_with(user)
    @secured
    @secured
    def get(self, id):
        """reading out a specific userobject.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_user = adm.get_user_by_id(id)
        return single_user

    @studyfix.marshal_with(user)
    @studyfix.expect(user, validate=True)  # We expect a user object from the client side.
    @secured
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

    @secured
    def delete(self, id):
        """Deletion of a specific user object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()
        single_user = adm.get_user_by_id(id)
        adm.delete_user(single_user)
        return '', 200


@studyfix.route('/user-by-lastname/<string:lastname>')
@studyfix.response(500, 'when server has problems')
class UserNameOperations(Resource):
    @studyfix.marshal_list_with(user)
    @secured
    def get(self, lastname):
        """Reading out user objects that are determined by the lastname.
        The objects to be read out are determined by '' name '' in the URI."""
        adm = Administration()
        user = adm.get_user_by_lastname(lastname)
        return user


@studyfix.route('/user-by-firstname/<string:firstname>')
@studyfix.response(500, 'when server has problems')
class UserFirstNameOperations(Resource):
    @studyfix.marshal_with(user)
    @secured
    def get(self, firstname):
        """Reading out user objects that are determined by the lastname.
        The objects to be read out are determined by '' name '' in the URI."""
        adm = Administration()
        user = adm.get_user_by_firstname(firstname)
        return user


@studyfix.route('/user-by-mail/<string:email>')
@studyfix.response(500, 'when server has problems')
class UserMailOperations(Resource):
    @studyfix.marshal_list_with(user)
    @secured
    def get(self, email):
        """Reading out user objects that are determined by the E-Mail.
        The objects to be read out are determined by '' mail '' in the URI."""
        adm = Administration()
        users = adm.get_user_by_email(email)
        return users


@studyfix.route('/user-by-google-id/<string:google_id>')
@studyfix.response(500, 'when server has problems')
class UserGoogleOperations(Resource):
    @studyfix.marshal_with(user)
    @secured
    def get(self, google_id):
        """Reading out user objects that are determined by the google id.
        The objects to be read out are determined by '' google_id '' in the URI."""
        adm = Administration()
        users = adm.get_user_by_google_id(google_id)
        return users


@studyfix.route('/user-by-learning-profile-id/<int:learning_profile_id>')
@studyfix.response(500, 'when server has problems')
class UserGoogleOperations(Resource):
    @studyfix.marshal_with(user)
    @secured
    def get(self, learning_profile_id):
        """Reading out user objects that are determined by the google id.
        The objects to be read out are determined by '' google_id '' in the URI."""
        adm = Administration()
        users = adm.get_user_by_learning_profile_id(learning_profile_id)
        return users


# ----ChatInvitation-----


@studyfix.route('/chatinvitation')
@studyfix.response(500, 'when server has problems')
class ChatInvitationListOperations(Resource):
    """Reading out all chatinvitation objects.
    If no user objects are available, an empty sequence is returned."""

    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self):
        adm = Administration()
        chatinvitations = adm.get_all_chatinvitations()
        return chatinvitations

    @studyfix.marshal_with(chatinvitation, code=200)
    @studyfix.expect(chatinvitation)  # We expect a user object from the client side.

    def post(self):
        """Create a new Chatinvitation object. We take the data sent by the client as a suggestion.
        For example, assigning the ID is not the responsibility of the client.
        Even if the client should assign an ID in the proposal, so
        it is up to the administration (business logic) to have a correct ID
        to forgive. * The corrected object will eventually be returned. *"""
        adm = Administration()
        print(api.payload)
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


@studyfix.route('/chatinvitation/<int:id>')
@studyfix.response(500, 'when server has problems')
class ChatInvitationOperations(Resource):
    @studyfix.marshal_with(chatinvitation)
    @secured
    def get(self, id):
        """reading out a specific chatinvitation object.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_chat_invitation = adm.get_chatinvitation_by_id(id)
        return single_chat_invitation

    @secured
    def delete(self, id):
        """Deletion of a specific chatinvitation object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()
        chat_invitation = adm.get_chatinvitation_by_id(id)

        if chat_invitation is not None:
            adm.delete_chatinvitation(chat_invitation)
            return '', 200
        else:
            return '', 500



    @studyfix.marshal_with(chatinvitation)
    @studyfix.expect(chatinvitation, validate=True)  # We expect a user object from the client side.
    @secured
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


@studyfix.route('/chatinvitation-by-target-user/<int:target_user>')
@studyfix.response(500, 'when server has problems')
class ChatInvitationByTargetOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self, target_user):
        """Reading out chatinvitation objects that are determined by the target user.
        The objects to be read out are determined by '' target_user'' in the URI."""
        adm = Administration()
        chatinvitation_target_user = adm.get_all_invites_by_target_user(target_user)
        return chatinvitation_target_user


@studyfix.route('/chatinvitation-by-source-user/<int:source_user>')
@studyfix.response(500, 'when server has problems')
class ChatInvitationBySourceOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self, source_user):
        """Reading out chatinvitation objects that are determined by the source user.
        The objects to be read out are determined by '' source_user '' in the URI."""
        adm = Administration()
        chatinvitation_source_user = adm.get_all_invites_by_source_user(source_user)
        return chatinvitation_source_user


@studyfix.route('/chatinvitation-accepted-by-chat/<int:chat_id>')
@studyfix.response(500, 'when server has problems')
class ChatInvitationsAcceptedOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self, chat_id):
        """Reading out chatinvitations from the CHAT that are determined by the accepted Chatinvitations.
        The objects to be read out are determined by '' chat_id '' in the URI."""
        adm = Administration()
        chatinvitation_is_accepted = adm.get_all_accepted_user_in_chat(chat_id)
        return chatinvitation_is_accepted


@studyfix.route('/chatinvitation-pend-invites')
@studyfix.response(500, 'when server has problems')
class ChatInvitationsPendInvitesOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self):
        """Reading out all chatinvitation objects that are still pending."""
        adm = Administration()
        chatinvitation_pend_invites = adm.get_all_pend_invites()
        return chatinvitation_pend_invites


@studyfix.route('/chatinvitation-pend-invites-target/<int:target_user>')
@studyfix.response(500, 'when server has problems')
class ChatInvitationsPendInvitesByTargetUserOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self, target_user):
        """Reading out chatinvitations objects that are pending determined by the target user.
        The objects to be read out are determined by '' target_user '' in the URI."""
        adm = Administration()
        chatinvitation_pend_invites_target_user = adm.get_pend_invites_by_target_user(target_user)
        return chatinvitation_pend_invites_target_user


@studyfix.route('/chatinvitation-pend-invites-source/<int:source_user>')
@studyfix.response(500, 'when server has problems')
class ChatInvitationsPendInvitesBySourceUserOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self, source_user):
        """Reading out chatinvitations objects that are pending determined by the source user.
        The objects to be read out are determined by '' source_user '' in the URI."""
        adm = Administration()
        chatinvitation_pend_invites_source_user = adm.get_pend_invites_by_source_user(source_user)
        return chatinvitation_pend_invites_source_user


@studyfix.route('/chatinvitation-accepted-invites-source/<int:source_user>')
@studyfix.response(500, 'when server has problems')
class ChatInvitationsAcceptedInvitesBySourceUserOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self, source_user):
        """Reading out chatinvitations objects that are accepted determined by the source_user.
        The objects to be read out are determined by '' source_user '' in the URI."""
        adm = Administration()
        chatinvitation_accepted_invites_source_user = adm.get_accepted_invites_by_source_user(source_user)
        return chatinvitation_accepted_invites_source_user


@studyfix.route('/chatinvitation-accepted-invites-target/<int:target_user>')
@studyfix.response(500, 'when server has problems')
class ChatInvitationsAcceptedInvitesByTargetUserOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self, target_user):
        """Reading out chatinvitations objects that are accepted determined by the target user.
        The objects to be read out are determined by '' target_user '' in the URI."""
        adm = Administration()
        chatinvitation_accepted_invites_target_user = adm.get_accepted_invites_by_target_user(target_user)
        return chatinvitation_accepted_invites_target_user



# ---------Chatmessage--------


@studyfix.route('/chatmessage')
@studyfix.response(500, 'when server has problems')
class ChatMessageListOperations(Resource):
    """Reading out all chatmessage objects.
    If no user objects are available, an empty sequence is returned."""

    @studyfix.marshal_list_with(chatmessage)
    @secured
    def get(self):
        adm = Administration()
        chatmessages = adm.get_all_chatmessages()
        return chatmessages

    @studyfix.marshal_with(chatmessage, code=200)
    @studyfix.expect(chatmessage)  # We expect a user object from the client side
    @secured
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


@studyfix.route('/chatmessage/<int:id>')
@studyfix.response(500, 'when server has problems')
class ChatMessageOperations(Resource):
    @studyfix.marshal_with(chatmessage)
    @secured
    def get(self, id):
        """reading out a specific chatmessageobject.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_chatmessage = adm.get_chatmessage_by_id(id)
        return single_chatmessage

    @studyfix.marshal_with(chatmessage)
    @studyfix.expect(chatmessage, validate=True)  # We expect a chatmessage object from the client side.
    @secured
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

    @secured
    def delete(self, id):
        """Deletion of a specific chatmessage object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()
        single_chatmessage = adm.get_chatmessage_by_id(id)
        adm.delete_chatmessage(single_chatmessage)
        return '', 200


@studyfix.route('/chatmessage-chat-id/<int:chat_id>')
@studyfix.response(500, 'when server has problems')
class ChatMessageOperations(Resource):
    @studyfix.marshal_list_with(chatmessage)
    @secured
    def get(self, chat_id):
        """reading out a chatmessageobject by chat_id.
           The object to be read is determined by the '' chat_id '' in the URI."""
        adm = Administration()
        chatmessage_by_chat_id = adm.get_chatmessages_by_chat_id(chat_id)
        return chatmessage_by_chat_id


# -------Chat-------


@studyfix.route('/chat')
@studyfix.response(500, 'when server has problems')
class ChatListOperations(Resource):
    """Reading out all chat objects.
    If no user objects are available, an empty sequence is returned."""

    @studyfix.marshal_list_with(chat)
    @secured
    def get(self):
        adm = Administration()
        chats = adm.get_all_chats()
        return chats


    @studyfix.marshal_with(chat, code=200)
    @studyfix.expect(chat)  # We expect a user object from the client side.
    @secured
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


@studyfix.route('/chat/<int:id>')
@studyfix.response(500, 'when server has problems')
class ChatOperations(Resource):
    @studyfix.marshal_with(chat)
    @secured
    def get(self, id):
        """reading out a specific chatobject.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_chat = adm.get_chat_by_id(id)
        return single_chat

    @secured
    def delete(self, id):
        """Deletion of a specific chat object.
        The object to be deleted is determined by the '' id '' in the URI."""

        adm = Administration()
        chat = adm.get_chat_by_id(id)

        if chat is not None:
            adm.delete_chat(chat)
            return '', 200
        else:
            return '', 500

    @studyfix.marshal_with(chat)
    @studyfix.expect(chat, validate=True)  # We expect a user object from the client side.
    @secured
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




# ----GroupInvitation----



@studyfix.route('/groupinvitation')
@studyfix.response(500, 'when server has problems')
class GroupInvitationListOperations(Resource):
    """Reading out all groupinvitation objects.
    If no user objects are available, an empty sequence is returned."""

    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self):
        adm = Administration()
        groupinvitations = adm.get_all_groupinvitations()
        return groupinvitations

    @studyfix.marshal_with(groupinvitation, code=200)
    @studyfix.expect(groupinvitation)  # We expect a user object from the client side.
    
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
            s = adm.create_groupinvitation(prpl.get_source_user(), prpl.get_target_user(), prpl.get_study_group_id(),
                                          prpl.get_is_accepted())


            return s, 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500


@studyfix.route('/groupinvitation/<int:id>')
@studyfix.response(500, 'when server has problems')
class GroupInvitationOperations(Resource):
    @studyfix.marshal_with(groupinvitation)
    @secured
    def get(self, id):
        """reading out a specific groupinvitationobject.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_groupinvitation = adm.get_groupinvitation_by_id(id)
        return single_groupinvitation

    @studyfix.marshal_with(groupinvitation)
    @studyfix.expect(groupinvitation, validate=True)  # We expect a user object from the client side.
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

    @secured
    def delete(self, id):
        """Deletion of a specific groupinvitation object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()
        single_groupinvitation = adm.get_user_by_id(id)
        adm.delete_groupinvitation(single_groupinvitation)
        return '', 200


@studyfix.route('/groupinvitation-by-study-group/<int:study_group_id>')
@studyfix.response(500, 'when server has problems')
class GroupinvitationByTargetOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, study_group_id):
        """Reading out groupinvitation objects that are determined by the study_group_id.
        The objects to be read out are determined by '' target_user'' in the URI."""
        adm = Administration()
        groupinvitation_by_study_group = adm.get_groupinvitation_by_study_group_id(study_group_id)
        return groupinvitation_by_study_group


@studyfix.route('/groupinvitation-by-target-user/<int:target_user>')
@studyfix.response(500, 'when server has problems')
class GroupInvitationByTargetOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, target_user):
        """Reading out groupinvitation objects that are determined by the target user.
        The objects to be read out are determined by '' target_user '' in the URI."""
        adm = Administration()
        groupinvitation_target_user = adm.get_groupinvitations_by_target_user(target_user)
        return groupinvitation_target_user


@studyfix.route('/groupinvitation-by-source-user/<int:source_user>')
@studyfix.response(500, 'when server has problems')
class GroupInvitationBySourceOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, source_user):
        """Reading out groupinvitation objects that are determined by the source user.
        The objects to be read out are determined by '' source_user '' in the URI."""
        adm = Administration()
        groupinvitation_source_user = adm.get_groupinvitations_by_source_user(source_user)
        return groupinvitation_source_user


@studyfix.route('/groupinvitation-pend-invites/<int:study_group_id>')
@studyfix.response(500, 'when server has problems')
class GroupInvitationsPendInvitesByStudyGroupOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, study_group_id):
        """Reading out all groupinvitation objects that are still pending by the study_group_id."""
        adm = Administration()
        groupinvitation_pend_invites_by_study_group = adm.get_groupinvitation_pend_invites_by_study_group(
            study_group_id)
        return groupinvitation_pend_invites_by_study_group


@studyfix.route('/groupinvitation-accepted-by-study-group/<int:study_group_id>')
@studyfix.response(500, 'when server has problems')
class GroupInvitationsAcceptedByStudyGroupOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, study_group_id):
        """Reading out chatinvitations from the CHAT that are determined by the accepted Chatinvitations.
        The objects to be read out are determined by '' chat_id '' in the URI."""
        adm = Administration()
        groupinvitation_is_accepted_by_study_group = adm.get_accepted_groupinvitation_by_study_group_id(study_group_id)
        return groupinvitation_is_accepted_by_study_group


@studyfix.route('/groupinvitation-pend-invites-target/<int:target_user>')
@studyfix.response(500, 'when server has problems')
class GroupInvitationsPendInvitesByTargetUserOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, target_user):
        """Reading out groupinvitations objects that are pending determined by the target user.
        The objects to be read out are determined by '' target_user '' in the URI."""
        adm = Administration()
        groupinvitation_pend_invites_target_user = adm.get_pend_invites_by_target_user(target_user)
        return groupinvitation_pend_invites_target_user


@studyfix.route('/groupinvitation-pend-invites-source/<int:source_user>')
@studyfix.response(500, 'when server has problems')
class GroupInvitationsPendInvitesBySourceUserOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, source_user):
        """Reading out chatinvitations objects that are pending determined by the source user.
        The objects to be read out are determined by '' source_user '' in the URI."""
        adm = Administration()
        groupinvitation_pend_invites_source_user = adm.get_pend_groupinvites_by_source_user(source_user)
        return groupinvitation_pend_invites_source_user


@studyfix.route('/groupinvitation-accepted-invites-source/<int:source_user>')
@studyfix.response(500, 'when server has problems')
class GroupInvitationsAcceptedInvitesBySourceUserOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, source_user):
        """Reading out groupinvitations objects that are accepted determined by the source_user.
        The objects to be read out are determined by '' source_user '' in the URI."""
        adm = Administration()
        groupinvitation_accepted_invites_source_user = adm.get_accepted_invites_by_source_user(source_user)
        return groupinvitation_accepted_invites_source_user


@studyfix.route('/groupinvitation-accepted-invites-target/<int:target_user>')
@studyfix.response(500, 'when server has problems')
class GroupInvitationsAcceptedInvitesByTargetUserOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, target_user):
        """Reading out groupinvitations objects that are accepted determined by the target user.
        The objects to be read out are determined by '' target_user '' in the URI."""
        adm = Administration()
        groupinvitation_accepted_invites_target_user = adm.get_accepted_invites_by_target_user(target_user)
        return groupinvitation_accepted_invites_target_user


@studyfix.route('/groupinvitation-pend-invites')
@studyfix.response(500, 'when server has problems')
class GroupInvitationsPendInvitesOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self):
        """Reading out all groupinvitation objects that are still pending."""
        adm = Administration()
        groupinvitation_pend_invites = adm.get_all_pend_invites()
        return groupinvitation_pend_invites



# -----StudyGroup---------


@studyfix.route('/studygroup')
@studyfix.response(500, 'when server has problems')
class StudyGroupListOperations(Resource):
    """Reading out all studygroup objects.
    If no user objects are available, an empty sequence is returned."""

    @studyfix.marshal_list_with(studygroup)
    @secured
    def get(self):
        adm = Administration()
        studygroups = adm.get_all_studygroups()
        return studygroups

    @studyfix.marshal_with(studygroup, code=200)
    @studyfix.expect(studygroup)  # We expect a user object from the client side.
    @secured
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
            s = adm.create_studygroup(prpl.get_name(), prpl.get_chat_id())

            return s, 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500


@studyfix.route('/studygroup/<int:id>')
@studyfix.response(500, 'when server has problems')
class StudyGroupOperations(Resource):
    @studyfix.marshal_with(studygroup)
    @secured
    def get(self, id):
        """reading out a specific studygroupobject.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_studygroup = adm.get_studygroup_by_id(id)
        return single_studygroup

    @secured
    def delete(self, id):
        """Deletion of a specific studygroup object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()
        single_studygroup= adm.get_studygroup_by_id(id)
        """adm.delete_studygroup(single_studygroup)
        return '', 200"""

        if single_studygroup is not None:
            adm.delete_studygroup(single_studygroup)
            return '', 200
        else:
            return '', 500


    @studyfix.marshal_with(studygroup)
    @studyfix.expect(studygroup, validate=True)  # We expect a user object from the client side.
    @secured
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



@studyfix.route('/studygroup/<string:name>')
@studyfix.response(500, 'when server has problems')
class StudyGroupOperations(Resource):
    @studyfix.marshal_with(studygroup)
    @secured
    def get(self, name):
        """Reading out studygroup objects that are determined by the lastname.
        The objects to be read out are determined by '' name '' in the URI."""
        adm = Administration()
        studygroup = adm.get_studygroup_by_name(name)
        return studygroup


@studyfix.route('/studygroup-by-learning-profile/<int:learning_profile_id>')
@studyfix.response(500, 'when server has problems')
class StudyGroupLearningProfileOperations(Resource):
    @studyfix.marshal_with(studygroup)
    @secured
    def get(self, learning_profile_id):
        """Reading out studygroup objects that are determined by the lastname.
        The objects to be read out are determined by '' name '' in the URI."""
        adm = Administration()
        studygroup = adm.get_studygroup_by_learning_profile_id(learning_profile_id)
        return studygroup



# -------LearningProfileGroup---------



@studyfix.route('/learningprofilegroup')
@studyfix.response(500, 'when server has problems')
class LearningProfileGroupListOperations(Resource):
    """Reading out all learninprofile group objects.
    If no user objects are available, an empty sequence is returned."""

    @studyfix.marshal_list_with(learningprofilegroup)
    @secured
    def get(self):
        adm = Administration()
        learningprofiles = adm.get_all_learningprofiles_group()
        return learningprofiles

    @studyfix.marshal_with(learningprofilegroup, code=200)
    @studyfix.expect(learningprofilegroup)  # We expect a user object from the client side.
    @secured
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

            s = adm.create_learningprofile_group(prpl.get_group_id(), prpl.get_name(),
                                                 prpl.get_prev_knowledge(),
                                                 prpl.get_extroversion(),
                                                 prpl.get_study_state(),
                                                 prpl.get_frequency(),
                                                 prpl.get_learntyp(),
                                                 prpl.get_semester(),
                                                 prpl.get_interest(),
                                                 prpl.get_degree_course())

            return s, 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500


@studyfix.route('/learningprofilegroup/<int:id>')
@studyfix.response(500, 'when server has problems')
class LearningProfileGroupOperations(Resource):
    @studyfix.marshal_with(learningprofilegroup)
    @secured
    def get(self, id):
        """reading out a specific learninprofileobject.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_learningprofile = adm.get_learningprofile_group_by_id(id)
        return single_learningprofile

    @studyfix.marshal_with(learningprofilegroup)
    @studyfix.expect(learningprofilegroup, validate=True)  # We expect a learningprofile object from the client side.
    @secured
    def put(self, id):
        """ Update of a specific learninprofile object.
        The relevant id is the id provided by the URI and thus as a method parameter
        is used. This parameter overwrites the ID attribute of the transmitted in the payload of the request
        student object."""
        adm = Administration()
        learningprofilegroup = LearningProfileGroup.from_dict(api.payload)
        print('main aufruf')

        if learningprofilegroup is not None:
            """This sets the id of the learninprofile object to be overwritten (see update)."""
            learningprofilegroup.set_id(id)
            adm.save_learningprofile_group(learningprofilegroup)
            return '', 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500

    @secured
    def delete(self, id):
        """Deletion of a specific learninprofile object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()

        learning_profile = adm.get_learningprofile_group_by_id(id)

        if learning_profile is not None:
            adm.delete_learningprofile_group(learning_profile)
            return '', 200
        else:
            return '', 500



@studyfix.route('/learningprofilegroup-by-name/<string:name>')
@studyfix.response(500, 'when server has problems')
class LearningProfileGroupByNameOperations(Resource):
    @studyfix.marshal_with(learningprofilegroup)
    @secured
    def get(self, name):
        """Reading out studygroup objects that are determined by the lastname.
        The objects to be read out are determined by '' name '' in the URI."""
        adm = Administration()
        learning_profile_by_name = adm.get_learningprofile_group_by_name(name)
        return learning_profile_by_name

@studyfix.route('/groups-by-google-id/<string:google_id>')
@studyfix.response(500, 'when server has problems')
class GroupsByGoogleId(Resource):
    @studyfix.marshal_with(studygroup)
    def get(self, google_id):
        adm = Administration()
        studygroups_by_google_id = adm.get_groups_by_google_id(google_id)
        return studygroups_by_google_id


# -------LearningProfileUser---------



@studyfix.route('/learningprofileuser')
@studyfix.response(500, 'when server has problems')
class LearningProfileUserListOperations(Resource):
    """Reading out all learninprofile user objects.
    If no user objects are available, an empty sequence is returned."""

    @studyfix.marshal_list_with(learningprofileuser)
    @secured
    def get(self):
        adm = Administration()
        learningprofiles = adm.get_all_learningprofiles_user()
        return learningprofiles

    @studyfix.marshal_with(learningprofileuser, code=200)
    @studyfix.expect(learningprofileuser)  # We expect a user object from the client side.
    @secured
    def post(self):
        """Create a new learningprofile group object. We take the data sent by the client as a suggestion.
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

            s = adm.create_learningprofile_user(prpl.get_user_id(),
                                                prpl.get_name(),
                                                prpl.get_prev_knowledge(),
                                                prpl.get_extroversion(),
                                                prpl.get_study_state(),
                                                prpl.get_frequency(),
                                                prpl.get_learntyp(),
                                                prpl.get_semester(),
                                                prpl.get_interest(),
                                                prpl.get_degree_course())

            return s, 200
        else:
            """When it comes down to it, we don't give anything back and throw a server error."""
            return '', 500


@studyfix.route('/learningprofileuser/<int:id>')
@studyfix.response(500, 'when server has problems')
class LearningProfileUserOperations(Resource):
    @studyfix.marshal_with(learningprofileuser)
    @secured
    def get(self, id):
        """reading out a specific learninprofileobject.
           The object to be read is determined by the '' id '' in the URI."""
        adm = Administration()
        single_learningprofile = adm.get_learningprofile_user_by_id(id)
        return single_learningprofile

    @studyfix.marshal_with(learningprofileuser)
    @studyfix.expect(learningprofileuser, validate=True)  # We expect a learningprofile object from the client side.
    @secured
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

    @secured
    def delete(self, id):
        """Deletion of a specific learninprofile object.
        The object to be deleted is determined by the '' id '' in the URI."""
        adm = Administration()
        single_learningprofile = adm.get_learningprofile_user_by_id(id)
        adm.delete_learningprofile_user(single_learningprofile)
        return '', 200


@studyfix.route('/learningprofileuser-by-name/<string:name>')
@studyfix.response(500, 'when server has problems')
class LearningProfileUserByNameOperations(Resource):
    @studyfix.marshal_with(learningprofilegroup)
    @secured
    def get(self, name):
        """Reading out studygroup objects that are determined by the lastname.
        The objects to be read out are determined by '' name '' in the URI."""
        adm = Administration()
        learning_profile_by_name = adm.get_learningprofile_user_by_name(name)
        return learning_profile_by_name

@studyfix.route('/friend-requests-by-google-id/<string:google_id>')
@studyfix.response(500, 'when server has problems')
class FriendRequestsByGoogleId(Resource):
    @studyfix.marshal_with(user)
    def get(self, google_id):
        adm = Administration()
        friend_requests_by_google_id = adm.get_friend_requests_by_google_id(google_id)
        return friend_requests_by_google_id

@studyfix.route('/friends-by-google-id/<string:google_id>')
@studyfix.response(500, 'when server has problems')
class FriendsByGoogleId(Resource):
    @studyfix.marshal_with(user)
    def get(self, google_id):
        adm = Administration()
        friends_by_google_id = adm.get_friends_by_google_id(google_id)
        return friends_by_google_id

@studyfix.route('/matching/<string:id>')
@studyfix.response(500, 'when server has problems')
class MatchingAlgorithmus(Resource):
    def get(self, id):
        adm = Administration()
        matches = adm.get_matches_user(id, .2)

        # Liste an User Matches display Informationen
        result = []

        # Filter existing friends
        buddy_ids = []

        # Where source user
        buddys = adm.get_all_invites_by_source_user(adm.get_user_by_google_id(id).get_id())
        if type(buddys) != list:
            buddy_ids.append(buddys.get_target_user())
        else:
            for obj in buddys:
                buddy_ids.append(obj.get_target_user())

        # Where target user
        buddys = adm.get_all_invites_by_target_user(adm.get_user_by_google_id(id).get_id())
        if type(buddys) != list:
            buddy_ids.append(buddys.get_source_user())
        else:
            for obj in buddys:
                buddy_ids.append(obj.get_source_user())

        print("Friend User Ids: (beeing filtered from result)", buddy_ids)

        for learningprofile_id in matches:
            user_id = adm.get_user_id_by_learningprofile_id(learningprofile_id)
            user = adm.get_user_by_id(user_id)
            learningprofile = adm.get_learningprofile_user_by_id(learningprofile_id)
            name = user.get_firstname() + " " + user.get_lastname()
            semester = learningprofile.get_semester()
            interest = learningprofile.get_interest()
            matching_score = matches[learningprofile_id]
            matching_score = str(round(matching_score*100)) + "%"

            if interest != 'interest preset' and user_id not in buddy_ids:
                result.append({"name": name, "semester": semester, "interest": interest, "matching_score": matching_score, "id": user_id})

        # Ergebnisse sortieren für frontend
        def get_score(var):
            return var.get("matching_score")
        result.sort(key=get_score)
        result.reverse()

        print("User Matches:", result)

        return result


@studyfix.route('/groupmatching/<string:id>')
@studyfix.response(500, 'when server has problems')
class GroupMatchingAlgorithmus(Resource):
    def get(self, id):
        adm = Administration()
        matches = adm.get_matches_group(id, .1)
        result = []

        # Filter existing group participations
        groupPart_ids = []

        # Where source user
        groupPart = adm.get_groupinvitations_by_source_user(adm.get_user_by_google_id(id).get_id())
        print(groupPart)
        if type(groupPart) != list:
            groupPart_ids.append(groupPart.get_study_group_id())
        else:
            for obj in groupPart:
                groupPart_ids.append(obj.get_study_group_id())

        # Where target user
        groupPart = adm.get_groupinvitations_by_target_user(adm.get_user_by_google_id(id).get_id())
        if type(groupPart) != list:
            groupPart_ids.append(groupPart.get_study_group_id())
        else:
            for obj in groupPart:
                groupPart_ids.append(obj.get_study_group_id())

        print("Group User Ids: (beeing filtered from result)", groupPart_ids)
        for learningprofile_id in matches:
            learningprofile = adm.get_learningprofile_group_by_id(learningprofile_id)
            group_id = learningprofile.get_group_id()
            group = adm.get_studygroup_by_id(group_id)
            grouplearningprofile = adm.get_learningprofile_group_by_id(learningprofile_id)
            name = group.get_name()
            semester = grouplearningprofile.get_semester()
            interest = grouplearningprofile.get_interest()
            matching_score = matches[learningprofile_id]
            matching_score = str(round(matching_score*100)) + "%"

            if interest != 'interest preset' and group_id not in groupPart_ids:
                result.append({"name": name, "semester": semester, "interest": interest, "matching_score": matching_score, "id": group_id})


            def get_score(matching_score):
                return matching_score.get("matching_score")
            result.sort(key= get_score)
            result.reverse()
        print("Group Matches:", result)
        return result


@studyfix.route('/auth')
@studyfix.response(500, 'when server has problems')
class Authorisation(Resource):
    @secured
    def get(self):
        return True


"""
Nachdem wir nun sämtliche Resourcen definiert haben, die wir via REST bereitstellen möchten,
müssen nun die App auch tatsächlich zu starten.
Diese Zeile ist leider nicht Teil der Flask-Doku! In jener Doku wird von einem Start via Kommandozeile ausgegangen.
Dies ist jedoch für uns in der Entwicklungsumgebung wenig komfortabel. Deshlab kommt es also schließlich zu den 
folgenden Zeilen. 
**ACHTUNG:** Diese Zeile wird nur in der lokalen Entwicklungsumgebung ausgeführt und hat in der Cloud keine Wirkung!
"""
if __name__ == '__main__':
    """print(Administration.get_matches_user(Administration(), "bUIElVVYTQPW22h4Sc4SvzjnMLx1", .1))"""
    """print(Administration.get_matches_group(Administration(), 1, .1))"""
    """print(Administration.get_matches_user(Administration(),"16060601 6962", 0.5))"""
    """print(Administration.get_groups_by_google_id(Administration(),"DcTHAA8lqLe09RNM2l36ipTfHYB2"))"""
    app.run(debug=True)


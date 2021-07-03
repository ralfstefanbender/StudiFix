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
A. Konventionen für dieses Module:
    A.1. HTTP response status codes:
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
    A.2. Name des Moduls:
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
studyFix-relevanten Operationen unter dem Präfix /studyfix zusammen."""

studyfix = api.namespace('studyfix', description='Funktionen des studyFix')



bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Der Unique Identifier eines BusinessObject'),
    'creation_date': fields.DateTime(attribute='_creation_date', description='Das Erstellungsdatum eines Business Object ',
                                     dt_format='iso8601')
})

nbo = api.inherit('NamedBusinessObject', bo, {
    'name': fields.String(attribute='_name', description='Name eines NamedBusinessObjects')
})


chat = api.inherit('Chat', nbo,{

})

chatinvitation = api.inherit('ChatInvitation', bo, {
    'source_owner': fields.Integer(attribute='_source_user', description='Unique Id des Chatinhabers'),
    'target_owner': fields.Integer(attribute='_target_user', description='Unique Id des Einzuladenden'),
    'chat_id': fields.Integer(attribute='_chat_id', description='Chat id des Chats'),
    'is_accepted': fields.Integer(attribute='_is_accepted', description='Invitation akzeptiert / nicht akzeptiert')
})

chatmessage = api.inherit('ChatMessage', bo, {
    'chat_id': fields.Integer(attribute='_chat_id', description='Unique Id des Chats'),
    'user_id': fields.Integer(attribute='_user_id', description='Unique Id des Versenders'),
    'text': fields.String(attribute='_text', description='Inhalt der Nachricht')
})

groupinvitation = api.inherit('GroupInvitation', bo, {
    'target_owner': fields.Integer(attribute='_target_user', description='Unique Id des Einzuladenden'),
    'source_owner': fields.Integer(attribute='_source_user', description='Unique Id des Chatinhabers'),
    'study_group_id': fields.Integer(attribute='_study_group_id', description='Unique Id der Gruppe'),
    'is_accepted': fields.Integer(attribute='_is_accepted', description='Invitation akzeptiert / nicht akzeptiert')
})

learningprofile = api.inherit('LearningProfile', nbo, {
    'prev_knowledge': fields.Integer(attribute='_prev_knowledge', description='Bisherige Kentnisse'),
    'extroversion': fields.Integer(attribute='_extroversion', description='Extrovertiertheit'),
    'study_state': fields.Integer(attribute='_study_state', description='On oder Offline'),
    'frequency': fields.Integer(attribute='_frequency', description='Häufigkeit'),
    'learntyp': fields.Integer(attribute='_learntyp', description='Learntyp des Profilinhabers'),
    'semester': fields.Integer(attribute='_semester', description='Semester'),
    'interest': fields.String(attribute='_interest', description='Interessen des Profilinhabers'),
    'degree_course': fields.String(attribute='_degree_course', description='Studiengang')
})

learningprofilegroup = api.inherit('LearningProfileGroup', learningprofile, {
    'group_id': fields.Integer(attribute='_group_id', description='Die Gruppen ID')

})

learningprofileuser = api.inherit('LearningProfileUser', learningprofile, {
    'user_id': fields.Integer(attribute='_user_id', description='Die User ID')
})

studygroup = api.inherit('StudyGroup', nbo, {
    'chat_id':fields.Integer(attribute='_chat_id', description='Die Chat ID')
})

user = api.inherit('User', bo, {
    'google_id': fields.String(attribute='_google_id', description='Google User Id des Profilinhabers'),
    'firstname': fields.String(attribute='_firstname', description='Vorname des Users'),
    'lastname': fields.String(attribute='_lastname', description='Nachname des Users'),
    'email': fields.String(attribute='_email', description='Email Adresse eines Users'),
    'adress': fields.String(attribute='_adress', description='Adresse des Profilinhabers')
})


@app.route('/hello')
def hello():
    return 'Hello World!'


# -----User-----


@studyfix.route('/user')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class UserListOperations(Resource):
    """Auslesen aller User-Objekte.
    Sollten keine User-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""

    @studyfix.marshal_list_with(user)
    @secured
    def get(self):
        adm = Administration()
        users = adm.get_all_users()
        return users

    @studyfix.marshal_with(user, code=200)
    @studyfix.expect(user)  #Wir erwarten ein User-Objekt von Client-Seite.
    @secured
    def post(self):
        """Anlegen eines neuen User-Objekts.
        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der Administration (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*"""

        adm = Administration()
        prpl = User.from_dict(api.payload)
        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""

        if prpl is not None:
            """ Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben."""

            s = adm.create_user(prpl.get_google_id(), prpl.get_firstname(), prpl.get_lastname(),
                                prpl.get_email(), prpl.get_adress())

            return s, 200

        else:
            ''' Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.'''

            return '', 500


@studyfix.route('/user/<int:id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class UserOperations(Resource):
    @studyfix.marshal_with(user)
    @secured
    @secured
    def get(self, id):
        """Auslesen eines bestimmten User-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        single_user = adm.get_user_by_id(id)
        return single_user

    @studyfix.marshal_with(user)
    @studyfix.expect(user, validate=True)   #Wir erwarten ein User-Objekt von Client-Seite.
    @secured
    def put(self, id):
        """Update eines bestimmten User-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        User-Objekts."""

        adm = Administration()
        user = User.from_dict(api.payload)
        print('main aufruf')

        if user is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) User-Objekts gesetzt."""

            user.set_id(id)
            adm.save_user(user)
            return '', 200

        else:
            return '', 500

    @secured
    def delete(self, id):
        """Löschen eines bestimmten User-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        single_user = adm.get_user_by_id(id)
        adm.delete_user(single_user)
        return '', 200


@studyfix.route('/user-by-lastname/<string:lastname>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class UserNameOperations(Resource):
    @studyfix.marshal_list_with(user)
    @secured
    def get(self, lastname):
        """ Auslesen von User-Objekten, die durch den Nachnamen bestimmt werden.
        Die auszulesenden Objekte werden durch ```lastname``` in dem URI bestimmt."""

        adm = Administration()
        user = adm.get_user_by_lastname(lastname)
        return user


@studyfix.route('/user-by-firstname/<string:firstname>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class UserFirstNameOperations(Resource):
    @studyfix.marshal_with(user)
    @secured
    def get(self, firstname):
        """ Auslesen von User-Objekten, die durch den Vornamen bestimmt werden.
        Die auszulesenden Objekte werden durch ```firstname``` in dem URI bestimmt."""

        adm = Administration()
        user = adm.get_user_by_firstname(firstname)
        return user


@studyfix.route('/user-by-mail/<string:email>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class UserMailOperations(Resource):
    @studyfix.marshal_list_with(user)
    @secured
    def get(self, email):
        """ Auslesen von User-Objekten, die durch die E-Mail bestimmt werden.
        Die auszulesenden Objekte werden durch ```email``` in dem URI bestimmt."""

        adm = Administration()
        users = adm.get_user_by_email(email)
        return users


@studyfix.route('/user-by-google-id/<string:google_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class UserGoogleOperations(Resource):
    @studyfix.marshal_with(user)
    @secured
    def get(self, google_id):
        """Auslesen eines bestimmten User-Objekts.
        Das auszulesende Objekt wird durch die ```google_id``` in dem URI bestimmt."""

        adm = Administration()
        users = adm.get_user_by_google_id(google_id)
        return users


@studyfix.route('/user-by-learning-profile-id/<int:learning_profile_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class UserGoogleOperations(Resource):
    @studyfix.marshal_with(user)
    @secured
    def get(self, learning_profile_id):
        """Auslesen eines bestimmten User-Objekts.
        Das auszulesende Objekt wird durch die ```learning_profile_id``` in dem URI bestimmt.
        """

        adm = Administration()
        users = adm.get_user_by_learning_profile_id(learning_profile_id)
        return users


# ----ChatInvitation-----


@studyfix.route('/chatinvitation')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ChatInvitationListOperations(Resource):
    """Auslesen aller ChatInvitation-Objekte.
    Sollten keine ChatInvitation-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""

    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self):
        adm = Administration()
        chatinvitations = adm.get_all_chatinvitations()
        return chatinvitations

    @studyfix.marshal_with(chatinvitation, code=200)
    @studyfix.expect(chatinvitation)   #Wir erwarten ein ChatInvitation-Objekt von Client-Seite.

    def post(self):
        """Anlegen eines neuen ChatInvitation-Objekts.
        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der Administration (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*
        """

        adm = Administration()
        print(api.payload)
        prpl = ChatInvitation.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""

        if prpl is not None:
            """ Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben. 
            """

            s = adm.create_chatinvitation(prpl.get_source_user(),
                                          prpl.get_target_user(),
                                          prpl.get_chat_id(),
                                          prpl.get_is_accepted()
                                          )
            return s, 200

        else:
            return '', 500


@studyfix.route('/chatinvitation/<int:id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ChatInvitationOperations(Resource):
    @studyfix.marshal_with(chatinvitation)
    @secured
    def get(self, id):
        """Auslesen eines bestimmten ChatInvitation-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt.
        """

        adm = Administration()
        single_chat_invitation = adm.get_chatinvitation_by_id(id)
        return single_chat_invitation

    @secured
    def delete(self, id):
        """Löschen eines bestimmten ChatInvitation-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        chat_invitation = adm.get_chatinvitation_by_id(id)

        if chat_invitation is not None:

            adm.delete_chatinvitation(chat_invitation)
            return '', 200

        else:
            return '', 500


    @studyfix.marshal_with(chatinvitation)
    @studyfix.expect(chatinvitation, validate=True)  #Wir erwarten ein ChatInvitation-Objekt von Client-Seite.

    def put(self, id):
        """Update eines bestimmten ChatInvitation-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        ChatInvitation-Objekts."""

        adm = Administration()
        chatinvitation = ChatInvitation.from_dict(api.payload)
        print('main aufruf')

        if chatinvitation is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) ChatInvitation-Objekts gesetzt."""

            chatinvitation.set_id(id)
            adm.save_chatinvitation(chatinvitation)
            return '', 200

        else:
            return '', 500


@studyfix.route('/chatinvitation-by-target-user/<int:target_user>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ChatInvitationByTargetOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self, target_user):
        """ Auslesen von allen ChatInvitation-Objekten, die durch den TargetUser bestimmt werden.
        Die auszulesenden Objekte werden durch ```target_user``` in dem URI bestimmt."""

        adm = Administration()
        chatinvitation_target_user = adm.get_all_invites_by_target_user(target_user)
        return chatinvitation_target_user


@studyfix.route('/chatinvitation-by-source-user/<int:source_user>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ChatInvitationBySourceOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self, source_user):
        """Auslesen von allen ChatInvitation-Objekten, die durch den TargetUser bestimmt werden.
        Die auszulesenden Objekte werden durch ```target_user``` in dem URI bestimmt."""

        adm = Administration()
        chatinvitation_source_user = adm.get_all_invites_by_source_user(source_user)
        return chatinvitation_source_user


@studyfix.route('/chatinvitation-accepted-by-chat/<int:chat_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ChatInvitationsAcceptedOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self, chat_id):
        """Auslesen von akzeptierten ChatInvitation-Objekten.
        Die auszulesenden Objekte werden durch ```chat_id``` in dem URI bestimmt."""

        adm = Administration()
        chatinvitation_is_accepted = adm.get_all_accepted_user_in_chat(chat_id)
        return chatinvitation_is_accepted


@studyfix.route('/chatinvitation-pend-invites')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ChatInvitationsPendInvitesOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self):
        """ Auslesen von allen ChatInvitation-Objekten die weder akzeptiert noch angenommen wurden. """

        adm = Administration()
        chatinvitation_pend_invites = adm.get_all_pend_invites()
        return chatinvitation_pend_invites


@studyfix.route('/chatinvitation-pend-invites-target/<int:target_user>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ChatInvitationsPendInvitesByTargetUserOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self, target_user):
        """ Auslesen von ChatInvitation-Objekten die vom TargetUser weder akzeptiert noch gelöscht wurden.
        Die auszulesenden Objekte werden durch ```target_user``` in dem URI bestimmt. """

        adm = Administration()
        chatinvitation_pend_invites_target_user = adm.get_pend_invites_by_target_user(target_user)
        return chatinvitation_pend_invites_target_user


@studyfix.route('/chatinvitation-pend-invites-source/<int:source_user>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ChatInvitationsPendInvitesBySourceUserOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self, source_user):
        """Auslesen von ChatInvitation-Objekten die vom SourceUser weder akzeptiert noch gelöscht wurden.
        Die auszulesenden Objekte werden durch ```source_user``` in dem URI bestimmt."""

        adm = Administration()
        chatinvitation_pend_invites_source_user = adm.get_pend_invites_by_source_user(source_user)
        return chatinvitation_pend_invites_source_user


@studyfix.route('/chatinvitation-accepted-invites-source/<int:source_user>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ChatInvitationsAcceptedInvitesBySourceUserOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self, source_user):
        """Auslesen von ChatInvitation-Objekten die vom SourceUser akzeptiert wurden.
        Die auszulesenden Objekte werden durch ```source_user``` in dem URI bestimmt."""

        adm = Administration()
        chatinvitation_accepted_invites_source_user = adm.get_accepted_invites_by_source_user(source_user)
        return chatinvitation_accepted_invites_source_user


@studyfix.route('/chatinvitation-accepted-invites-target/<int:target_user>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ChatInvitationsAcceptedInvitesByTargetUserOperations(Resource):
    @studyfix.marshal_list_with(chatinvitation)
    @secured
    def get(self, target_user):
        """Auslesen von ChatInvitation-Objekten die vom TargetUser akzeptiert wurden.
        Die auszulesenden Objekte werden durch ```target_user``` in dem URI bestimmt."""

        adm = Administration()
        chatinvitation_accepted_invites_target_user = adm.get_accepted_invites_by_target_user(target_user)
        return chatinvitation_accepted_invites_target_user



# ---------Chatmessage--------


@studyfix.route('/chatmessage')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ChatMessageListOperations(Resource):
    """Auslesen aller ChatMessage-Objekte.
    Sollten keine ChatMessage-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""

    @studyfix.marshal_list_with(chatmessage)
    @secured
    def get(self):
        adm = Administration()
        chatmessages = adm.get_all_chatmessages()
        return chatmessages

    @studyfix.marshal_with(chatmessage, code=200)
    @studyfix.expect(chatmessage)  #Wir erwarten ein ChatMessage-Objekt von Client-Seite.

    def post(self):
        """Anlegen eines neuen ChatMessage-Objekts.
        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der Administration (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*"""

        adm = Administration()
        prpl = ChatMessage.from_dict(api.payload)
        
        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""

        if prpl is not None:
            """Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben."""

            chatmessage = adm.create_chatmessage(prpl.get_chat_id(), prpl.get_user_id(), prpl.get_text())

            return chatmessage, 200

        else:
            return '', 500


@studyfix.route('/chatmessage/<int:id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ChatMessageOperations(Resource):
    @studyfix.marshal_with(chatmessage)
    @secured
    def get(self, id):
        """Auslesen eines bestimmten ChatMessage-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        single_chatmessage = adm.get_chatmessage_by_id(id)
        return single_chatmessage

    @studyfix.marshal_with(chatmessage)
    @studyfix.expect(chatmessage, validate=True)  #Wir erwarten ein ChatMessage-Objekt von Client-Seite.
    @secured
    def put(self, id):
        """Update eines bestimmten ChatMessage-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        ChatMessage-Objekts."""

        adm = Administration()
        chatmessage = ChatMessage.from_dict(api.payload)
        print('main aufruf')

        if chatmessage is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) ChatMessage-Objekts gesetzt."""

            chatmessage.set_id(id)
            adm.save_chatmessage(chatmessage)
            return '', 200

        else:
            return '', 500

    @secured
    def delete(self, id):
        """Löschen eines bestimmten ChatInvitation-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        single_chatmessage = adm.get_chatmessage_by_id(id)
        adm.delete_chatmessage(single_chatmessage)
        return '', 200


@studyfix.route('/chatmessage-chat-id/<int:chat_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ChatMessageOperations(Resource):
    @studyfix.marshal_list_with(chatmessage)
    @secured
    def get(self, chat_id):
        """Auslesen von ChatMessage-Objekten über den Chat.
        Die auszulesenden Objekte werden durch ```chat_id``` in dem URI bestimmt."""

        adm = Administration()
        chatmessage_by_chat_id = adm.get_chatmessages_by_chat_id(chat_id)
        return chatmessage_by_chat_id


# -------Chat-------


@studyfix.route('/chat')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ChatListOperations(Resource):
    """Auslesen aller Chat-Objekte.
    Sollten keine Chat-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""

    @studyfix.marshal_list_with(chat)
    @secured
    def get(self):
        adm = Administration()
        chats = adm.get_all_chats()
        return chats


    @studyfix.marshal_with(chat, code=200)
    @studyfix.expect(chat)  #Wir erwarten ein ChatMessage-Objekt von Client-Seite.
    @secured
    def post(self):
        """Anlegen eines neuen Chat-Objekts.
        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der Administration (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*"""

        adm = Administration()
        prpl = Chat.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""

        if prpl is not None:
            """Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben."""

            c = adm.create_chat(prpl.get_name())
            return c, 200

        else:
            return '', 500


@studyfix.route('/chat/<int:id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class ChatOperations(Resource):
    @studyfix.marshal_with(chat)
    @secured
    def get(self, id):
        """Auslesen eines bestimmten Chat-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        single_chat = adm.get_chat_by_id(id)
        return single_chat

    @secured
    def delete(self, id):
        """Löschen eines bestimmten Chat-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        chat = adm.get_chat_by_id(id)

        if chat is not None:
            adm.delete_chat(chat)
            return '', 200

        else:
            return '', 500

    @studyfix.marshal_with(chat)
    @studyfix.expect(chat, validate=True)  #Wir erwarten ein ChatMessage-Objekt von Client-Seite.
    @secured
    def put(self, id):
        """Update eines bestimmten Chat-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        Chat-Objekts."""

        adm = Administration()
        chat = Chat.from_dict(api.payload)
        print('main aufruf')

        if chat is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Person-Objekts gesetzt."""

            chat.set_id(id)
            adm.save_chat(chat)
            return '', 200

        else:
            return '', 500


# ----GroupInvitation----


@studyfix.route('/groupinvitation')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GroupInvitationListOperations(Resource):
    """Auslesen aller GroupInvitation-Objekte.
    Sollten keine GroupInvitation-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""

    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self):
        adm = Administration()
        groupinvitations = adm.get_all_groupinvitations()
        return groupinvitations

    @studyfix.marshal_with(groupinvitation, code=200)
    @studyfix.expect(groupinvitation)   #Wir erwarten ein ChatMessage-Objekt von Client-Seite.
    
    def post(self):
        """Anlegen eines neuen GroupInvitation-Objekts.
        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der Administration (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*"""

        adm = Administration()
        prpl = GroupInvitation.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""

        if prpl is not None:
            """Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben."""

            s = adm.create_groupinvitation(prpl.get_source_user(),
                                           prpl.get_target_user(),
                                           prpl.get_study_group_id(),
                                           prpl.get_is_accepted()
                                           )
            return s, 200

        else:
            return '', 500


@studyfix.route('/groupinvitation/<int:id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GroupInvitationOperations(Resource):
    @studyfix.marshal_with(groupinvitation)
    @secured
    def get(self, id):
        """Auslesen eines bestimmten GroupInvitation-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        single_groupinvitation = adm.get_groupinvitation_by_id(id)
        return single_groupinvitation

    @studyfix.marshal_with(groupinvitation)
    @studyfix.expect(groupinvitation, validate=True)  #Wir erwarten ein ChatMessage-Objekt von Client-Seite.
    def put(self, id):
        """Update eines bestimmten GroupInvitation-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        GroupInvitation-Objekts."""

        adm = Administration()
        groupinvitation = GroupInvitation.from_dict(api.payload)
        print('main aufruf')

        if groupinvitation is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Person-Objekts gesetzt."""

            groupinvitation.set_id(id)
            adm.save_groupinvitation(groupinvitation)
            return '', 200

        else:
            return '', 500

    @secured
    def delete(self, id):
        """Löschen eines bestimmten GroupInvitation-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        single_groupinvitation = adm.get_user_by_id(id)
        adm.delete_groupinvitation(single_groupinvitation)
        return '', 200


@studyfix.route('/groupinvitation-by-study-group/<int:study_group_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GroupinvitationByTargetOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, study_group_id):
        """Auslesen von ChatMessage-Objekten über eine Group.
        Die auszulesenden Objekte werden durch ```study_group_id``` in dem URI bestimmt."""

        adm = Administration()
        groupinvitation_by_study_group = adm.get_groupinvitation_by_study_group_id(study_group_id)
        return groupinvitation_by_study_group


@studyfix.route('/groupinvitation-by-target-user/<int:target_user>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GroupInvitationByTargetOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, target_user):
        """Auslesen von GroupInvitation-Objekten, die durch den TargetUser bestimmt werden.
        Die auszulesenden Objekte werden durch ```target_user``` in dem URI bestimmt."""

        adm = Administration()
        groupinvitation_target_user = adm.get_groupinvitations_by_target_user(target_user)
        return groupinvitation_target_user


@studyfix.route('/groupinvitation-by-source-user/<int:source_user>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GroupInvitationBySourceOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, source_user):
        """Auslesen von GroupInvitation-Objekten, die durch den SourceUser bestimmt werden.
        Die auszulesenden Objekte werden durch ```source_user``` in dem URI bestimmt."""

        adm = Administration()
        groupinvitation_source_user = adm.get_groupinvitations_by_source_user(source_user)
        return groupinvitation_source_user


@studyfix.route('/groupinvitation-pend-invites/<int:study_group_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GroupInvitationsPendInvitesByStudyGroupOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, study_group_id):
        """Auslesen von allen GroupInvitation-Objekten die weder akzeptiert noch angenommen wurden über die StudyGroupID."""

        adm = Administration()
        groupinvitation_pend_invites_by_study_group = adm.get_groupinvitation_pend_invites_by_study_group(
            study_group_id)
        return groupinvitation_pend_invites_by_study_group


@studyfix.route('/groupinvitation-accepted-by-study-group/<int:study_group_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GroupInvitationsAcceptedByStudyGroupOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, study_group_id):
        """Auslesen aller akzeptierten GroupInvitation-Objekten der StudyGroup. """
        
        adm = Administration()
        groupinvitation_is_accepted_by_study_group = adm.get_accepted_groupinvitation_by_study_group_id(study_group_id)
        return groupinvitation_is_accepted_by_study_group


@studyfix.route('/groupinvitation-pend-invites-target/<int:target_user>')
@studyfix.response(500, 'when server has problems')
class GroupInvitationsPendInvitesByTargetUserOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, target_user):
        """Auslesen von GroupInvitation-Objekten die vom TargetUser weder akzeptiert noch gelöscht wurden.
        Die auszulesenden Objekte werden durch ```target_user``` in dem URI bestimmt."""

        adm = Administration()
        groupinvitation_pend_invites_target_user = adm.get_pend_invites_by_target_user(target_user)
        return groupinvitation_pend_invites_target_user


@studyfix.route('/groupinvitation-pend-invites-source/<int:source_user>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GroupInvitationsPendInvitesBySourceUserOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, source_user):
        """Auslesen von GroupInvitation-Objekten die vom SourceUser weder akzeptiert noch gelöscht wurden.
        Die auszulesenden Objekte werden durch ```source_user``` in dem URI bestimmt."""

        adm = Administration()
        groupinvitation_pend_invites_source_user = adm.get_pend_groupinvites_by_source_user(source_user)
        return groupinvitation_pend_invites_source_user


@studyfix.route('/groupinvitation-accepted-invites-source/<int:source_user>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GroupInvitationsAcceptedInvitesBySourceUserOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, source_user):
        """Auslesen von GroupInvitation-Objekten die vom SourceUser akzeptiert wurden.
        Die auszulesenden Objekte werden durch ```source_user``` in dem URI bestimmt."""

        adm = Administration()
        groupinvitation_accepted_invites_source_user = adm.get_accepted_invites_by_source_user(source_user)
        return groupinvitation_accepted_invites_source_user


@studyfix.route('/groupinvitation-accepted-invites-target/<int:target_user>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GroupInvitationsAcceptedInvitesByTargetUserOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self, target_user):
        """Auslesen von GroupInvitation-Objekten die vom TargetUser akzeptiert wurden.
        Die auszulesenden Objekte werden durch ```target_user``` in dem URI bestimmt."""

        adm = Administration()
        groupinvitation_accepted_invites_target_user = adm.get_accepted_invites_by_target_user(target_user)
        return groupinvitation_accepted_invites_target_user


@studyfix.route('/groupinvitation-pend-invites')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GroupInvitationsPendInvitesOperations(Resource):
    @studyfix.marshal_list_with(groupinvitation)
    @secured
    def get(self):
        """Auslesen von allen GroupInvitation-Objekten die weder akzeptiert noch gelöscht wurden."""

        adm = Administration()
        groupinvitation_pend_invites = adm.get_all_pend_invites()
        return groupinvitation_pend_invites


# -----StudyGroup---------


@studyfix.route('/studygroup')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class StudyGroupListOperations(Resource):
    """Auslesen aller StudyGroup-Objekte.
    Sollten keine StudyGroup-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""

    @studyfix.marshal_list_with(studygroup)
    @secured
    def get(self):
        adm = Administration()
        studygroups = adm.get_all_studygroups()
        return studygroups

    @studyfix.marshal_with(studygroup, code=200)
    @studyfix.expect(studygroup)  #Wir erwarten ein ChatMessage-Objekt von Client-Seite.
    @secured
    def post(self):
        """Anlegen eines neuen StudyGroup-Objekts.
        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der Administration (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*"""

        adm = Administration()
        prpl = StudyGroup.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""

        if prpl is not None:
            """Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben."""

            s = adm.create_studygroup(prpl.get_name(), prpl.get_chat_id())

            return s, 200

        else:
            return '', 500


@studyfix.route('/studygroup/<int:id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class StudyGroupOperations(Resource):
    @studyfix.marshal_with(studygroup)
    @secured
    def get(self, id):
        """Auslesen eines bestimmten StudyGroup-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        single_studygroup = adm.get_studygroup_by_id(id)
        return single_studygroup

    @secured
    def delete(self, id):
        """Löschen eines bestimmten StudyGroup-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        single_studygroup= adm.get_studygroup_by_id(id)

        if single_studygroup is not None:
            adm.delete_studygroup(single_studygroup)
            return '', 200

        else:
            return '', 500


    @studyfix.marshal_with(studygroup)
    @studyfix.expect(studygroup, validate=True)  #Wir erwarten ein ChatMessage-Objekt von Client-Seite.
    @secured
    def put(self, id):
        """Update eines bestimmten StudyGroup-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        StudyGroup-Objekts."""

        adm = Administration()
        studygroup = StudyGroup.from_dict(api.payload)
        print('main aufruf')

        if studygroup is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Person-Objekts gesetzt."""

            studygroup.set_id(id)
            adm.save_studygroup(studygroup)
            return '', 200

        else:
            return '', 500


@studyfix.route('/studygroup/<string:name>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class StudyGroupOperations(Resource):
    @studyfix.marshal_with(studygroup)
    @secured
    def get(self, name):
        """ Auslesen von StudyGroup-Objekten, die durch den Namen bestimmt werden.
        Die auszulesenden Objekte werden durch ```name``` in dem URI bestimmt."""

        adm = Administration()
        studygroup = adm.get_studygroup_by_name(name)
        return studygroup


@studyfix.route('/studygroup-by-learning-profile/<int:learning_profile_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class StudyGroupLearningProfileOperations(Resource):
    @studyfix.marshal_with(studygroup)
    @secured
    def get(self, learning_profile_id):
        adm = Administration()
        studygroup = adm.get_studygroup_by_learning_profile_id(learning_profile_id)
        return studygroup

@studyfix.route('/studygroup-create-package/<string:name>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class StudyGroupLearningProfileOperations(Resource):
    @studyfix.expect()
    @secured
    def get(self, learning_profile_id):
        """Auslesen von StudyGroup-Objekten über eine LearningProfileID.
        Die auszulesenden Objekte werden durch ```learning_profile_id`` in dem URI bestimmt."""

        adm = Administration()
        studygroup = adm.get_studygroup_by_learning_profile_id(learning_profile_id)
        return studygroup


# -------LearningProfileGroup---------


@studyfix.route('/learningprofilegroup')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class LearningProfileGroupListOperations(Resource):
    """Auslesen aller LearningProfileGroup-Objekte.
    Sollten keine LearningProfileGroup-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""

    @studyfix.marshal_list_with(learningprofilegroup)
    @secured
    def get(self):
        adm = Administration()
        learningprofiles = adm.get_all_learningprofiles_group()
        return learningprofiles

    @studyfix.marshal_with(learningprofilegroup, code=200)
    @studyfix.expect(learningprofilegroup)   #Wir erwarten ein ChatMessage-Objekt von Client-Seite.
    @secured
    def post(self):
        """Anlegen eines neuen LearningProfileGroup-Objekts.
        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der Administration (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*"""

        adm = Administration()
        prpl = LearningProfileGroup.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""

        if prpl is not None:
            """Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben."""

            s = adm.create_learningprofile_group(
                prpl.get_group_id(),
                prpl.get_name(),
                prpl.get_prev_knowledge(),
                prpl.get_extroversion(),
                prpl.get_study_state(),
                prpl.get_frequency(),
                prpl.get_learntyp(),
                prpl.get_semester(),
                prpl.get_interest(),
                prpl.get_degree_course()
                )
            return s, 200

        else:
            return '', 500


@studyfix.route('/learningprofilegroup/<int:id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class LearningProfileGroupOperations(Resource):
    @studyfix.marshal_with(learningprofilegroup)

    def get(self, id):
        """Auslesen eines bestimmten LearningProfileGroup-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        single_learningprofile = adm.get_learningprofile_group_by_id(id)
        return single_learningprofile

    @studyfix.marshal_with(learningprofilegroup)
    @studyfix.expect(learningprofilegroup, validate=True)   #Wir erwarten ein ChatMessage-Objekt von Client-Seite.
    @secured
    def put(self, id):
        """Update eines bestimmten LearningProfileGroup-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        LearningProfileGroup-Objekts."""

        adm = Administration()
        learningprofilegroup = LearningProfileGroup.from_dict(api.payload)
        print('main aufruf')

        if learningprofilegroup is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Person-Objekts gesetzt."""

            learningprofilegroup.set_id(id)
            adm.save_learningprofile_group(learningprofilegroup)
            return '', 200

        else:
            return '', 500

    @secured
    def delete(self, id):
        """Löschen eines bestimmten LearningProfileGroup-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()

        learning_profile = adm.get_learningprofile_group_by_id(id)

        if learning_profile is not None:
            adm.delete_learningprofile_group(learning_profile)
            return '', 200

        else:
            return '', 500

@studyfix.route('/learningprofilegroup-by-name/<string:name>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class LearningProfileGroupByNameOperations(Resource):
    @studyfix.marshal_with(learningprofilegroup)
    @secured
    def get(self, name):
        """Auslesen von LearningProfileGroup-Objekten, die durch den Namen bestimmt werden.
        Die auszulesenden Objekte werden durch ```name``` in dem URI bestimmt."""

        adm = Administration()
        learning_profile_by_name = adm.get_learningprofile_group_by_name(name)
        return learning_profile_by_name

@studyfix.route('/learningprofilegroup-by-group-id/<int:group_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class LearningProfileGroupByNameOperations(Resource):
    @studyfix.marshal_with(learningprofilegroup)
    @secured
    def get(self, group_id):
        """Auslesen von LearningProfileGroup-Objekten, durch eine GroupID.
        Die auszulesenden Objekte werden durch ```group_id``` in dem URI bestimmt."""
        adm = Administration()
        learning_profile_by_group_id = adm.get_learningprofile_group_by_group_id(group_id)
        return learning_profile_by_group_id


@studyfix.route('/groups-by-google-id/<string:google_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GroupsByGoogleId(Resource):
    @studyfix.marshal_with(studygroup)
    def get(self, google_id):
        """Auslesen von LearningProfileGroup-Objekt.
        Das auszulesende Objekt wird durch die ```google_id``` in dem URI bestimmt."""

        adm = Administration()
        studygroups_by_google_id = adm.get_groups_by_google_id(google_id)
        return studygroups_by_google_id


# -------LearningProfileUser---------


@studyfix.route('/learningprofileuser')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class LearningProfileUserListOperations(Resource):
    """Auslesen aller LearningProfileUser-Objekte.
    Sollten keine LearningProfileUser-Objekte verfügbar sein, so wird eine leere Sequenz zurückgegeben."""

    @studyfix.marshal_list_with(learningprofileuser)
    @secured
    def get(self):
        adm = Administration()
        learningprofiles = adm.get_all_learningprofiles_user()
        return learningprofiles

    @studyfix.marshal_with(learningprofileuser, code=200)
    @studyfix.expect(learningprofileuser) 

    def post(self):
        """Anlegen eines neuen LearningProfileUser-Objekts.
        **ACHTUNG:** Wir fassen die vom Client gesendeten Daten als Vorschlag auf.
        So ist zum Beispiel die Vergabe der ID nicht Aufgabe des Clients.
        Selbst wenn der Client eine ID in dem Proposal vergeben sollte, so
        liegt es an der Administration (Businesslogik), eine korrekte ID
        zu vergeben. *Das korrigierte Objekt wird schließlich zurückgegeben.*"""

        adm = Administration()
        prpl = LearningProfileUser.from_dict(api.payload)

        """RATSCHLAG: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!"""

        if prpl is not None:
            """Das serverseitig erzeugte Objekt ist das maßgebliche und 
            wird auch dem Client zurückgegeben."""

            s = adm.create_learningprofile_user(
                prpl.get_user_id(),
                prpl.get_name(),
                prpl.get_prev_knowledge(),
                prpl.get_extroversion(),
                prpl.get_study_state(),
                prpl.get_frequency(),
                prpl.get_learntyp(),
                prpl.get_semester(),
                prpl.get_interest(),
                prpl.get_degree_course()
                )

            return s, 200

        else:
            return '', 500


@studyfix.route('/learningprofileuser/<int:id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class LearningProfileUserOperations(Resource):
    @studyfix.marshal_with(learningprofileuser)
    @secured
    def get(self, id):
        """Auslesen eines bestimmten LearningProfileUser-Objekts.
        Das auszulesende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        single_learningprofile = adm.get_learningprofile_user_by_id(id)
        return single_learningprofile

    @studyfix.route('/learningprofileuser-by-user-id/<int:user_id>')
    @studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
    class LearningProfileUserOperations(Resource):
        @studyfix.marshal_with(learningprofileuser)
        @secured
        def get(self, user_id):
            """Auslesen eines bestimmten LearningProfileUser-Objekts.
            Das auszulesende Objekt wird durch die ```user_id``` in dem URI bestimmt."""

            adm = Administration()
            single_learningprofile = adm.get_learningprofile_user_by_user_id(user_id)
            return single_learningprofile

    @studyfix.marshal_with(learningprofileuser)
    @studyfix.expect(learningprofileuser, validate=True) 
    @secured
    def put(self, id):
        """Update eines bestimmten LearningProfileUser-Objekts.
        **ACHTUNG:** Relevante id ist die id, die mittels URI bereitgestellt und somit als Methodenparameter
        verwendet wird. Dieser Parameter überschreibt das ID-Attribut des im Payload der Anfrage übermittelten
        LearningProfileUser-Objekts."""

        adm = Administration()
        learningprofile = LearningProfileUser.from_dict(api.payload)
        print('main aufruf')

        if learningprofile is not None:
            """Hierdurch wird die id des zu überschreibenden (vgl. Update) Person-Objekts gesetzt."""

            learningprofile.set_id(id)
            adm.save_learningprofile_user(learningprofile)
            return '', 200

        else:
            return '', 500

    @secured
    def delete(self, id):
        """Löschen eines bestimmten LearningProfileGroup-Objekts.
        Das zu löschende Objekt wird durch die ```id``` in dem URI bestimmt."""

        adm = Administration()
        single_learningprofile = adm.get_learningprofile_user_by_id(id)
        adm.delete_learningprofile_user(single_learningprofile)
        return '', 200


@studyfix.route('/learningprofileuser-by-name/<string:name>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class LearningProfileUserByNameOperations(Resource):
    @studyfix.marshal_with(learningprofilegroup)
    @secured
    def get(self, name):
        """Auslesen von LearningProfileUser-Objekten, die durch den Namen bestimmt werden.
        Die auszulesenden Objekte werden durch ```name``` in dem URI bestimmt."""

        adm = Administration()
        learning_profile_by_name = adm.get_learningprofile_user_by_name(name)
        return learning_profile_by_name

#

@studyfix.route('/friend-requests-by-google-id/<string:google_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class FriendRequestsByGoogleId(Resource):
    @studyfix.marshal_with(user)
    def get(self, google_id):
        """Auslesen von Freundschaftsanfragen.
        Die auszulesenden Objekte werden durch ```google_id``` in dem URI bestimmt."""
        adm = Administration()
        friend_requests_by_google_id = adm.get_friend_requests_by_google_id(google_id)
        return friend_requests_by_google_id

@studyfix.route('/friends-by-google-id/<string:google_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class FriendsByGoogleId(Resource):
    @studyfix.marshal_with(user)
    def get(self, google_id):
        """Auslesen von Freunden.
        Die auszulesenden Objekte werden durch ```google_id``` in dem URI bestimmt."""
        adm = Administration()
        friends_by_google_id = adm.get_friends_by_google_id(google_id)
        return friends_by_google_id

@studyfix.route('/matching/<string:id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class MatchingAlgorithmus(Resource):
    def get(self, id):
        """Hier wurde der Matchin Algorithmus für die Freunde geschrieben"""

        adm = Administration()
        matches = adm.get_matches_user(id, .2)

        # Liste an User Matches display Informationen
        result = []

        # Filter existierende Freunde
        buddy_ids = []

        # Wo SourceUser
        buddys = adm.get_all_invites_by_source_user(adm.get_user_by_google_id(id).get_id())
        if type(buddys) != list:
            buddy_ids.append(buddys.get_target_user())
        else:
            for obj in buddys:
                buddy_ids.append(obj.get_target_user())

        # Wo TargetUser
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
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GroupMatchingAlgorithmus(Resource):
    def get(self, id):
        """Hier wurde der Matchin Algorithmus für die Gruppen geschrieben"""

        adm = Administration()
        matches = adm.get_matches_group(id, .1)
        result = []

        # Filter exisitierende Gruppen-Teilnahmen
        groupPart_ids = []

        # Wo SourceUser
        groupPart = adm.get_groupinvitations_by_source_user(adm.get_user_by_google_id(id).get_id())
        print(groupPart)
        if type(groupPart) != list:
            groupPart_ids.append(groupPart.get_study_group_id())
        else:
            for obj in groupPart:
                groupPart_ids.append(obj.get_study_group_id())

        # Wo TargetUser
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

            if interest != 'interest_preset' and group_id not in groupPart_ids:
                result.append({"name": name, "semester": semester, "interest": interest, "matching_score": matching_score, "id": group_id})


            def get_score(matching_score):
                return matching_score.get("matching_score")
            result.sort(key= get_score)
            result.reverse()
        print("Group Matches:", result)
        return result


@studyfix.route('/pending_group_invites-by-google-id/<string:google_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GroupsByGoogleId(Resource):

    def get(self, google_id):
        adm = Administration()
        result = []
        pending_group_invites_by_google_id = adm.get_user_pending_invites_groups_by_google_id(google_id)
        for inv in pending_group_invites_by_google_id:
            result.append({"group_id": inv[1].get_id(), "group_name": inv[1].get_name(), "google_id": inv[0].get_google_id(),
                           "firstname": inv[0].get_firstname(), "lastname": inv[0].get_lastname(),
                           "id": inv[0].get_id()})
        return result



@studyfix.route('/auth')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class Authorisation(Resource):
    @secured
    def get(self):
        return True

@studyfix.route('/acceptfriendrequests/<int:target_id>/<int:source_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class AcceptFriendInvites(Resource):

    def get(self, target_id, source_id):
        adm = Administration()
        adm.accept_friend_request(target_id, source_id)
        return True

@studyfix.route('/declinefriendrequests/<int:target_id>/<int:source_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class DeclineFriendInvites(Resource):

    def get(self, target_id, source_id):
        adm = Administration()
        adm.decline_friend_request(target_id, source_id)
        return True


@studyfix.route('/acceptgrouprequest/<int:group_id>/<int:user_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class AcceptGroupRequest(Resource):

    def get(self, group_id, user_id):
        adm = Administration()
        adm.accept_group_request(group_id, user_id)
        return True


@studyfix.route('/declinegrouprequest/<int:group_id>/<int:user_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class DeclineGroupRequest(Resource):

    def get(self, group_id, user_id):
        adm = Administration()
        adm.decline_group_request(group_id, user_id)
        return True


@studyfix.route('/chat-by-user-id/<int:user_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GetChatByUserId(Resource):
    @studyfix.marshal_with(chat)
    def get(self, user_id):
        adm = Administration()
        result = adm.get_chat_by_user_id(user_id)
        return result


@studyfix.route('/other-user-by-chat-id/<int:current_user_id>/<int:chat_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GetChatByUserId(Resource):
    @studyfix.marshal_with(user)
    def get(self, current_user_id, chat_id):
        adm = Administration()
        if adm.isgroupchat(chat_id):
            result = adm.get_group_users_by_chat(current_user_id, chat_id)
            print(result)
        else:
            result = adm.get_other_user_by_chat_id(current_user_id, chat_id)
        return result

@studyfix.route('/removefriend/<int:current_user_id>/<int:chat_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GetChatByUserId(Resource):

    def get(self, current_user_id, chat_id):
        adm = Administration()
        result = adm.remove_friend(current_user_id, chat_id)
        return result


@studyfix.route('/create-study-group-package/<string:name>/<string:user_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class CreateStudyGroupPackage(Resource):
    def get(self, name, user_id):
        adm = Administration()
        result = adm.create_studygroup_package(name, user_id)
        return True

@studyfix.route('/leavegroup/<int:current_user_id>/<int:group_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class LeaveGroup(Resource):

    def get(self, current_user_id, group_id):
        adm = Administration()
        result = adm.leave_group(current_user_id, group_id)
        return result

@studyfix.route('/group-chat-by-user-id/<int:user_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GetGroupChatByUserId(Resource):
    @studyfix.marshal_with(chat)
    def get(self, user_id):
        adm = Administration()
        result = adm.get_group_chat_by_user_id(user_id)
        return result

@studyfix.route('/group_users_by_group_id/<int:group_id>')
@studyfix.response(500, 'Wenn ein Server-seitiger Fehler aufkommt')
class GetGroupUsersByGroupId(Resource):
    @studyfix.marshal_with(user)
    def get(self, group_id):
        adm = Administration()
        result = adm.get_group_users_by_group_id(group_id)
        return result

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
    app.run(debug=True)


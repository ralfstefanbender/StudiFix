from flask import Flask
# Auf Flask aufbauend nutzen wir RestX
from flask_restx import Api, Resource, fields
# Wir benutzen noch eine Flask-Erweiterung für Cross-Origin Resource Sharing
from flask_cors import CORS

from server.Administration import Administration
from server.bo.ChatInvitation import ChatInvitation

from server.bo.ChatMessage import ChatMessage

from server.bo.GroupInvitation import GroupInvitation
from server.bo.LearningProfile import LearningProfile
from server.bo.StudyGroup import StudyGroup
from server.bo.User import User
from server.bo.Chat import Chat
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

StudiFix = api.namespace('StudiFix', description='Funktionen des StudiFix')



bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Unique id of a business object'),
    'creation_date': fields.DateTime(attribute='_creation_date', description='creation date of a business object')
})

nbo = api.inherit('NamedBusinessObject', bo, {
    'name': fields.String(attribute='_name', description='name of a named business object')
})

chatinvitation = api.inherit('ChatInvitation', bo, {
    'source_user':fields.Integer(attribute='_source_user', description='Unique Id des Chatinhabers'),
    'target_user':fields.Integer(attribute='_target_user', description='Unique Id des Einzuladenden'),
    'chat_id':fields.Integer(attribute='_chat_id', description='Chat id des Chats'),
    'is_accepted':fields.Boolean(attribute='_is_accepted', description='Akzeptierte Chateinladungen')
})

chatmessage = api.inherit('ChatMessage', bo, {
    'chat_id':fields.Integer(attribute='_chat_id', description='Unique Id des Chats'),
    'user_id':fields.Integer(attribute='_user_id', description='Unique Id des Versenders'),
    'text':fields.String(attribute='_text', description='Inhalt der Nachricht')
})

groupinvitation = api.inherit('GroupInvitation', bo, {
    'study_group_id':fields.Integer(attribute='_study_group_id', description='Unique Id der Gruppe'),
    'source_user':fields.Integer(attribute='_source_user', description='Unique Id des Chatinhabers'),
    'target_user':fields.Integer(attribute='_target_user', description='Unique Id des Einzuladenden'),
    'is_accepted':fields.Boolean(attribute='_is_accepted', description='Akzeptiert')
})

learningprofile = api.inherit('LearningProfile', nbo, {
    'frequency':fields.Integer(attribute='_frequency', description='Häufigkeit'),
    'studystate':fields.Integer(attribute='_studystate', description='on oder offline'),
    'extroversion':fields.Integer(attribute='_extroversion', description='extrovertiertheit'),
    'profile_id':fields.Integer(attribute='_profile_id', description='profile id'),
    'prev_knowledge':fields.Integer(attribute='_study_group_id', description='bisherige Kentnisse'),
    'lerntyp':fields.Integer(attribute='_lerntyp', description='Lerntypdes Profilinhabers'),
    'interest': fields.List(attribute='_interest', description='Interessen des Profilinhabers'),
    'semester': fields.Integer(attribute='_semester', description='Semester'),
    'degree_course':fields.String(attribute='_degree_course', description='Studiengang')
})

studygroup = api.inherit('StudyGroup', nbo, {
    'learning_profile_id':fields.Integer(attribute='_learning_profile_id', description='FK Learningprofile id'),
    'group_name':fields.String(attribute='_semester', description='Gruppenname'),
    'chat_id':fields.Integer(attribute='_chat_id', description='Chat id ')
})

user = api.api.inherit('User', nbo, {
    'google_id':fields.String(attribute='_google_id', description='Google Id des Profilinhabers'),
    'first_name':fields.String(attribute='_first_name', description='Vorname des Profilinhabers'),
    'last_name':fields.String(attribute='_last_name', description='Nachname des Profilinhabers'),
    'email':fields.String(attribute='_email', description='Email des Profilinhabers'),
    'adress':fields.String(attribute='_adress', description='Adresse des Profilinhabers')
})
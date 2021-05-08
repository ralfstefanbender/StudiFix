from flask import Flask
# Auf Flask aufbauend nutzen wir RestX
from flask_restx import Api, Resource, fields
# Wir benutzen noch eine Flask-Erweiterung für Cross-Origin Resource Sharing
from flask_cors import CORS

from server.Administration import Administration
from server.bo.Chat import Chat
from server.bo.ChatMessage import ChatMessage
from server.bo.GroupInvitation import GroupInvitation

from server.bo.LearningProfile import LearningProfile
from server.bo.StudyGroup import StudyGroup
from server.bo.User import User

app = Flask(__name__)


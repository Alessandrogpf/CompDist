from flask import Blueprint, redirect, Response
from flask_admin.contrib.sqla import ModelView
from werkzeug.exceptions import HTTPException
from .. import auth
from ..controllers.auth_controller import validate_authentication
from ..models.profile import Profile

custom_admin_bp = Blueprint('custom_admin', __name__)

class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))

class MyModelView(ModelView):
    def is_accessible(self):
        if auth.get_auth():
            username = auth.get_auth().get('username')
            password = auth.get_auth().get('password')
            if username and password:
                if validate_authentication(username, password):
                    return True
        raise AuthException('Not authenticated.')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(auth.login_required())

class ProfileView(MyModelView):
    column_exclude_list = ['password']
    column_searchable_list = ['username']
    can_export = True
    can_view_details = True

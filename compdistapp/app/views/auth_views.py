from flask import Blueprint, jsonify
from ..controllers.auth_controller import verify_password
from ..models.profile import Profile
from .. import auth

auth_bp = Blueprint('auth', __name__)
auth.verify_password(verify_password)

@auth_bp.route('/')
@auth.login_required
def index():
    user = auth.current_user()
    user_db = Profile.query.filter_by(username=user).first()

    if user_db:
        message_info = f"Usuário {user}, acessou o index."
        response = {"success": message_info}
        return jsonify(response)

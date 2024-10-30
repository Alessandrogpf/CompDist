from werkzeug.security import generate_password_hash, check_password_hash
from ..models.profile import Profile
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = Profile.query.filter(Profile.username == username)

    if user.all():
        user_query = user.all()[0]
        if check_password_hash(generate_password_hash(user_query.password), password):
            return username


def validate_authentication(username, password):
    user = Profile.query.filter(Profile.username == username)

    if user.all():
        user_query = user.all()[0]
        if user_query.password == password:
            return True
        return False
    return False

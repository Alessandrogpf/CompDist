from werkzeug.security import generate_password_hash, check_password_hash
from ..models.profile import Profile

# Verifica a senha de um usuário
def verify_password(username, password):
    user = Profile.query.filter_by(username=username).first()
    if user and check_password_hash(generate_password_hash(user.password), password):
        return username

# Valida a autenticação de um usuário para o acesso ao admin
def validate_authentication(username, password):
    user = Profile.query.filter_by(username=username).first()
    if user and user.password == password:
        return True
    return False

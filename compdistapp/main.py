import os
from app import create_app, db
from app.models.profile import Profile  # Importa o modelo para garantir que ele seja registrado

app = create_app()

def create_default_user():
    existing_user = Profile.query.filter_by(username="brivaldo").first()
    if not existing_user:
        new_user = Profile(username="brivaldo", password="123")
        db.session.add(new_user)
        db.session.commit()

if __name__ == "__main__":
    db_path = os.path.join(os.path.dirname(__file__), "app", "instance", "usersdb.sqlite3")

    with app.app_context():
        if not os.path.exists(db_path):
            db.create_all()  
        create_default_user() 

    app.run(host="0.0.0.0", port=8080)
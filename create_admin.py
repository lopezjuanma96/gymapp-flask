from gymapp import create_app
from gymapp.models.user import User

if __name__ == "__main__":
    with create_app().app_context():
        User.create_admin()

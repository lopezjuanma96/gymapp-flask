from ..database import db
from werkzeug.security import generate_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def create_admin(
            cls,
            username: str = "admin",
            password: str = "admin"
            ):
        hashed_password = generate_password_hash(password)
        admin = cls(username=username, password=hashed_password, admin=True)
        db.session.add(admin)
        db.session.commit()
        return admin

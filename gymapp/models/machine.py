from ..database import db


class Machine(db.Model):
    __tablename__ = 'machines'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256))
    image = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<Machine {}>'.format(self.name)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def check(self, check_id):
        return self.id == check_id

    def update(self):
        db.session.commit()

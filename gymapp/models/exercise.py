from ..database import db


class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256))
    video_url = db.Column(db.String(64), default=None)
    machine_id = db.Column(db.Integer, db.ForeignKey('machines.id'))

    machine = db.relationship(
        'Machine',
        backref=db.backref('exercises', lazy=True)
        )

    def __repr__(self):
        return '<Exercise {}>'.format(self.name)

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def from_template(cls, template, **kwargs):
        """
        Create an exercise from a template.
        On kwargs pass modifications to the template.
        """
        exercise = cls(
            name=template.name,
            description=template.description,
            video_url=template.video_url,
            machine=template.machine,
            **kwargs
            )
        return exercise


class ExerciseTemplate(db.Model):
    """
    Exercise templates will be uploaded by admins.
    """
    __tablename__ = 'exercise_templates'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256))
    video_url = db.Column(db.String(64), default=None)
    machine_id = db.Column(db.Integer, db.ForeignKey('machines.id'))

    machine = db.relationship(
        'Machine',
        backref=db.backref('exercise_templates', lazy=True)
        )

    def __repr__(self):
        return '<ExerciseTemplate {}>'.format(self.name)

    def add(self):
        db.session.add(self)
        db.session.commit()

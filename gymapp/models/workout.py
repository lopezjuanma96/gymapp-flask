from ..database import db


workout_exercises = db.Table(
    'workout_exercises',
    db.Column(
        'workout_id',
        db.Integer,
        db.ForeignKey('workout.id'),
        primary_key=True
        ),
    db.Column(
        'exercise_id',
        db.Integer,
        db.ForeignKey('exercise.id'),
        primary_key=True
        )
)


class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(64), nullable=False)
    creation = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(256))

    user = db.relationship('User', backref=db.backref('workouts', lazy=True))
    exercises = db.relationship(
        'Exercise',
        secondary=workout_exercises,
        backref=db.backref('workouts', lazy=True)
        )

    def __repr__(self):
        return '<Workout {}>'.format(self.name)

    def add(self):
        db.session.add(self)
        db.session.commit()

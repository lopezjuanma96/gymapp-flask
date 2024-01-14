from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class NewExerciseTemplateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=64)])
    description = StringField('Description', validators=[Length(max=256)])
    video_url = StringField('Video URL', validators=[Length(max=64)])
    machine_id = StringField('Machine ID', validators=[DataRequired()])
    submit = SubmitField('Submit')

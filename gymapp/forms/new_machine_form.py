from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class NewMachineForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(min=4, max=25)]
        )
    description = StringField(
        'Description',
        validators=[DataRequired(), Length(min=4, max=256)]
        )
    image = StringField(
        'Image',
        validators=[DataRequired(), Length(min=4, max=64)]
        )
    submit = SubmitField('Submit')

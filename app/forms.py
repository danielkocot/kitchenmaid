from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField
from wtforms.validators import DataRequired


class NewForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    stock = IntegerField('Stock', validators=[DataRequired()])
    best_before_date = DateField('Best before', format="%d.%m.%Y", validators=[DataRequired()])
    submit = SubmitField('Add')
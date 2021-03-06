# project/user/forms.py


from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from project.models import User


class LoginForm(Form):
    email = TextField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class RegisterForm(Form):
    email = TextField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True


class ChangePasswordForm(Form):
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
class InputForm(Form):
    region = TextField('region', validators=[DataRequired()])
    name = TextField('nm', validators=[DataRequired()])

class ProviderForm(Form):
    Snm = TextField(
    'Snm',
    validators=[DataRequired(), Length(min=2, max=40)])

    Rnm = TextField(
    'Rnm',
    validators=[DataRequired(), Length(min=6, max=40)])

    Anm = TextField(
    'Anm',
    validators=[DataRequired(), Length(min=6, max=40)])

    Cnm = TextField(
    'Cnm',
    validators=[DataRequired(), Length(min=3, max=40)])

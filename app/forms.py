from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, DateField, RadioField, IntegerField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class SigninForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=20)])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Signin")


# TODO rename the ffrom and ffor
class ReceiptForm(FlaskForm):
    ffrom = StringField("From", validators=[DataRequired(), Length(min=4, max=150)])
    ffor = StringField("For", validators=[DataRequired(), Length(min=4, max=150)])
    amount = IntegerField("Amount", validators=[DataRequired()])
    payment_type = RadioField("Payment Type", choices=["Cash", "Check"])
    date = DateField("Date", format='%Y-%m-%d')
    submit = SubmitField("Generate")
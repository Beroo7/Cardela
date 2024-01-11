from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize

from wtforms.fields import StringField, IntegerField, SubmitField, PasswordField, RadioField, DateField, SelectField
from wtforms.validators import DataRequired, length, equal_to

class AddProductForm(FlaskForm):
    name = StringField("Product Name", validators=[DataRequired(message="Product Name is required")])
    price = IntegerField("Product Price", validators=[DataRequired(message="Product Price is required")])
    img = FileField("Product Image",
                    validators=[
                        FileRequired(),
                        FileSize(max_size=1024 * 1024 * 20),
                        FileAllowed(["jpg", "png", "jpeg"], message="Allowed file types - jpg, png, jpeg")
                    ])

    submit = SubmitField("Submit")

#usrnm, pass, rpt_pass, gender, bd, cntr
class RegisterForm(FlaskForm):
    username = StringField("Enter Username")
    password = PasswordField("Enter Password", validators=[length(min=8, max=16)])
    repeat_password = PasswordField("Enter Password Again", validators=[equal_to("password", message="Passwords doesn't match")])
    gender = RadioField("Choose Gender", choices=["Male", "Female", "other"])
    birthday = DateField("Enter Birthday Date")
    country = SelectField("Enter Your Country", choices=["Choose Country", "Albania", "Croatia", "Georgia", "Germany", "United States", "United Kingdom"])

    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("Enter Username", validators=[DataRequired()])
    password = PasswordField("Enter Password", validators=[DataRequired(), length(min=8, max=16)])
    submit = SubmitField("Login")
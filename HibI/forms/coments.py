from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename


class ComentsForm(FlaskForm):
    author = TextAreaField("автор")
    content = TextAreaField("Помните что надо уважать соучастников сайта и нельзя их оскорблять, булить или кидать им спам в коментарии. Большое спасибо")
    submit = SubmitField('Прокоментировать')

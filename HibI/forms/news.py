from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание: ( здесь вы можете написать свой: код, стих, рассказ, рецепт или вообще, что угодно чем хотите поделиться")
    is_private = BooleanField("Личное")
    submit = SubmitField('Опубликовать')

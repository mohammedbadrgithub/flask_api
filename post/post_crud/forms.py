from flask_wtf import FlaskForm
from wtforms import StringField,FileField


class PostForm(FlaskForm):
    title = StringField('Title')
    body = StringField('Body')
    description = StringField('Description')
    image = FileField('Image')


class CategoryForm(FlaskForm):
    categoryName = StringField('Category Name')
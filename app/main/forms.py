from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo

class BlogForm(FlaskForm):

    blogTitle = StringField('Blog Title',validators=[Required()])
    blogDescription = StringField('Description',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment', validators=[Required()])
    submit = SubmitField('Submit')


class updateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself',validators = [Required()])
    submit = SubmitField('Submit')    

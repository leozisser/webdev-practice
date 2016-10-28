__author__ = 'Leo'
from flask_wtf import Form
from wtforms import TextField,BooleanField
from wtforms.validators import Required

class QuizForm(Form):
    answer_apple = TextField('your answer',validators= [Required()])
    answer_orange = TextField('your answer',validators= [Required()])

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)


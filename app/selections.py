from wtforms import SelectField
from flask_wtf import FlaskForm
from app.engravings import engrav_list

class Form(FlaskForm):
    engravings = SelectField('Engravings', choices=engrav_list)
    lvl = SelectField('Lvl', choices=[1,2,3])
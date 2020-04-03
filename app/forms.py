from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField, HiddenField
from wtforms import validators
from wtforms.validators import DataRequired
from werkzeug.datastructures import MultiDict

class MainForm(Form):
	HomeAddressTitle = StringField("My Home Address")		
	HomeAddress = StringField('Home Address', [validators.Required("Please enter suburb or home address.")],render_kw={"placeholder": "Enter your address","id":"geocomplete","size":"60"})	
	HomeLat = HiddenField(render_kw={"id":"home_lat"})	
	HomeLng = HiddenField(render_kw={"id":"home_lng"})		
	Submit1 = SubmitField('Submit',render_kw={"size":"90"})	    

class ResultForm(Form):
    Submit2 = SubmitField('Back',render_kw={"size":"90"})	 
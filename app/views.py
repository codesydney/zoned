from flask import render_template, flash, redirect, request, url_for
from app import app, db, models
from .forms import MainForm, ResultForm
from math import sin, cos, sqrt, atan2
from flask_bootstrap import Bootstrap

Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = MainForm()
	resultform = ResultForm()
	
	if form.validate_on_submit() and form.Submit1.data:
		HomeAddress = form.HomeAddress.data
		HomeLat = form.HomeLat.data
		HomeLng = form.HomeLng.data		
		
		#If no address inputted, geocode defaults to 100 Market St, Sydney
		if not HomeLat:
			HomeLat = "-33.8704510"
			HomeLng = "151.2087600"
			HomeAddress = "Invalid home address. Results are computed based on 100 Market St, Sydney NSW 2000"
		
		return render_template('result.html',
								resultform=resultform,
								HomeAddress=HomeAddress,
								HomeLat=HomeLat,
								HomeLng=HomeLng)
								
	elif resultform.validate_on_submit() and resultform.Submit2.data:	
         return redirect(url_for('index'))
	else:		
	    return render_template('mainform.html',
                                form=form)
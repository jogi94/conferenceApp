from django import forms
from django.db import models
from .models import *
from django.contrib.admin.widgets import *

class AvailabilityForm(forms.Form):
	roomCategory = (
		('Contact','Contact'),
		('Sharing','Sharing'),
		('Team','Team'),
		)
	room = forms.ChoiceField(choices=roomCategory,required=True)
	check_in = forms.TimeField()
	check_out = forms.TimeField()
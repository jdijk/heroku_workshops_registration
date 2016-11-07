from django.forms import ModelForm
from .models import *


class RegistrationForm(ModelForm):
	class Meta:
		model = Attendee
		fields = ['full_name', 'company', 'role', 'email']


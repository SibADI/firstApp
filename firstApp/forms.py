from django.forms import ModelForm
from .models import *

class MeetingForm(ModelForm):
	class Meta:
		model = Meeting
		fields = ('title', 'target', 'text', 'date', 'place', 'quest')
		#fields = "__all__"
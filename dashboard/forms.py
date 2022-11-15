import datetime

from django import forms
from django.forms import DateInput
from .models import Dashes

class DashesForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    deadline_at = forms.DateTimeField(required=True, widget=DateInput(attrs={'date':'datetime-local'}), initial=datetime.date.today(), localize=True)

class DashesFormm(forms.ModelForm):
    class Meta:
        model = Dashes
        fields = ('title','description','deadline_at')

    deadline_at = forms.DateTimeField(required=True, widget=DateInput(attrs={'date': 'datetime-local'}),
                                      initial=datetime.date.today(), localize=True)


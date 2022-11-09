from django import forms


class MyForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    deadline = forms.DateTimeField()


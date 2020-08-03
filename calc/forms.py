from django import forms
from calc.models import Credentials

class EntryForm(forms.ModelForm):

    class Meta:
        model = Credentials
        fields = '__all__'
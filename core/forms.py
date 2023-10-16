from django import forms
from .models import Client

class CSVUploadForm(forms.Form):
    file = forms.FileField()

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client

        fields = [
            "username",
            "tts_enabled"
        ]
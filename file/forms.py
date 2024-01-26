from django import forms
from .models import FileUpload
class imgForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['name','create']
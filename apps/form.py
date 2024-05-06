from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from apps.models import UploadImage


class RegisterModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'username']

    def clean_password(self):
        return make_password(self.cleaned_data.get('password'))


# forms.py


class VerificationForm(forms.Form):
    verification_code = forms.CharField(max_length=6, label='Verification Code')

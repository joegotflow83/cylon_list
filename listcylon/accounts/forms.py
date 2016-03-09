from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    city_preference = forms.CharField(max_length=128)

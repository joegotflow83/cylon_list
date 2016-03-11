from django import forms

from .models import Job, Car


class JobForm(forms.ModelForm):

    class Meta:

        model = Job
        fields = ['title', 'description', 'city', 'highlight_skills', 'plus_skills', 'compensation',
                  'employment_type', 'tags', 'image']


class CarForm(forms.ModelForm):

    class Meta:

        model = Car
        fields = ['title', 'description', 'city', 'brand', 'model', 'condition', 'cylinders', 'drive',
                  'odometer', 'color', 'transmission', 'car_type', 'price', 'tags', 'image']


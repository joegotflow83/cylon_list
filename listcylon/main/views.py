from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    """Display the users home page"""
    template_name = 'main/home.html'

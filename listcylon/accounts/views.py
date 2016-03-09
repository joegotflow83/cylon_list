from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView


class Signup(CreateView):
    """Allow a user to sign up"""
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login')

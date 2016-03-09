from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView

from .forms import SignUpForm
from .models import UserProfile


class Signup(CreateView):
    """Allow a user to sign up"""
    model = User
    form_class = SignUpForm

    def form_valid(self, form):
        """Validate the form"""
        new_user = form.save()
        UserProfile.objects.create(user=new_user, city_preference=form.cleaned_data['city_preference'])
        new_user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')


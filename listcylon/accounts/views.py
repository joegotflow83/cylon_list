from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView

from .forms import SignUpForm
from .models import UserProfile


class Signup(CreateView):
    """Allow a user to sign up"""
    model = User
    form_class = SignUpForm

    def form_valid(self, form):
        """Validate the form"""
        new_user = form.save()
        capitalized_city = form.cleaned_data['city_preference'].capitalize()
        UserProfile.objects.create(user=new_user, city_preference=capitalized_city)
        new_user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')


class UpdateCity(UpdateView):
    """A user can update what city they want to look in"""
    model = UserProfile
    fields = ['city_preference']
    template_name = 'accounts/userprofile_form.html'

    def form_valid(self, form):
        city = form.save(commit=False)
        city.city_preference = form.cleaned_data['city_preference'].capitalize()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

from .models import Job, Car
from .forms import JobForm, CarForm


class Home(TemplateView):
    """Display the users home page"""
    template_name = 'main/home.html'


class AllJobsCity(ListView):
    """Show all cities in the city of choice"""
    model = Job

    def get_queryset(self):
        return Job.objects.show_jobs_in_city(self.request.user)


class AccountingPosting(CreateView):
    """Allow users to post accounting jobs"""
    model = Job
    form_class = JobForm
    template_name = 'main/accounting_form.html'

    def form_valid(self, form):
        job = form.save(commit=False)
        job.user = self.request.user
        job.category = 'Accounting'
        job.city = form.cleaned_data['city'].capitalize()
        job.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class BuisnessPosting(CreateView):
    form_class = JobForm
    template_name = 'main/buisness_form.html'

    def form_valid(self, form):
        job = form.save(commit=False)
        job.user = self.request.user
        job.category = 'Buisness'
        job.city = form.cleaned_data['city'].capitalize()
        job.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class EducationPosting(CreateView):
    """Allow users to post education jobs"""
    model = Job
    form_class = JobForm
    template_name = 'main/education_form.html'

    def form_valid(self, form):
        job = form.save(commit=False)
        job.user = self.request.user
        job.category = 'Education'
        job.city = form.cleaned_data['city'].capitalize()
        job.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class RealEstatePosting(CreateView):
    """Allow users to post real estate jobs"""
    model = Job
    form_class = JobForm
    template_name = 'main/real_estate_form.html'

    def form_valid(self, form):
        job = form.save(commit=False)
        job.user = self.request.user
        job.category = 'Accounting'
        job.city = form.cleaned_data['city'].capitalize()
        job.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class GovernmentPosting(CreateView):
    """Allow users to post government jobs"""
    model = Job
    form_class = JobForm
    template_name = 'main/government_list.html'

    def form_valid(self, form):
        job = form.save(commit=False)
        job.user = self.request.user
        job.category = 'Government'
        job.city = form.cleaned_data['city'].capitalize()
        job.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class TechnologyPosting(CreateView):
    """Allow users to post technology jobs"""
    model = Job
    form_class = JobForm
    template_name = 'main/technology_form.html'

    def form_valid(self, form):
        job = form.save(commit=False)
        job.user = self.request.user
        job.category = 'Technology'
        job.city = form.cleaned_data['city'].capitalize()
        job.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class JobDetail(DetailView):
    """View all the details of a particular job"""
    model = Job


# Job listings by category
class AccountingJobs(ListView):
    """Display all accounting jobs"""
    model = Job
    template_name = 'main/accounting_list.html'

    def get_queryset(self):
        return Job.objects.order_by_job(self.request.user, "Accounting")


class AccountingThumbnail(ListView):
    """View all accounting jobs thumbnail version"""
    model = Job
    template_name = 'main/accounting_thumbnail.html'

    def get_queryset(self):
        return Job.objects.order_by_job(self.request.user, "Accounting")


class NewestAccounting(ListView):
    """Display the newest posts"""
    model = Job
    template_name = 'main/accounting_newest.html'

    def get_queryset(self):
        return Job.objects.newest_posts(self.request.user, "Accounting")


class HighestAccounting(ListView):
    """Display the highest accounting jobs"""
    model = Job
    template_name = 'main/accounting_high_price.html'

    def get_queryset(self):
        return Job.objects.highest_price(self.request.user, "Accounting")


class LowestAccounting(ListView):
    """Display the lowest accounting jobs"""
    model = Job
    template_name = 'main/accounting_low_price.html'

    def get_queryset(self):
        return Job.objects.lowest_price(self.request.user, "Accounting")


class BuisnessJobs(ListView):
    """Display all buisness jobs"""
    model = Job
    template_name = 'main/buisness_list.html'

    def get_queryset(self):
        return Job.objects.order_by_job(self.request.user, 'Buisness')


class EducationJobs(ListView):
    """Display all education jobs"""
    model = Job
    template_name = 'main/education_list.html'

    def get_queryset(self):
        return Job.objects.order_by_job(self.request.user, 'Education')


class RealEstateJobs(ListView):
    """Display all real estate jobs"""
    model = Job
    template_name = 'main/real_estate_list.html'

    def get_queryset(self):
        return Job.objects.order_by_job(self.request.user, 'Real Estate')


class GovernmentJobs(ListView):
    """Display all government jobs"""
    model = Job
    template_name = 'main/government_list.html'

    def get_queryset(self):
        return Job.objects.order_by_job(self.request.user, 'Government')


class TechnologyJobs(ListView):
    """Display all tech jobs"""
    model = Job
    template_name = 'main/technology_list.html'

    def get_queryset(self):
        return Job.objects.order_by_job(self.request.user, 'Technology')


class DisplayCityJobs(ListView):
    """Display all jobs in the city"""
    model = Job

    def get_queryset(self):
        return Job.objects.show_jobs_in_city(self.request.user)


# Car Listings
class AcuraPosting(CreateView):
    """Add an acura post"""
    model = Car
    form_class = CarForm
    template_name = 'main/acura_form.html'

    def form_valid(self, form):
        car = form.save(commit=False)
        car.user = self.request.user
        car.city = form.cleaned_data['city'].capitalize()
        car.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class AudiPosting(CreateView):
    """Add an audi post"""
    model = Car
    form_class = CarForm
    template_name = 'main/audi_form.html'

    def form_valid(self, form):
        car = form.save(commit=False)
        car.user = self.request.user
        car.city = form.cleaned_data['city'].capitalize()
        car.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class BMWPosting(CreateView):
    """Add a bmw post"""
    model = Car
    form_class = CarForm
    template_name = 'main/bmw_form.html'

    def form_valid(self, form):
        car = form.save(commit=False)
        car.user = self.request.user
        car.city = form.cleaned_data['city'].capitalize()
        car.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class BuickPosting(CreateView):
    """Add a buick post"""
    model = Car
    form_class = CarForm
    template_name = 'main/buick_form.html'

    def form_valid(self, form):
        car = form.save(commit=False)
        car.user = self.request.user
        car.city = form.cleaned_data['city'].capitalize()
        car.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class Acura(ListView):
    """Display all acura cars"""
    model = Car
    template_name = 'main/acura_list.html'

    def get_queryset(self):
        return Car.objects.order_by_brand(self.request.user, 'Acura')


class Audi(ListView):
    """Display all audi cars"""
    model = Car
    template_name = 'main/audi_list.html'

    def get_queryset(self):
        return Car.objects.order_by_brand(self.request.user, 'Audi')


class BMW(ListView):
    """Display all BMW cars"""
    model = Car
    template_name = 'main/bmw_list.html'

    def get_queryset(self):
        return Car.objects.order_by_brand(self.request.user, 'BMW')


class Buick(ListView):
    """Display all buick cars"""
    model = Car
    template_name = 'main/buick_list.html'

    def get_queryset(self):
        return Car.objects.order_by_brand(self.request.user, 'Buick')


class CarDetail(DetailView):
    """View a car post in detail"""
    model = Car


class AllCarsCity(ListView):
    """Show all cars in the city provided"""
    model = Car

    def get_queryset(self):
        return Car.objects.show_cars_in_city(self.request.user)

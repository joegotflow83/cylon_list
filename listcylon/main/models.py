from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

from taggit.managers import TaggableManager


brands = (
    ('Acura', 'Acura'),
    ('Audi', 'Audi'),
    ('BMW', 'BMW'),
    ('Buick', 'Buick'),
    ('Cheverolet', 'Cheverolet'),
    ('Dodge', 'Dodge'),
    ('Ferrai', 'Ferrai'),
    ('Ford', 'Ford'),
    ('Lamborghini', 'Lamborghini'),
    ('Mclaren', 'Mclaren'),
    ('Mercedes', 'Mercedes'),
    ('Mitusbishi', 'Mitsubishi'),
    ('Pagani', 'Pagani'),
    ('Porsche', 'Porsche'),
    ('Subaru', 'Subaru'),
    ('Tesla', 'Tesla'),
    ('Volkswagen', 'Volkwagen')
)

categories = (
    ('Accounting', 'Accounting'),
    ('Buisness', 'Buisness'),
    ('Education', 'Education'),
    ('Real Estate', 'Real Estate'),
    ('Government', 'Government'),
    ('Technology', 'Technology')
)


class CarManager(models.Manager):

    def show_cars_in_city(self, user):
        """Show the cars in the city the user has chosen"""
        return self.filter(city=user.userprofile.city_preference)

    def order_by_brand(self, user, brand):
        """Display the cars by brand"""
        return self.filter(Q(brand=brand), Q(city=user.userprofile.city_preference))


class JobManager(models.Manager):

    def show_jobs_in_city(self, user):
        """Show the jobs in the city the user has chosen"""
        return self.filter(city=user.userprofile.city_preference)

    def order_by_job(self, user, category):
        """Display jobs by category"""
        return self.filter(Q(category=category), Q(city=user.userprofile.city_preference))

    def newest_posts(self, user, category):
        """Display the newest posts"""
        return self.filter(Q(category=category), Q(city=user.userprofile.city_preference)).order_by('-created')

    def highest_price(self, user, category):
        """Display the highest compensation jobs"""
        return self.filter(Q(category=category), Q(city=user.userprofile.city_preference)).order_by('-compensation')

    def lowest_price(self, user, category):
        """Display the lowest compensation jobs"""
        return self.filter(Q(category=category), Q(city=user.userprofile.city_preference)).order_by('compensation')


class HouseManager(models.Manager):

    def show_houses_in_city(self, user):
        """Show the houses in the city the user has chosen"""
        return self.filter(city=user.userprofile.city_preference)


class Post(models.Model):

    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)


class Car(Post):

    brand = models.CharField(max_length=64, choices=brands)
    model = models.CharField(max_length=64)
    condition = models.CharField(max_length=255)
    cylinders = models.CharField(max_length=32)
    drive = models.CharField(max_length=3)
    odometer = models.CommaSeparatedIntegerField(max_length=8)
    color = models.CharField(max_length=32)
    transmission = models.CharField(max_length=20)
    car_type = models.CharField(max_length=32)
    price = models.CommaSeparatedIntegerField(max_length=15)
    tags = TaggableManager()

    objects = CarManager()


class Job(Post):

    category = models.CharField(max_length=64, choices=categories)
    highlight_skills = models.CharField(max_length=255)
    plus_skills = models.CharField(max_length=255)
    compensation = models.CharField(max_length=12)
    employment_type = models.CharField(max_length=15)
    tags = TaggableManager()

    objects = JobManager()


class House(Post):

    condition = models.CharField(max_length=255)
    year_built = models.IntegerField()
    beds = models.IntegerField()
    baths = models.FloatField()
    square_feet = models.CommaSeparatedIntegerField(max_length=7)
    price = models.CommaSeparatedIntegerField(max_length=15)
    mortgage = models.CommaSeparatedIntegerField(max_length=7)
    tags = TaggableManager()

    objects = HouseManager()


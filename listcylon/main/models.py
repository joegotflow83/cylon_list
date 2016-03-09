from django.db import models
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


class Post(models.Model):

    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Car(Post):

    brand = models.CharField(max_length=64, choices=brands)
    model = models.CharField(max_length=64)
    condition = models.CharField(max_length=255)
    cylinders = models.CharField(max_lenth=32)
    drive = models.CharField(max_length=3)
    odometer = models.CommaSeparatedIntegerField()
    color = models.CharField(max_lenth=32)
    transmission = models.CharField(max_length=20)
    car_type = models.CharField(max_length=32)
    price = models.CommaSeparatedIntegerField()
    tags = TaggableManager()


class Job(Post):

    category = models.CharField(max_length=64, choices=categories)
    highlight_skills = models.CharField(max_length=255)
    plus_skills = models.CharField(max_length=255)
    compensation = models.CharField(max_length=12)
    employment_type = models.CharField(max_length=15)
    tags = TaggableManager()


class House(Post):

    condition = models.CharField(max_length=255)
    year_built = models.IntegerField()
    beds = models.IntegerField()
    baths = models.FloatField()
    square_feet = models.CommaSeparatedIntegerField()
    price = models.CommaSeparatedIntegerField()
    mortgage = models.CommaSeparatedIntegerField()
    tags = TaggableManager()


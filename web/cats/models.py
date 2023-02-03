from django.db import models
from django.urls import reverse

from datetime import date
import re
import math


class Cat(models.Model):
    SEX_CHOICES = [('m','male'), ('f','female')]
    
    name = models.CharField(max_length=20)
    approximate_date_of_birth = models.DateField(default = date(1900, 1, 1)) 
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    health_status = models.CharField(max_length=100)
    
    def calculate_age(self):
        birthdate = self.approximate_date_of_birth
        today = date.today()
        age_months = (today - birthdate).days /30

        if age_months >= 1 and age_months < 12:
            # For a kitten we need it's age in months.
            # Min. age of a kitten for adoption is 1 month, so we don't expect user to submit a kitten younger than that.
            return '{:.0f} months'.format(age_months)
        else:
            # For an adult cat (older than 1 year) we need it's age in years.
            age_years = age_months /12
            if re.search(r"\.[0-4]", str(age_years)):
                # Age is rounded down if the first decimal of age_years is < 5
                return '{:.0f} years'.format(age_years)
            else:
                # Age is rounded up if the first decimal of age_years is >= 5 
                return '{:.0f},5 years'.format(math.floor(age_years))
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cats:profile', kwargs={'pk' : self.pk})


class Photo(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='cats/photos')

from django.db import models
from django.urls import reverse

from datetime import date


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
            self.age = '{:.0f} months'.format(age_months)
        else:
            age_years = age_months /12
            self.age = '{:.0f} years'.format(age_years)
        return self.age
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cats:profile', kwargs={'pk' : self.pk})


class Photo(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='cats/photos')

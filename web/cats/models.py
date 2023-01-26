from django.db import models

# Create your models here.

class Cat(models.Model):
    SEX_CHOICES = [('m','male'), ('f','female')]
    
    name = models.CharField(max_length=20)
    # we need years and months as well if its a kitten
    # don't know how to make it yet
    age = models.IntegerField()    
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    health_status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Photo(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()

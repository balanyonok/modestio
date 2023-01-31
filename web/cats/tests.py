from django.test import TestCase
from .models import Cat
from datetime import date

class CatModelTest(TestCase):

    def test_calculate_age_with_1month_old_kitten(self):
        # Returns calculated age of a kitten in months (string)
        kitten = Cat(approximate_date_of_birth = date(2023, 1, 1))
        self.assertEqual(kitten.calculate_age(), '1 months')


    def test_calculate_age_3years_old_cat(self):
        # Returns calculated age of a the cat in years (string)
        adult_cat = Cat(approximate_date_of_birth = date(2020, 1, 1))
        self.assertEqual(adult_cat.calculate_age(), '3 years')

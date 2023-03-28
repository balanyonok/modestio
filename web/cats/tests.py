from django.test import TestCase
from .models import Cat
from datetime import date

from mock import patch, Mock


class CatModelTest(TestCase):
    @patch("cats.models.date")
    def test_calculate_age_with_1month_old_kitten(self, date_class_mock):
        # Returns calculated age of a kitten in months (string)
        date_class_mock.today = Mock(return_value=date(2023, 2, 1))
        kitten = Cat(approximate_date_of_birth=date(2023, 1, 1))
        self.assertEqual(kitten.calculate_age(), "1 months")

    @patch("cats.models.date")
    def test_calculate_age_3years_old_cat(self, date_class_mock):
        # Returns calculated age of a the cat in years (string)
        date_class_mock.today = Mock(return_value=date(2023, 2, 1))
        adult_cat = Cat(approximate_date_of_birth=date(2020, 1, 1))
        self.assertEqual(adult_cat.calculate_age(), "3 years")

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Cat


class AvailableCatsView(generic.ListView):
    """
    Return the list of cats submitted by admin(pani Kockova)
    with every cat's name, age and 1 picture.
    """

    model = Cat
    template_name = "cats/cats_for_adoption.html"
    context_object_name = "available_cats"

    def get_queryset(self):
        return Cat.objects.all


class CatProfileView(generic.DetailView):
    """
    Return the chosen cat profile
    with all the details including up to 10 pictures.
    """

    model = Cat
    template_name = "cats/cat_profile.html"

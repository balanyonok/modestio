from django.urls import path
from . import views

app_name = 'cats'
urlpatterns = [
    # /cats/
    path('', views.AvailableCatsView.as_view(), name='list'),
    # /cats/1/
    path('<int:pk>/', views.CatProfileView.as_view(), name='profile'),
]
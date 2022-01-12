from django.urls import path
from .views import HomePageView
from . import views


urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-details'),
    path('home/', HomePageView.as_view(), name='home'),
    ]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'), 
    path('tours', views.tours, name='tours'),
    path('feedbacks', views.feedbacks, name='feedbacks'),
    path('contacts', views.contacts, name='contacts')
]
from django.urls import path
from .views import home

urlpatterns = [
    path('', name='home', view=home),
]

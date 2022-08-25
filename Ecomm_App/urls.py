from django.urls import path

from Ecomm_App.views import index

urlpatterns = [
    path('', index, name='index'),
]
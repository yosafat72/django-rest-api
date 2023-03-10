from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save', views.save, name='save'),
    path('findById', views.findById, name='findById')
]

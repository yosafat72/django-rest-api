from django.shortcuts import render
from django.http import HttpResponse
from django_api.response import Response
from . import transformer
from .models import Users


# Create your views here.
def index(request):
    user = Users.objects.all()
    user = transformer.transform(user)
    return Response.ok(values=user, message="Successfully fetched data")

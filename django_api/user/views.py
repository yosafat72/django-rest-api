from django.shortcuts import render
from django.http import JsonResponse
from django_api.response import Response
from django_api.utils import Utils
from . import transformer
from .models import Users
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        user = Users.objects.all()
        user = transformer.transform(user)
        return Response.ok(values=user, message="Successfully fetched data")
    else:
        return Response.badRequest(message="Bad request")


@csrf_exempt
def save(request):
    if request.method == 'POST':
        requestData = json.loads(request.body)

        user = Users()
        user.id = Utils.randomStringForId()
        user.address = requestData['address']
        user.dob = requestData['dob']
        user.email = requestData['email']
        user.gender = requestData['gender']
        user.name = requestData['name']
        user.phone = requestData['phone']
        user.save()

        return Response.ok(values=transformer.singleTransform(user), message="Successfully added data")
    else:
        return Response.badRequest(message="Bad request")


@csrf_exempt
def findById(request):
    if request.method == 'POST':
        requestData = json.loads(request.body)

        user = Users.objects.filter(id=requestData['id']).first()

        if not user:
            return Response.ok(message="User not found")

        user = transformer.singleTransform(user)
        return Response.ok(values=user, message="User found")
    else:
        return Response.badRequest(message="Bad request")

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return JsonResponse({"msg": "This is the socials API."})

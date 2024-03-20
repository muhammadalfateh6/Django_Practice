from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show_home(request):
    return HttpResponse('This is littlelemon')

def home_page(request):
    return HttpResponse('Home Page')

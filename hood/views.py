from django.shortcuts import render
from django.http import HttpResponse
from .decorators import user_has_hood

def home_page(request):

  return render(request,'home.html')
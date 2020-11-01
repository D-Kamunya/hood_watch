from django.shortcuts import render
from django.http import HttpResponse
from .decorators import user_has_hood
from .models import NeighbourHood
def home_page(request):


  hoods=NeighbourHood.get_all_neighbourhoods()
  context={
    'hoods':hoods
  }
  return render(request,'home.html',context)
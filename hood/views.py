from django.shortcuts import render,redirect
from django.http import HttpResponse
from .decorators import user_has_hood
from .models import NeighbourHood
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F

@login_required(login_url='/accounts/login/')
def home_page(request):


  hoods=NeighbourHood.get_all_neighbourhoods()
  context={
    'hoods':hoods
  }
  return render(request,'home.html',context)



@login_required(login_url='/accounts/login/')
def join_hood(request,hood_id):
  hood=NeighbourHood.find_neighbourhood(hood_id)
  Profile.objects.filter(user=request.user).update(neighbourhood=hood)
  NeighbourHood.objects.filter(id=hood_id).update(hood_occupants=F("hood_occupants") + 1)  
  messages.success(request, f'You joined {hood.hood_name} neighbourhood.')
  return redirect ('home_page')
from django.urls import path
from . import views


urlpatterns=[
  path('',views.home_page,name='home_page'),
  path('join/hood/<hood_id>',views.join_hood,name='join_hood')
]
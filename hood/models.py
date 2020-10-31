from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
import datetime as dt

class NeighbourHood(models.Model):
    hood_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    hood_photo = ImageField(blank=True, manual_crop="")
    hood_name = models.TextField(max_length=500)
    hood_location = models.CharField(max_length=60, blank=True)
    hood_occupants = models.IntegerField(default=0)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hood_name

    class Meta:
        ordering = ['create_at'] 

    def create_neighbourhood(self):
      '''
      Saves NeighbourHood instance to db
      '''
      self.save()

    @classmethod
    def delete_neighbourhood(cls,hood_id):
      '''
      Deletes NeighbourHood based on its id
      '''
      cls.objects.filter(id=hood_id).delete()
      

    @classmethod
    def get_all_neighbourhoods(cls):
      '''
      Returns all NeighbourHood objects from db
      '''
      hoods=cls.objects.all()
      return hoods 


    @classmethod
    def find_neighbourhood(cls,hood_id):
      '''
      Returns NeighbourHood based on its id
      '''
      hood=cls.objects.get(id=hood_id)
      return hood



        
      


   
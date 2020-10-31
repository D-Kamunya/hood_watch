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


class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
    bs_name = models.TextField(max_length=120)
    bs_description = models.TextField(blank=True)
    bs_photo = ImageField(blank=True, manual_crop="")
    bs_email = models.EmailField(max_length=254)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bs_name

    class Meta:
        ordering = ['create_at'] 

    def create_business(self):
      '''
      Saves Business instance to db
      '''
      self.save()

    def delete_business(self):
      '''
      Deletes Business instance from db
      '''
      self.delete()
      

    @classmethod
    def get_all_bs_by_hood(cls,hood_id):
      '''
      Returns all Businesses in the hood objects from db
      '''
      bs=cls.objects.filter(neighbourhood_id=hood_id)
      return bs 


    @classmethod
    def find_business(cls,bs_id):
      '''
      Returns Business based on its id
      '''
      bs=cls.objects.get(id=bs_id)
      return bs


    @classmethod
    def search_business(cls, name,hood_id):
      '''
      Returns Business search based on its name and user neighbourhood
      '''
      return cls.objects.filter(bs_name__icontains=name , neighbourhood_id=hood_id)








        
      


   
from django.db import models
from django.contrib.auth.models import User
import datetime as dt

class NeighbourHood(models.Model):
    hood_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    hood_name = models.TextField(max_length=500)
    hood_location = models.CharField(max_length=60, blank=True)
    hood_occupants = models.IntegerField(default=0)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hood_name

from django import forms
from django.contrib.auth.models import User
from .models import Business,Post
from pyuploadcare.dj.forms import ImageField


class BusinessForm(forms.ModelForm):
    bs_photo = ImageField(label='')
    widgets = {
          "bs_name":forms.TextInput(attrs={"class":"form-control mb-4"}),
          "bs_description":forms.Textarea(attrs={'cols': 110, 'rows': 15,"class":"form-control mb-4"}),
          "bs_email":forms.TextInput(attrs={"class":"form-control mb-4"}),
      }

    class Meta:
        model = Business
        fields = ('bs_name','bs_description','bs_email', 'bs_photo')


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'neighbourhood']
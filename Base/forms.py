from .models import *
from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from django.db import transaction



class CustomerSignUpForm(UserCreationForm):
    # first_name = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username","password1","password2"]
    
    @transaction.atomic
    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.save()
        return user


class RestaurantOwnerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username","password1","password2"]

    @transaction.atomic
    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.is_restaurantowner = True
        user.save()
        restaurantowner = RestaurantOwner.objects.create(user=user)
        restaurantowner.save()
        return user

# class RestaurantRegisterForm(ModelForm):
#     class Meta:
#         model = Restaurant
#         fields = ["restaurant_name","description","profile_picture"]
#     profile_picture = forms.ImageField()

class RestaurantRegisterForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['restaurant_name', 'description', 'profile_picture']

    profile_picture = forms.ImageField()
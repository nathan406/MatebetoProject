from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_restaurantowner = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

class RestaurantOwner(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True,unique=True)


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=100,null=True,blank=False)
    restaurant_groups = models.ManyToManyField(Group, related_name='restaurant_groups')
    profile_picture = models.ImageField(null=True,blank=True)
    description = models.TextField(null=True,blank=True,max_length=2000)
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True )
    
    # updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    
    # class Meta:
    #     ordering = ['-updated','-created']

    def __str__(self) :
        return self.restaurant_name


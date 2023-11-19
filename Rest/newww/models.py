from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Data(models.Model):
    rest_icon=models.CharField(max_length=100)
    rest_name=models.CharField(max_length=100)
    rest_description=models.TextField()
    rest_rating=models.DecimalField(max_digits=2,decimal_places=1,default=3.0)
    rest_image=models.ImageField(upload_to="static/images",default="")


class Review(models.Model):
    rest_user_name = models.CharField(max_length=100,default="")
    rest_name=models.CharField(max_length=100,default="")
    rest_rating=models.DecimalField(max_digits=2,decimal_places=1)
    rest_review=models.TextField()

class FavRest(models.Model):
    rest_user_name = models.CharField(max_length = 100,default=None,blank=True)
    rest_hotel_name = models.CharField(max_length = 100,default=None,blank=True)

# class Signin(models.Model):
#     Username=models.CharField(max_length=100)
#     Phonenumer=models.IntegerField(max_length=10)
#     Email=models.EmailField(max_length=50)
#     Password=models.CharField(max_length=100)
# class Fav(models.Model):
#     favourites=models.ManyToManyField(User,related_name='favourite',default=None,blank=True)

class Reviews(models.Model):
    rest_username = models.CharField(max_length=100,default="")
    restname=models.CharField(max_length=100,default="")
    restrating=models.DecimalField(max_digits=2,decimal_places=1)
    restreview=models.TextField()
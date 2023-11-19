from django.db import models

# Create your models here.

class Review(models.Model):
    review=models.TextField()
    rating=models.IntegerField(max_length=2)
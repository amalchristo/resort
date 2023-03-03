from django.db import models

# Create your models here.
class Resort_admin(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
class Add_room(models.Model):
    room_name = models.CharField(max_length=50)
    room_capacity = models.CharField(max_length=50)
    room_photo = models.ImageField(upload_to = 'room/')
    room_price = models.CharField(max_length=100)
    room_description = models.CharField(max_length=1000)
    
class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    aadhaar_card = models.CharField(max_length=50)
    Qualification = models.CharField(max_length=50)
    agg = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='staff/')
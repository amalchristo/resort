from django.db import models

# Create your models here.
class Review(models.Model):
    add_review = models.CharField(max_length=500)
    
class Customer(models.Model):
    customer_username = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=50)
    customer_password = models.CharField(max_length=50)
    
class Bookroom(models.Model):
    book_name = models.CharField(max_length=100)
    book_email = models.CharField(max_length=100)
    check_in = models.CharField(max_length=50)
    check_out = models.CharField(max_length=50)
    
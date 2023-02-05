from django.db import models

class Reviews(models.Model):
    fio = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateTimeField()
    email = models.EmailField(max_length=250)

class Menu(models.Model):
    dish_photo = models.ImageField()
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    consist = models.TextField()

class Feedback(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=15)

class PhotoGallery(models.Model):
    photo = models.ImageField()

class Reserve(models.Model):
    fio = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)

class Banner(models.Model):
    photo = models.ImageField()
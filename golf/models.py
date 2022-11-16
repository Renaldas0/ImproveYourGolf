from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

CLASS_CHOICES = (('Short_game', 'Short_game'),
                 ('Kids_club', 'Kids_club'),
                 ('Long_game', 'Long_game'))


CLASS_STATUS = (('Fully_Booked', 'Fully_Booked'),
                ('Available', 'Available'))


class ClassName(models.Model):

    class_name = models.CharField(
        max_length=15, choices=CLASS_CHOICES, primary_key=True)

    def __str__(self):
        return str(self.class_name)


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, default='')

    def __str__(self):
        return self.name


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, default=True)
    class_name = models.ForeignKey(
        'ClassName', on_delete=models.CASCADE, default=True)
    status = models.CharField(
        max_length=15, choices=CLASS_STATUS, default='Available')
    places = models.IntegerField(default=True, null=False, validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])

    def __str__(self):
        return str(self.class_name)

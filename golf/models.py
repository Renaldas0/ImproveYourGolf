from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

CLASS_CHOICES = (('Short_game', 'Short_game'),
                 ('Kids_club', 'Kids_club'),
                 ('Long_game', 'Long_game'))


CLASS_STATUS = (('Fully_Booked', 'Fully_Booked'),
                ('Available', 'Available'))


OPTION_STATUS = (('y', 'Yes'), ('n', 'No'), ('p', 'Pending'))


class ClassName(models.Model):

    class_name = models.CharField(
        max_length=15, choices=CLASS_CHOICES, primary_key=True)

    def __str__(self):
        return str(self.class_name)


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, default='')

    def __str__(self):
        return self.username


class Booking(models.Model):

    class Meta:
        verbose_name_plural = 'Bookings'

    booking_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)
    class_name = models.ForeignKey(
        ClassName, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=15, choices=CLASS_STATUS, default='Available')
    places = models.IntegerField(default=True, null=False, validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])
    requested_date = models.DateField()
    bookingtatus = models.CharField(
        max_length=10, default='p', choices=OPTION_STATUS)

    def __str__(self):
        return str(self.class_name)

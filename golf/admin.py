"""Imports"""
from django.contrib import admin
from .models import Customer, ClassName, Booking

# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Customer Admin"""
    list_display = ('customer_id', 'username', 'email',)


@admin.register(ClassName)
class ClassNameAdmin(admin.ModelAdmin):
    """Classname Admin"""
    list_display = ('class_name',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Booking Admin"""
    search_fields = ['class_name']
    list_filter = ('class_name', 'status')
    list_display = ('booking_id', 'class_name', 'customer', 'status',
                    'requested_date',)

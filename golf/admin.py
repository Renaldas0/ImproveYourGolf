"""Imports"""
from django.contrib import admin
from .models import Customer, ClassName, Booking

# Register your models here.


admin.site.register(Customer)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'full_name', 'email',)


admin.site.register(ClassName)


class ClassNameAdmin(admin.ModelAdmin):
    list_display = ('classes',)


admin.site.register(Booking)


class BookingAdmin(admin.ModelAdmin):
    search_fields = ['class_name']
    list_filter = ('class_name', 'status')
    list_display = ('booking_id', 'class_name', 'customer', 'status',
                    'requested_date',)

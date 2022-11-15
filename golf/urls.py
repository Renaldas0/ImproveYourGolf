"""Imports"""
from django.urls import path
from golf import views


urlpatterns = [
    path('manage_booking', views.ManageBooking.as_view(),
         name='manage_booking'),
    path('delete_booking/<booking_id>',
         views.DeleteBooking.as_view(), name='delete_booking'),
    ]

from django.contrib import admin
from django.urls import path, include
from golf.views import main_page
from golf import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main_page'),
    path('accounts/', include('allauth.urls')),
    path('booking/', views.booking, name='booking'),
    path('delete_booking/', views.delete_booking, name='delete_booking')
]

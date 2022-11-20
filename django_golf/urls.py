from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import handler403, handler404, handler500
from golf import views
from golf.views import main_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main_page'),
    path('accounts/', include('allauth.urls')),
    path('booking/', include(
        'golf.urls'), name='golf_urls'),
]

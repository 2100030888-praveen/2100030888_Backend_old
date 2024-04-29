
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name = 'home'),
    path('insert_record_country/', insert_record_country, name='insert_record_country'),
    path('insert_record/', insert_record, name='insert_record'),
    path('get_canada/', get_canada, name='get_canada'),

    path('save_location/', save_location, name='save_location'),

    path('save_country/', save_country, name='save_country'),  # Add this line for the save_country view

]

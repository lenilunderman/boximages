from django.contrib import admin

# Register your models here.
from .models import ImageGallery

# Register on the admin dashboard part of the website
admin.site.register(ImageGallery)

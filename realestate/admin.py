from django.contrib import admin
from . models import PropertyListing, PropertyImage, Neighborhood, Home_Type, PriceRange

# Register your models here.

admin.site.register(PropertyListing)

admin.site.register(PropertyImage)

admin.site.register(Neighborhood)

admin.site.register(Home_Type)

admin.site.register(PriceRange)
from django.contrib import admin
from .models import Property, Neighborhood, Zipcode
# Register your models here.

admin.site.register(Property)
admin.site.register(Neighborhood)
admin.site.register(Zipcode)
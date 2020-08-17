from django.contrib import admin
from .models import State, Senator, Senate_Bill

myModels = [State, Senator, Senate_Bill]
admin.site.register(myModels)
from django.contrib import admin
from .models import Drinks
from .models import Food

admin.site.register(Drinks)
admin.site.register(Food)
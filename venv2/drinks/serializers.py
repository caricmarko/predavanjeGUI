from rest_framework import serializers
from .models import Drinks,Food

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Drinks
        fields=['id','name','description']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Food
        fields=['id','name','description']


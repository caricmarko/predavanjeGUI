from django.http import JsonResponse
from .models import Drinks,Food
from .serializers import DrinkSerializer,FoodSerializer
from rest_framework.response import Response
from rest_framework import status
from urllib import response
from rest_framework.decorators import api_view

@api_view(['GET'])
def drink_list(request):
    drinks = Drinks.objects.all()
    serializer = DrinkSerializer(drinks,many=True)
    #return JsonResponse({"drinks":serializer.data})
    return Response({"drink":serializer.data})

@api_view(['GET', 'PUT','DELETE'])
def drink_detail(request,id):
    try:
        drink = Drinks.objects.get(pk=id)
    except Drinks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method=='GET'):
        serializer = DrinkSerializer(drink)
        return Response({"drink":serializer.data})
    elif(request.method=='PUT'):
        serializer = DrinkSerializer(drink,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='DELETE'):
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def food_list(request):
    food = Food.objects.all()
    serializer = FoodSerializer(food,many=True)
    return JsonResponse({"food":serializer.data})

def food_detail(request,id):
    try:
        drink = Food.objects.get(pk=id)
    except Food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = FoodSerializer(drink)
    return JsonResponse({"food":serializer.data})
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework import status

from inventory_shoe.models import Inventory_shoe
from inventory_shoe.serializers import Inventory_shoeSerializer
from rest_framework.decorators import api_view


# API views defined below:

@api_view(['GET', 'POST', 'DELETE'])
def inventory_shoe_list(request):
    if request.method == 'GET':
        inventory_shoes = Inventory_shoe.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            inventory_shoes = inventory_shoes.filter(name__icontains=name)

        inventory_shoes_serializer = Inventory_shoeSerializer(inventory_shoes, many=True)
        return JsonResponse(inventory_shoes_serializer.data, safe=False)
    elif request.method == 'POST':
        inventory_shoe_data = JSONParser().parse(request)
        inventory_shoe_serializer = Inventory_shoeSerializer(data=inventory_shoe_data)
        if inventory_shoe_serializer.is_valid():
            inventory_shoe_serializer.save()
            return JsonResponse(inventory_shoe_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(inventory_shoe_serializer.errors, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Inventory_shoe.objects.all().delete()
        return JsonResponse({'message': '{} all data inventory deleted successfully'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT','PATCH', 'DELETE'])
def inventory_shoe_detail(request, pk):
    try:
        inventory_shoe = Inventory_shoe.objects.get(pk=pk)
    except Inventory_shoe.DoesNotExist:
        return JsonResponse({'message': 'the data does not exist!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        inventory_shoe_serializer = Inventory_shoeSerializer(inventory_shoe)
        return JsonResponse(inventory_shoe_serializer.data)
    elif request.method == 'PUT':
        inventory_shoe_data = JSONParser().parse(request)
        inventory_shoe_deserializer = Inventory_shoeSerializer(inventory_shoe, data=inventory_shoe_data)
        if inventory_shoe_deserializer.is_valid():
            inventory_shoe_deserializer.save()
            return JsonResponse(inventory_shoe_deserializer.data)
        return JsonResponse(inventory_shoe_deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        inventory_shoe_data = JSONParser().parse(request)
        inventory_shoe_deserializer = Inventory_shoeSerializer(inventory_shoe, data=inventory_shoe_data, partial=True)
        if inventory_shoe_deserializer.is_valid():
            inventory_shoe_deserializer.save()
            return JsonResponse(inventory_shoe_deserializer.data)
        return JsonResponse(inventory_shoe_deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        inventory_shoe.delete()
        return JsonResponse({'message': 'data pk id deleted sucessfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def inventory_shoe_list_available(request):
    inventory_shoe = Inventory_shoe.objects.filter(available=True)

    if request.method == 'GET':
        inventory_shoes_serializer = Inventory_shoeSerializer(inventory_shoe, many=True)
        return JsonResponse(inventory_shoes_serializer.data, safe=False)

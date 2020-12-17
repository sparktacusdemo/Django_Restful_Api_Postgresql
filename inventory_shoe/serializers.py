from rest_framework import serializers
from inventory_shoe.models import Inventory_shoe


class Inventory_shoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory_shoe
        fields = ('id',
                  'name',
                  'description',
                  'available')

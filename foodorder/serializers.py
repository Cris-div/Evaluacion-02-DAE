from rest_framework import serializers
from .models import Pedido , Plato

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'fecha', 'total', 'estado', 'platos']
        read_only_fields = ['created_at', 'updated_at']


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = ['id', 'nombre', 'precio', 'categoria']
        read_only_fields = ['created_at', 'updated_at']
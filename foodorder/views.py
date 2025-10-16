from django.shortcuts import render
from rest_framework import viewsets , filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Plato, Pedido
from .serializers import PlatoSerializer, PedidoSerializer
# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'message': '🍔 Welcome to FoodOrder API',
        'version': 'v1.0',
        'description': 'Sistema de gestión de platos y pedidos para restaurante',
        'endpoints': {
            'platos': reverse('plato-list', request=request, format=format),
            'pedidos': reverse('pedido-list', request=request, format=format),
        }
    })


class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['estado', 'total']
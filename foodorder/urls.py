from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import api_root, PlatoViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r'platos', PlatoViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]

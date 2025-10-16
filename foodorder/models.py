from django.db import models

# Create your models here.

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    Estados=[('pendiente','Pendiente'),
            ('en_proceso','En Proceso'),
            ('entregado','Entregado'),
            ('cancelado','Cancelado')]
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=20 ,choices=Estados , default='pendiente')

    platos= models.ManyToManyField(Plato, related_name='pedidos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.estado
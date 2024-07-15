from django.contrib.auth.models import User
from django.db import models

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default='C',
        max_length=1,
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )
    
    def __str__(self):
        return f'Pedido Nº {self.pk}'


class RequestItem(models.Model):
    class Meta:
        verbose_name = 'RequestItem'   # O que mostrar quando houver uma categoria
        verbose_name_plural = 'RequestItens'  # O que mostrar quando estiver no plural
        
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=255)
    variation_id = models.PositiveIntegerField()
    price = models.FloatField()
    promocional_price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField()
    image = models.CharField(max_length=2000)
    
    def __str__(self):
        return f'Item do {self.request}'
    
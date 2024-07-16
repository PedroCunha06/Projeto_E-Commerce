from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

import re

from utils.validation_cpf import validation_cpf

class ProfileUser(models.Model):
    class Meta:
        verbose_name = 'ProfileUser'   # O que mostrar quando houver uma categoria
        verbose_name_plural = 'ProfileUsers'  # O que mostrar quando estiver no plural
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    birth_date = models.DateField()
    cpf = models.CharField(max_length=11, help_text='Just numbers.')
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=5)
    complement = models.CharField(max_length=30, blank=True)
    neightborhood = models.CharField(max_length=30)
    cep = models.CharField(max_length=8, help_text='Just numbers.')
    city = models.CharField(max_length=30)
    state = models.CharField(
        max_length=2,
        default='SP',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins')
        )
    )
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def clean(self):
        error_message = {}
        
        if not validation_cpf(self.cpf):
            error_message['cpf'] = 'Enter a valid CPF'
            
        if re.search(r'[^0-9]', self.cep) or len(self.cep) != 8:
            error_message['cep'] = 'Enter a valid CEP'
            
        if error_message:
            raise ValidationError(error_message)
            
    
    
    

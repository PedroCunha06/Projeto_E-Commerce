from django.contrib import admin
from product.models import Product

@admin.register(Product)    # Usa o decorator para registrar o model
class ProductAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'marketing_price'    # Mostrar name no display
    ordering = '-id', # Ordernar por Id decrescente
    search_fields = 'name', 'id',  # Campo de pesquisa
    list_per_page = 10  # Itens por página
    list_max_show_all = 100 # Itens máximo a se mostrar na tela
    list_editable = 'marketing_price',   # Permite ter tópicos editáveis
    list_display_links = 'name',   # O que está como editable, não pode estar aqui

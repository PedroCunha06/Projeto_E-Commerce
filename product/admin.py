from django.contrib import admin
from product.models import Product, Variation

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        VariationInline
    ]
    list_display = 'id', 'name', 'formatted_marketing_price', 'formatted_promotional_price',    # Mostrar name no display
    ordering = '-id', # Ordernar por Id decrescente
    search_fields = 'name', 'id',  # Campo de pesquisa
    list_per_page = 10  # Itens por página
    list_max_show_all = 100 # Itens máximo a se mostrar na tela
    list_display_links = 'name',   # O que está como editable, não pode estar aqui
    
admin.site.register(Product, ProductAdmin)  # Registra o model no admin

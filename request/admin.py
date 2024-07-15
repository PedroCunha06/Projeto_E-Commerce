from django.contrib import admin
from request.models import Request, RequestItem

class RequestItemInline(admin.TabularInline):
    model = RequestItem
    extra = 1


class RequestAdmin(admin.ModelAdmin):
    inlines = [
        RequestItemInline
    ]
    list_display = 'id', 'user', 'status'  # Mostrar name no display
    ordering = '-id', # Ordernar por Id decrescente
    search_fields = 'name', 'id',  # Campo de pesquisa
    list_per_page = 10  # Itens por página
    list_max_show_all = 100 # Itens máximo a se mostrar na tela
    list_editable = 'status',   # Permite ter tópicos editáveis
    list_display_links = 'user',   # O que está como editable, não pode estar aqui
    
admin.site.register(Request, RequestAdmin)  # Registra o model no admin

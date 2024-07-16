from django.contrib import admin
from user_profile.models import ProfileUser

@admin.register(ProfileUser)
class ProfileUserAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', # Mostrar name no display
    ordering = '-id', # Ordernar por Id decrescente
    search_fields = 'name', 'id',  # Campo de pesquisa
    list_per_page = 10  # Itens por página
    list_max_show_all = 100 # Itens máximo a se mostrar na tela
    list_display_links = 'user',   # O que está como editable, não pode estar aqui

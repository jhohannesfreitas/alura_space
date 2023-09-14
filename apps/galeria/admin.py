"""
PAINEL ADMIN

Informe tudo que deseja mostrar no painel admin
-http://127.0.0.1:8000/admin
-criar o super usuário: python manage.py createsuperuser

"""


from django.contrib import admin
from apps.galeria.models import Fotografia


class ListandoFotografia(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria","usuario",)
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografia)

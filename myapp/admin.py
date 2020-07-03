from django.contrib import admin
from .models import ComprarArticulo, Nota
# Register your models here.


class AdminComprarArticulo(admin.ModelAdmin):
    list_display = ["__unicode__", "categoria", "descripcion"]

    class Meta:
        model = ComprarArticulo


class AdminNota(admin.ModelAdmin):
    list_display = ["__unicode__", "name", "desc"]
    class Meta:
        model = Nota


admin.site.register(ComprarArticulo, AdminComprarArticulo)

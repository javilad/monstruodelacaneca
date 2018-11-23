from django.contrib import admin
from monstruo.models import  *
from django.utils.html import format_html

# Register your models here.


# class ResiduoInline(admin.StackedInline):
#     model = Residuo
#     extra = 3

# class CanecaAdmin(admin.ModelAdmin):
#     inlines = [ResiduoInline]
#     list_display = ('nombre','tipoUso', 'imagen')
#     list_filter = ['tipoUso']


class PartidaInline(admin.TabularInline):
    model = Partida
    extra = 1


class RecicladorAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{self.imagen}" />'.format(obj.imagen.url))

    image_tag.short_description = 'imagen'
    inlines = [PartidaInline]
    list_display = ('alias','tipoReciclador', 'nivelActual','puntos','imagen')
    list_filter = ['tipoReciclador']


admin.site.register(TipoReciclador)
admin.site.register(TipoUso)

admin.site.register(Reciclador,RecicladorAdmin )
admin.site.register(Partida)

#admin.site.register(Caneca, CanecaAdmin)
admin.site.register(Caneca)
admin.site.register(Residuo)
admin.site.register(Nivel)

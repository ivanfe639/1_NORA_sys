from django.contrib import admin
from noraSys.models import SuperUsuario, Menu, Pedido

# Register your models here.
class SuperUsuarioAdmin(admin.ModelAdmin):
    list_display=('USER','PASSWORD')

class MenuAdmin(admin.ModelAdmin):
    list_display=('DATE','OPTION1','OPTION2','OPTION3','OPTION4')

class PedidoAdmind(admin.ModelAdmin):
    list_display=('DATE','NAME','OPTION','COMMENTS')

admin.site.register(SuperUsuario,SuperUsuarioAdmin)   
admin.site.register(Menu,MenuAdmin)   
admin.site.register(Pedido)


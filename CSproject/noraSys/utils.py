from noraSys.models import SuperUsuario, Menu, Pedido

LIMIT_HOUR = 20

#_______________________________________________________________________________________________________
# Función para verificar las credenciales de super usuario, revisa en la base de datos si existen    ///
#                                                                                                   ///
# check_SU(userIn,passIn):                                                                         ///
# userIN: <str> usuario                                                                           ///
# passIn: <str> contraseña                                                                       ///
#_______________________________________________________________________________________________///
def check_SU(userIn,passIn):

    # Bandera para saber si el proceso se autorizó o no
    auth_flag = 0

    query_SU = SuperUsuario.objects.values_list('USER','PASSWORD')
    
    # subindice[0] usuarios, subindce[1] contraseñas
    for SU in query_SU:
        if (SU[0] == userIn):
            if (SU[1] == passIn):
                auth_flag = 1
                break;
    
    
    return auth_flag

#______________________________________________________________________________________________________
# Función para escribir en la base de datos el menú de un día en especifico, si existe un menú con  ///
# esa fecha lo modifica                                                                            ///
#                                                                                                 ///
# writeMenu(dicc_menu):                                                                          ///
# dicc_menu ={'fecha' : <DateTime>,                                                             ///
#             'opcion1' : <str>,                                                               ///
#             'opcion2' : <str>,                                                              ///
#             'opcion3' : <str>,                                                             ///
#             'opcion4' : <str>,}                                                           ///
#__________________________________________________________________________________________///
def writeMenu(dicc_menu):
    # Revisa si el registro existe para esa fecha
    try:
        query_menu = Menu.objects.get(DATE=dicc_menu['fecha'])
        exist_flag = 1
    except:
        exist_flag = 0
    
    if (exist_flag == 0):
        print('NO existe')
        menu_temp = Menu(DATE=dicc_menu['fecha'], OPTION1=dicc_menu['opcion1'], OPTION2=dicc_menu['opcion2'], OPTION3=dicc_menu['opcion3'], OPTION4=dicc_menu['opcion4'])
        menu_temp.save()
    else:
        query_menu.delete()
        menu_temp = Menu(DATE=dicc_menu['fecha'], OPTION1=dicc_menu['opcion1'], OPTION2=dicc_menu['opcion2'], OPTION3=dicc_menu['opcion3'], OPTION4=dicc_menu['opcion4'])
        menu_temp.save()
        print('SI existe')


#____________________________________________________________________________________________________
# Función para retornar los query de la base de datos de Pedidos y Menu para visualizarlos        ///
#                                                                                                ///
# vizPedidos(fecha):                                                                            ///
# fecha: <DateTime>                                                                            ///
#_____________________________________________________________________________________________///
def vizPedidos(fecha):
    
    query_menu = Menu.objects.all().filter(DATE=fecha).values_list('OPTION1','OPTION2','OPTION3','OPTION4')

    query_pedido = Pedido.objects.all().filter(DATE=fecha).values_list('DATE','NAME','OPTION','COMMENTS')
                        
            
    dicc_vizPedidos = {'query_pedido' : query_pedido,
                    'query_menu' : query_menu}
    return dicc_vizPedidos


#____________________________________________________________________________________________________
# Función para retornar el query de la base de datos Menu para visualizar a los clientes          ///
#                                                                                                ///
# consultMenu(fecha):                                                                            ///
# fecha: <DateTime>                                                                            ///
#_____________________________________________________________________________________________///
def consultMenu(fecha):
    
    query_Menu = Menu.objects.all().filter(DATE=fecha).values_list('DATE','OPTION1','OPTION2','OPTION3','OPTION4')
    return query_Menu


#______________________________________________________________________________________________________
# Función para escribir en la base de datos el pedido que realiza un cliente en un día en           ///
# especifico                                                                                       ///
#                                                                                                 ///
# writePedido(dicc_pedido):                                                                      ///
# dicc_pedido = {'nombre' : request.POST['nombre'],                                             ///
#                'opcionSelect': <int>,                                                        ///
#                'comentarios' : <str>,                                                       ///
#                'fechaHoy' : <DateTime>}                                                    ///
#___________________________________________________________________________________________///
def writePedido(dicc_pedido):

    # Guardar el pedido en la base de datos
    query_temp = Pedido(DATE=dicc_pedido['fechaHoy'], NAME=dicc_pedido['nombre'], OPTION=dicc_pedido['opcionSelect'], COMMENTS=dicc_pedido['comentarios'])
    query_temp.save()

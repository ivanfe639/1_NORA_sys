from django.shortcuts import render

from noraSys.utils import check_SU, writeMenu, vizPedidos, consultMenu, writePedido
from noraSys.utils import LIMIT_HOUR
from noraSys.forms import noraForm, authForm, noraVerPedidos, clientsForm

from datetime import date
import time





#http://localhost:8000/noraSysSuperUser/
def indexNora(request):

    autorizado = ''

    if request.method == 'POST':
                       
        
        # Vista para la autenticación de NORA
        if ('authNora' in request.POST):
            print('|| authNora ||')
            
            userIn = request.POST['usuario']
            passIn = request.POST['contrasena']
            # print('userIn %s' % (userIn))
            # print('passIn %s' % (passIn))

            # Comprueba las credenciales 
            auth_flag = check_SU(userIn,passIn)

            if (auth_flag == 0):
                print('Usuario no autorizado ')
                autorizado = 'Usuario no autorizado'
            else:
                print('usuario autorizado')
                return render(request, '3selectorNoraView.html') 


        # Renderiza la vista de creacion de menus
        elif ('crearMenus' in request.POST):
            print('||crearMenus||')
            noraFormulario = noraForm()
            dicc_context = {'form' : noraFormulario}
            return render(request, '2noraMenuView.html',dicc_context) 
        

        # Renderiza la vista de revision de pedidos
        elif ('verPedidos' in request.POST):
            print('||verPedidos||')
            formPedidos = noraVerPedidos()
            dicc_pedidos ={'form' : formPedidos}
            return render(request, '4noraVerPedidosView.html',dicc_pedidos) 


        elif ('visualizarPedidos' in request.POST):
            print('||visualizarPedidos||')

            fecha = request.POST['fechaPedidos']

            # Consulta los pedidos realizados y el menu de esa fecha y retorna las consultas a renderizar
            dicc_context = vizPedidos(fecha)

            return render(request, '5vizPedidosView.html',dicc_context) 

        elif ('sendSlack' in request.POST):
            print('||sendSlack||')

            ######################################
            # @celeryTask to send Slack reminder 
            ######################################


        # Renderiza la vista de creacionde menus
        elif ('saveMenus' in request.POST):
            print('||saveMenus||')

            # diccionario donde se almacena los valores insgresados en el formulario
            dicc_menu ={'fecha' : request.POST['fecha'],
                        'opcion1' : request.POST['opcion1'],
                        'opcion2' : request.POST['opcion2'],
                        'opcion3' : request.POST['opcion3'],
                        'opcion4' : request.POST['opcion4'],
            }
            
            # Escribe modifica el menu segun lna fecha ingresada
            writeMenu(dicc_menu)

            #Renderizar se ha guardado el registro

    norafomu = authForm()
    dicc_context = {'form' : norafomu,
                    'autorizacion' : autorizado,}
    return render(request, '1noraAuthView.html',dicc_context) 
    #return render(request, '2noraMenuView.html',dicc_context) 


#http://localhost:8000/noraSysClientes/
def indexClients(request):
    print('--__indexClients__--')
    
    fecha_hoy = date.today()    # para el menu
    hora_actual = int(time.strftime("%H")) # para saber si aún puede realizar un pedido


    if (hora_actual < LIMIT_HOUR):       
        print('fecha_hoy= ',fecha_hoy)
        print('hora_actual= ',hora_actual)

        if request.method == 'POST':
            print('main')
            
            dicc_pedido = {'nombre' : request.POST['nombre'],
                           'opcionSelect': request.POST['opciones'],
                           'comentarios' : request.POST['comentarios'],
                           'fechaHoy' : fecha_hoy}

            print('nombre = ', dicc_pedido['nombre'])
            print('opcionSelect = ', dicc_pedido['opcionSelect'])
            print('comentarios = ', dicc_pedido['comentarios'])
            

            # Almacena el pedido en la base de datos
            writePedido(dicc_pedido)
            

            return render(request, '8gracias.html',dicc_pedido) 

        else:
            clientFormu = clientsForm()
        
        menuHoy = consultMenu(fecha_hoy)
                
        dicc_context = {'form' : clientFormu,
                        'menuHoy' : menuHoy }
        return render(request, '6seleccionClientesView.html',dicc_context) 

    else:

        return render(request, '7noHacerPedidos.html',{'horaMax' : LIMIT_HOUR}) 
    
    



from django.db.models import query
import pytest
from noraSys.utils import *
from datetime import date

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4


@pytest.mark.django_db
def test_usuarioValido_check_SU():
    
    # Guarda un registro en la DB de pruebas
    query_temp = SuperUsuario(USER='su',PASSWORD='su')
    query_temp.save()

    userIn = 'su'
    passIn = 'su'

    assert check_SU(userIn,passIn) == 1

@pytest.mark.django_db
def test_usuarioInvalido_check_SU():
    
    # Guarda un registro en la DB de pruebas
    query_temp = SuperUsuario(USER='su',PASSWORD='su')
    query_temp.save()

    userIn = 'invalido'
    passIn = 'invalido'

    assert check_SU(userIn,passIn) == 0


@pytest.mark.django_db
def test_writeMenu():

    # genera un menú temporal       
    fechaHoy = date.today()
    dicc_menu ={'fecha' : fechaHoy,
             'opcion1' : 'Opcion 1',
             'opcion2' : 'Opcion 2',
             'opcion3' : 'Opcion 3',
             'opcion4' : 'Opcion 4'}

    # Escribe el menú temporal
    writeMenu(dicc_menu)

    # Lee el menú escrito en la base de datos
    query_Menu = Menu.objects.all().filter(DATE=fechaHoy).values_list('DATE','OPTION1','OPTION2','OPTION3','OPTION4')

    # banderas de verificación de cada lectura
    boolOp0 = boolOp1 = boolOp2 = boolOp3 = boolOp4 = False

    # Comprueba que cada registro se haya escrito correctamente 
    if (query_Menu[0][0] == dicc_menu['fecha']):
        boolOp0 = True
        
    if (query_Menu[0][1] == dicc_menu['opcion1']):
        boolOp1 = True

    if (query_Menu[0][2] == dicc_menu['opcion2']):
        boolOp2 = True

    if (query_Menu[0][3] == dicc_menu['opcion3']):
        boolOp3 = True
        
    if (query_Menu[0][4] == dicc_menu['opcion4']):
        boolOp4 = True

    # Verifica si todos los registros fueron leidos correctamente
    assert (boolOp0 and boolOp1 and boolOp2 and boolOp3 and boolOp4) == True

@pytest.mark.django_db
def test_writePedido():

    # Crea el set de datos de prueba
    fechaHoy = date.today()
    dicc_pedido = {'nombre' : 'John Doe',
                'opcionSelect': 1,
                'comentarios' : 'Comentarios comentarios',
                'fechaHoy' : fechaHoy}

    # Usa la función par escribir el pedido
    writePedido(dicc_pedido)

    query_pedido = Pedido.objects.all().filter(DATE=fechaHoy).values_list('DATE','NAME','OPTION','COMMENTS')

    # banderas de verificación de cada lectura
    boolOp0 = boolOp1 = boolOp2 = boolOp3 = False

    # Comprueba que cada registro se haya escrito correctamente 
    if (query_pedido[0][0] == dicc_pedido['fechaHoy']):
        boolOp0 = True

    if (query_pedido[0][1] == dicc_pedido['nombre']):
        boolOp1 = True

    if (query_pedido[0][2] == dicc_pedido['opcionSelect']):
        boolOp2 = True

    if (query_pedido[0][3] == dicc_pedido['comentarios']):
        boolOp3 = True

    # Comprueba que cada registro se haya leido de manera correcta
    assert (boolOp0 and boolOp1 and boolOp2 and boolOp3 ) == True


@pytest.mark.django_db
def test_vizPedidos_queryPedido():
    
    ########################################################################
    # Crea el set de datos de prueba
    fechaHoy = date.today()
    dicc_pedido = {'nombre' : 'John Doe',
                'opcionSelect': 1,
                'comentarios' : 'Comentarios comentarios',
                'fechaHoy' : fechaHoy}

    # Usa la función par escribir el pedido
    writePedido(dicc_pedido)

    # genera un menú temporal       
    dicc_menu ={'fecha' : fechaHoy,
             'opcion1' : 'Opcion 1',
             'opcion2' : 'Opcion 2',
             'opcion3' : 'Opcion 3',
             'opcion4' : 'Opcion 4'}

    # Escribe el menú temporal
    writeMenu(dicc_menu)

    ########################################################################
    diccionario = vizPedidos(fechaHoy)

    query_pedido = diccionario['query_pedido']

     # banderas de verificación de cada lectura
    boolOp0 = boolOp1 = boolOp2 = boolOp3 = False

    # Comprueba que cada registro se haya escrito correctamente 
    if (query_pedido[0][0] == dicc_pedido['fechaHoy']):
        boolOp0 = True

    if (query_pedido[0][1] == dicc_pedido['nombre']):
        boolOp1 = True

    if (query_pedido[0][2] == dicc_pedido['opcionSelect']):
        boolOp2 = True

    if (query_pedido[0][3] == dicc_pedido['comentarios']):
        boolOp3 = True

    assert (boolOp0 and boolOp1 and boolOp2 and boolOp3 ) == True


@pytest.mark.django_db
def test_vizPedidos_queryMenu():
    
    ########################################################################
    # Crea el set de datos de prueba
    fechaHoy = date.today()
    dicc_pedido = {'nombre' : 'John Doe',
                'opcionSelect': 1,
                'comentarios' : 'Comentarios comentarios',
                'fechaHoy' : fechaHoy}

    # Usa la función par escribir el pedido
    writePedido(dicc_pedido)

    # genera un menú temporal       
    dicc_menu ={'fecha' : fechaHoy,
             'opcion1' : 'Opcion 1',
             'opcion2' : 'Opcion 2',
             'opcion3' : 'Opcion 3',
             'opcion4' : 'Opcion 4'}

    # Escribe el menú temporal
    writeMenu(dicc_menu)

    ########################################################################
    diccionario = vizPedidos(fechaHoy)

    query_Menu = diccionario['query_menu']

    # banderas de verificación de cada lectura
    boolOp1 = boolOp2 = boolOp3 = boolOp4 = False

    # Comprueba que cada registro se haya escrito correctamente 
           
    if (query_Menu[0][0] == dicc_menu['opcion1']):
        boolOp1 = True

    if (query_Menu[0][1] == dicc_menu['opcion2']):
        boolOp2 = True

    if (query_Menu[0][2] == dicc_menu['opcion3']):
        boolOp3 = True
        
    if (query_Menu[0][3] == dicc_menu['opcion4']):
        boolOp4 = True

    # Verifica si todos los registros fueron leidos correctamente
    assert (boolOp1 and boolOp2 and boolOp3 and boolOp4) == True

@pytest.mark.django_db
def test_consulMenu():

    # genera un menú temporal       
    fechaHoy = date.today()
    dicc_menu ={'fecha' : fechaHoy,
             'opcion1' : 'Opcion 1',
             'opcion2' : 'Opcion 2',
             'opcion3' : 'Opcion 3',
             'opcion4' : 'Opcion 4'}

    # Escribe el menú temporal
    writeMenu(dicc_menu)

    query_Menu = consultMenu(fechaHoy)


    # banderas de verificación de cada lectura
    boolOp0 = boolOp1 = boolOp2 = boolOp3 = boolOp4 = False

    # Comprueba que cada registro se haya escrito correctamente 

    if (query_Menu[0][0] == dicc_menu['fecha']):
        boolOp0 = True 

    if (query_Menu[0][1] == dicc_menu['opcion1']):
        boolOp1 = True

    if (query_Menu[0][2] == dicc_menu['opcion2']):
        boolOp2 = True

    if (query_Menu[0][3] == dicc_menu['opcion3']):
        boolOp3 = True
        
    if (query_Menu[0][4] == dicc_menu['opcion4']):
        boolOp4 = True

    assert boolOp0 and boolOp1 and boolOp2 and boolOp3 and boolOp4 == True







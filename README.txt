
Hola! como están!!

Antes de todo quisiera dar una explicación corta del por qué no pude implementar las tareas asíncronas de Celery. Por cuestiones de versiones de cada una de las librerías y de restricciones de permisos del PC (la prueba la realicé en un PC prestado ya que el mío justo murió :/) el servidor de Celery no se podía iniciar, así que opte por realizar el reto desde cero y dejando la opción lista para cuando la configuración de Celery esté correcta. Una vez dicho esto pasemos al reto.

El reto consistía en realizar una app donde un usuario con permisos pudiera crear el menú alimenticio de determinados días para que en otra vista los clientes pudieran realizar pedidos sobre ese menú y así facilitar la gestión de los almuerzos. La app la enfoque en dos vistas principales, la primera fue la vista del super usuario que por medio de una autenticación de credenciales pudiera entrar al menú de gestión donde se pueda realizar la creación de menús, ver los pedidos realizados y enviar un recordatorio a los clientes. Esta autenticación se realizó consultando a una base de datos donde se encuentran las credenciales de las únicas personas que pueden acceder y así evitar que cualquier persona pueda entrar al menú de gestión.

La segunda vista que implementé fue la de clientes, la cual muestra el menú del día en curso si aún es posible hacer pedidos, en este caso antes de las 11:00 am (La hora máxima configurada es 20 para cuestiones de pruebas, esta constante se encuentra cómo LIMIT_HOUR en el archivo utils.py).

DATOS UTILES

Las URLs son las siguientes:
http://localhost:8000/noraSysSuperUser/
http://localhost:8000/noraSysClientes/

Las credenciales de super usuario son:
Usuario: nora
Contraseña: nora

Tambien se recomienda crear un entorno virtual e instalar los paquetes que se encuentran en el archivo requirements.txt así:
pip install -r requirements.txt


Por cuestiones de pruebas, el día 23 de agosto hay datos almacenados de pedidos y menú, tener en cuenta que el menú para los clientes se toma el día actual cuando se haga la consulta.

Para el testeo de las funciones que cree usé Pytest, y para ejecutar las pruebas solo hay que ejecutar “pytest” en el directorio principal del proyecto

Básicamente eso es todo, solo queda darles las gracias por la oportunidad brindada y me la pasé muy bien programando esta mni App, fue chevre hacerla :D.

Saludos.


Ivan Felipe Obregon Carreño
ivan.fe639@gmail.como
+57 314 247 2279
MS. en Ingeniería Electrónica
Ing. Electrónico





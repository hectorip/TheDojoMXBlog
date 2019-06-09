### Arquitectura cliente-servidor.

Esta característica normalmente es algo que ya hacemos normalmente con nuestros servicios web en general.

Una API REST debe ser ejecutada como un **servidor**, que sea encargado de contestar las peticiones de un **cliente**. El cliente es el programa que usa los servicios que la API provee, pide datos u operaciones y estas son ejecutadas. Fielding pensaba en el cliente como en la interfaz de usuario, pero en nuestros días un cliente podría ser fácilmente otro servidor.

Esta arquitectura nos permite separar claramente las responsabilidades de cada programa y esto a su vez *permite que tanto el cliente como el servidor puedan cambiar y evolucionar por su cuenta*, sin depender mutuamente uno del otro.

La arquitectura cliente servidor también define otras cosas, por ejemplo que el servidor nunca inicia la comunicación y sólo responde a peticiones que el cliente le haya hecho, pero no es esencial cumplir con estas para hablar de una API REST, lo más importante es la **separación de responsabilidades** entre cliente y servidor.


### Comunicación sin estado

El estado se refiere a toda la información que contiene un sistema programa en un punto del tiempo. Un sistema REST no mantiene esta información _en la comunicación entre cliente y servidor_. 

Esto quiere decir que no se mantiene una conexión que mantenga un sesión en el servidor que contenga los datos del cliente actual. Cada vez que el cliente haga una petición deberá envíar todos los datos necesarios para que el servidor genere y obtenga la información que se está pidiendo.

Esto tiene ventajas y desventajas. Primero, desacopla completamente el cliente y la implementación del servidor, ya que un cliente se podría comunicar con _cualquier instancia_ del servidor actual. Esto a su vez permite crear servicios replicados y balanceados que son capaces de soportar mucho mejor cargas grandes de trabajo generadas por muchos clientes, ya que no se casa un cliente con un servidor.

Una de las desventajas de este tipo de comunicación es que el estado se tiene que recrear en cada llamada, por lo que la transferencia de información repetida y el procesamiento de esta genera una carga extra que se podría evitar en una conexión que mantenga el estado.

Conocer estos detalles nos permitirá decidir si REST es lo adecuado para nuestro proyecto.

### Interfaz uniforme

Esta es la característica más distintiva de un sistema REST. Quier

### Sistema en capas

Las funciones del servidor y la comunicación con el cliente podrían (normalmente, _deberían_) estar separadas en capas con diferentes funciones cada una. Por ejemplo, el servicio podría estar compuesto por:

* Una red de entrega de contenido (CDN)
* Un balanceador de carga
* Un firewall
* Un servidor de autenticación
* El servidor de web
* El servidor de aplicaciones

Esta separación en capas hace que el servicio web sea más confiable y tenga mejor comportamiento en general. Lo importante de 

### Interfaz uniforme



### No mantiene el estado

### Cacheable

### Código bajo demanda [opcional]

## Implementación de las restricciones de REST

## Documentación

## Conclusión
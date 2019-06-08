---
title: "Diseño de una API RESTful"
date: 2019-05-17
author: Héctor Patricio
tags: api rest restful arquitectura
comments: true
excerpt: "Diseñemos una API REST, pero aprendamos en el camino qué es."
header:
  overlay_image: #image
---

En el [artículo anterior de la serie](/2019/05/06/diseno-y-desarrollo-de-una-api-desde-cero.html) hablamos un poco de lo que es una API RESTful. En este artículo la definiremos a cabalidad, con ejemplos y veremos las ventajas y desventajas desde el punto de vista de desarrollo y arquitectura.

Antes de empezar con lo nuestro, hablemos que lo que NO es una API RESTful.

## Esto no es RESTful

Actualmente, muchos desarrolladores (yo me contaba entre ellos), llaman API REST a cualquier servicio Web que corra sobre HTTP, sirva recursos (objetos o elementos que representan un objeto) o cosas parecidas y use JSON como medio de comunicación.
De estas cosas, sólo la parte de servir recursos (en realidad _representaciones_ de recursos) tiene que ver con una API RESTful. El estilo arquitectural RESTful no forza el uso de HTTP y mucho menos de JSON.

Dada esta tendencia de llamar API REST a cualquier cosa que funcione sobre HTTP, debemos estar de acuerdo en que la mayoría de las API's ni siquiera _intenta_ ser REST.
Algunas son RPC (Remote Procedure Call) sobre HTTP simplemente. Otro mal uso que he escuchado es que cualquier cosa que sirva JSON es llamada API REST, pero como ya dijimos el estilo arquitectural REST ni siquiera fuerza el uso de JSON (y no todas las API's que sirven XML son SOAP).

## Arquitectura RESTful

Una API REST está definida por seis características o restricciones que vamos a explicar a continuación. Las vamos a cambiar un poco del orden tradicional para que tenga más sentido la forma en que las explicamos.

### Arquitectura cliente-servidor.

Esta característica normalmente no está en primer lugar, pero para que todo tenga sentido creo que debe ser la primera. Una API REST debe ser ejecutada en un servidor, que sea encargado de contestar las peticiones de un cliente. Esta arquitectura nos permite separar claramente las responsabilidades de cada programa.

### Sistema en capas

El sistema de comunicación entre el cliente y el servidor debería estar separado en capas con diferentes funcionalidades pero que todo esto sea transparente para el usuario.

### Interfaz uniforme

### Sin estado

### Cacheable

### Código bajo demanda [opcional]

## Implementación de las restricciones de REST

## Documentación

## Conclusión

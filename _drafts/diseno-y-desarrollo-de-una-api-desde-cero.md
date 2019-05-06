---
title: "Diseño y desarrollo de una API RESTful desde cero - La importancia de diseñar tu API"
date: 2019-04-22
author: Héctor Patricio
tags:
categories: 
comments: true
excerpt: "El primer artículo de la serie. ¿Por qué es importante diseñar de antemano tu API?"
header:
  overlay_image: #image
---

En este post explicaré **los principios básicos de diseño de una API**. Esta primera parte es bastante teórica, empezaremos con la práctica (no con la programación, sino con el diseño) en la parte final de este post.

Primero hablemos de la importancia del diseño o la arquitectura de la API. En la serie de posts hablaremos de API's para consumo web, a través de HTTP, ya que son las de mayor uso actualmente.

Pero primero hablemos de la importancia del diseño de la API.

## La importancia de diseñar la API

Pensar de antemano (y tal vez poner por escrito) la estructura y nombres de la API, aunque parezca una tarea a veces innecesaria, aburrida o burocrática, puede dar las siguientes ventajas:

1. **Mayor facilidad de desarrollo**. Tener una forma de nombrar los endpoints (los links con los que los sistemas externos interactúan), una estrucutra de respuesta, un estándar de errores y otras cuestiones definidas de antemano te permitirá pasar directo al diseño e implementación de las funcionalidades cuando llegue el momento. Si escoges usar una estructura de diseño común y popular puede que incluso haya herramientas que te faciliten la tarea. Nuestra API estará preparada para ser mantenible y escalable.
2. **Familiariadad**. Si sigues un patrón de diseño común, cuando otros desarrolladores usen tu API la entenderán más fácil y podrán comenzar a sacarle provecho más rápido.
3. **Menos documentación**. Aprovechando lo anterior, puede que gran parte de la estructura y prácticas comunes del patrón que escogiste ya estén explicadas, por lo que normalmente tendrás que documentar sólamente las partes que son especeificas de tu API.

El trabajo extra que pongas en diseñar tu API o por lo menos escoger un patrón de diseño común te ahorrará trabajo en el futuro, a tu equipo y a otros desarrolladores.

Dependiendo de la época y las necesidades han surgido varios estilos o patrones de diseño comunes.
Aquí hablaremos de tres de los más usados.

## SOAP (Simple Object Access Protocol)

Este es el estilo de servicios más usado en el mundo empresarial y también el más antiguo. En realidad es un protocolo que establece desde la manera de comunicación hasta el lenguaje usado para transferir datos.
Su nombre es un acrónimo que signfica *Simple Object Access Protocol (Protocolo simple de acceso a objetos)* y fue desarrollado por Microsoft inicialmente. El lenguaje que se usa para transferir datos es XML y tiene varios estándares que definen cada aspecto de la comunicación, por lo que no se queda en sólo un estilo de diseño de API's. Su objetivo original era definir como acceder y usar servicios web.
>>>>>>> Stashed changes

### Ventajas de SOAP

1. **Pensado para transacciones complejas**. SOAP está pensado para usarse con **transacciones**. Si lo que requieres es que tu API realice transacciones [ACID](https://en.wikipedia.org/wiki/ACID_(computer_science)), trabajar con SOAP te facilitará la vida.
2. **Establece cada parte de la comunicación**. Esto puede ser una ventaja o una desventaja, pero si estás con una tecnolodía que lo permite y aprovecha, trabajar con SOAP puede ser rápido y sin dolor, ya que los estándares estarán implementados en la platafoma/lenguaje (sobre todo las de Microsoft)

## API's RESTful

Una API REST aprovecha el diseño de las peticiones HTTP para hacer interfaces web intuitivas.
REST son las siglas de "Representational State Transfer" (Transferencia de Estado Representacional). Esto significa.


## Protocolos y lenguajes de comunicación

## El ejercicio

## Conclusión y próximos artículos
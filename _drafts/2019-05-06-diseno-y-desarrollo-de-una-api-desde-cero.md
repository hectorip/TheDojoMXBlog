---
title: "Diseño y desarrollo de una API RESTful desde cero - La importancia de diseñar tu API"
date: 2019-05-06
author: Héctor Patricio
tags: apis rest soap
categories: api rest soap
comments: true
excerpt: "El primer artículo de la serie. ¿Por qué es importante diseñar de antemano tu API?"
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1200/v1557201862/edho-pratama-149011-unsplash_jlppci.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1200/v1557201862/edho-pratama-149011-unsplash_jlppci.jpg
  overlay_filter: rgba(0, 0, 0, 0.5)
---

En este post explicaré **los principios básicos de diseño de una API**. Esta primera parte es bastante teórica, empezaremos con la práctica (no con la programación, sino con el diseño) en un post posterior.

Primero hablemos de la importancia del diseño o la arquitectura de la API. En la serie de posts hablaremos de API's para consumo web, a través de HTTP, ya que son las de mayor uso y popularidad.

Pero primero hablemos de la importancia del diseño de la API.

## La importancia de diseñar tu API

Pensar de antemano (y tal vez poner por escrito) la estructura y nombres de la API, aunque parezca una tarea a veces innecesaria, aburrida o burocrática, puede dar las siguientes ventajas:

1. **Mayor facilidad de desarrollo**. Tener una forma de nombrar los endpoints (los links con los que los sistemas externos interactúan), una estrucutra de respuesta, un estándar de errores y otras cuestiones definidas de antemano te permitirá pasar directo al diseño e implementación de las funcionalidades cuando llegue el momento. Si escoges usar una estructura de diseño común y popular puede que incluso haya herramientas que te faciliten la tarea. Nuestra API estará preparada para ser mantenible y escalable.
2. **Familiariadad**. Si sigues un patrón de diseño común, cuando otros desarrolladores usen tu API la entenderán más fácil y podrán comenzar a sacarle provecho más rápido.
3. **Menos documentación**. Aprovechando lo anterior, puede que gran parte de la estructura y prácticas comunes del patrón que escogiste ya estén explicadas, por lo que normalmente tendrás que documentar sólamente las partes que son especeificas de tu API.

El trabajo extra que pongas en diseñar tu API o por lo menos escoger un patrón de diseño común te ahorrará trabajo en el futuro, a tu equipo y a otros desarrolladores.

Dependiendo de la época y las necesidades han surgido varios estilos o patrones de diseño comunes. Aquí hablaremos de dos de los más usados a lo largo del tiempo y de los más populares.

## SOAP (Simple Object Access Protocol)

Este es el estilo de servicios más usado en el mundo empresarial y también el más antiguo de los que hablaremo aquí. En realidad es un protocolo que establece desde la manera de comunicación hasta el lenguaje usado para transferir datos.
Su nombre es un acrónimo que signfica *Simple Object Access Protocol (Protocolo simple de acceso a objetos)* y fue desarrollado por Microsoft inicialmente. El lenguaje que se usa para transferir datos es XML y tiene varios estándares que definen cada aspecto de la comunicación, por lo que no se queda en sólo un estilo de diseño de API's. Su objetivo original era definir como acceder y usar servicios web.

### Ventajas de SOAP

1. **Pensado para transacciones complejas**. SOAP está pensado para usarse con **transacciones**. Si lo que requieres es que tu API realice transacciones [ACID](https://en.wikipedia.org/wiki/ACID_(computer_science)), trabajar con SOAP te facilitará la vida.
2. **Establece cada parte de la comunicación**. Esto puede ser una ventaja o una desventaja, pero si estás con una tecnología que lo permite y aprovecha, trabajar con SOAP puede ser rápido y sin dolor, ya que los estándares estarán implementados en la platafoma/lenguaje (sobre todo las de Microsoft).
3. **Se lleva bien con las tecnologías de Microsoft**. Si trabajas en los lenguajes y con los editores de MS, nunca en tu vida vas a tener que tocar siquiera el XML crudo con el que se transmiten los datos. Sus herramientas y lenguajes tienen todo lo necesario para hacerte fácil trabajar con SOAP.

### Desventajas de SOAP.

1. **Sólo se lleva bien con las tecnologíos de MS**. Casi en ningún otro lenguaje y editores hay soporte tan completo para SOAP como lo hay para las tecnologías de MS. Si por alguna razón tienes que trabajar con SOAP en otra tecnología, va a parecer un martirio, y aún así a veces se tiene que hacer. Hayu mejores herramientas para trabajar con otros tipos de API's en los lenguajes más comunes usados en OpenSource.
2. **XML**. Parsear y procesar XML es en geneal más difícil y requiere más pasos que hacer con otros lenguajes de transmisión de datos usados con otros estilos de API's.
3. **Velocidad**. Al ser un protocolo más complejo, aumenta la cantidad de procesamiento y transferencia de datos requerido para funcionar, lo que lo hace más lento que otras alternativas. Además, no es fácilmente cacheable, por lo que cada respuesta tiene que ser única.

### Conclusión acerca de SOAP

Hay personas que se escandalizan cuando tienen que trabajar en un API's SOAP, y esto de verdad es un problema cuando tus herramientas no hacen fácil trabajar con este tipo de API's. Sin embargo, sus características las hacen adecuadas para API's transaccionales enfocadas en el mercado empresarial, por lo que es conveniente escorger este tipo de API's en los casos adecuados. **Cada herramienta fue creada con un propósito y tiene sus usos adecuados.**

## API's RESTful

Una API REST aprovecha el diseño de las peticiones HTTP para hacer interfaces web intuitivas.
REST son las siglas de "Representational State Transfer" (Transferencia de Estado Representacional), que es un estilo de arquitectura de sistemas distribuidos (podemos pensar en la web como un sistema distribuido). 
Este estilo establece 6 características que se deben de cumplir para que un sistema sea considerado RESTful:

1. Arquitectura cliente-servidor. Existe un programa encargado de hacer peticiones (cliente) y uno encargado de responderlas (servidor).
2. Interfaz uniforme. Todos los clientes deberían acceder a la misma interfaz. Si el servidor cumple con la interfaz, puede haber un número ilimitado de clientes independientes que cambian sin dependencias entre ellos o con la implementación del servidor. *Esta es una de las razones principales por las que las API's REST son tan usadas actualmente.* Este punto lo trataremos más a profundidad en el siguiente artículo.
3. Sistema sin estado. Las conexiones entre los sistemas (cliente y servidor) no deberían dependender de un estado creado o mantenido a través de peticiones anteiores. Todo lo necesario para generar una respuesta se encuentra en la petición actual.
4. Cacheable. Las respuestas pueden ser guardadas para ser contestadas más rápidamente por el mismo servidor o por un sistema intermedio.
5. Sistema en capas. El sistema puede estar construido por varias capas de servicio y esto ser transparente para los clientes (no tienen que modificar sus llamadas).
6. Código bajo demanda. El servidor debe ser capaz de envíar código a cliente para que sea ejecutado.

Todos los puntos anteriores nos permiten crear una API que se comporta de manera efectuva para las necesidades actuales, además aprovecha las caractarísticas nativas de los sistemas web, por lo que crear una API RESTful es más sencillo que trabajar con SOAP, por que no implica protocolos extra.

### Ventas de REST

1. **Implementación más fácil**. Comparado con SOAP, implementar una API RESTful es más sencillo casi en cualquier lenguaje, no requiere protocolos extra. Además en la mayoría de los lenguajes ya hay clientes o es muy sencillo programar uno.
2. **Flexibilidad**. REST no define el lenguaje de transferencia de datos, el tipo de autenticación y otros detalles de la comunicación que se dejan a discreción de los implementadores. En la actualidad, la mayoría de las API's REST usan JSON como lenguaje de transeferencia, pero bien podrían usar XML o MessagePack, incluso un lenguaje propietario.
3. **Popularidad**. La extensión de uso de API's RESTful ha hecho que proliferen herramientas para construirlas, probarlas y ponerlas en producción, por le que es muy sencillo desarrollarlas, aunque no deja de presentar retos.
4. **Escalabilidad**. Esta es una de las razones por las que las API rest se han vuelto tan populares. Incrementar la cantidad de usuarios que se pueden atender con una API RESTful es más sencillo que son SOAP debido a la cacheabilidad y a que las conexiones sin estado permiten escalamiento horizontal (replicación de servidores) y por lo tanto los costos se abaratan. La mayoría de las API's grandes conocidas siguen este estilo.

### Desventajas de REST

1. **Flexibilidad**. La flexibilidad es un don y maldición. Cuando a las personas se les permite hacer lo que sea, harán hasta lo inimaginable, por lo que se pueden encontrar implementaciones horribles y sin una guía definida nuestra propia API puede quedar hecha un asco.
2. **Transacciones**. REST no establece una manera de manejar operaciones transaccionales, por lo que la implementación queda completamente del lado del diseño. Hay que tener en cuenta el manejo del estado, replicación de servidores, consistencia y [condiciones de carrera](https://es.wikipedia.org/wiki/Condici%C3%B3n_de_carrera). Esto no hace sencillo trabajar con transacciones en API's REST.
3. **Seguridad**. No estamos diciendo que REST sea más inseguro que SOAP, sino REST no establece los medios de protección de interacciones e información, por lo que queda completamente como decisión de los desarrolladores y arquitectos del sistema. Sin una implementación adecuada tu API quedará vulnerable.


## Otros estilos

Han surgido nuevas maneras de consumir y diseñar API's como [GraphQL](https://graphql.org/learn/) y [gRPC](https://grpc.io/), pero cada una merece su propio artículo.

## Nuestra API

Para crear nuestra API elegiremos el estilo RESTful, primero, por su popularidad, las aplicaciones y porque lo que aprendamos tendrá aplicaciones útiles inmeditas y en el futuro.

En el camino aprenderemos:

- Buenas prácticas de transferencia de datos y de estado
- Cómo comunicar errores
- Crear una estructura de mensajes intuitiva
- Versionamiento de nuestra API
- Nombrado de los endpoints
- Seguridad

El ejercicio será el siguiente:

> Crear una API que permita crear listas de vocabularios. Un usuario se registra y puede crear tantos vocabularios como desee. Un vocabulario consiste de una lista de palabras ornedas por tiempo de inserción y su definción, que puede ser tomada del diccionario (fija) o definida por el usuario. Además una palabra puede tener imágenes adjuntas.

Esta aplicación nos permitirá poner en práctica y aprender de todos los puntos antes mencionados y otros. No te pierdas el siguiente artículo.
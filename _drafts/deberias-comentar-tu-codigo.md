---
title: "¿Deberías comentar tu código?"
date: 2020-12-27
author: Héctor Patricio
tags: comments comentarios mantenibilidad código-mantenible ousterhout aposd
comments: true
excerpt: "Hay programadores que dice que los comentarios son un mal que se debería evitar al máximo. Aquí proponemos lo contrario: usa los comentarios correctamente para crear código mantenible, basados en las "
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/v1608012314/snapbuilder_ykt2d6.png
  teaser: https://res.cloudinary.com/hectorip/image/upload/v1608012314/snapbuilder_ykt2d6.png
  overlay_filter: rgba(0, 0, 0, 0.5)
---

Cuando hablamos de comentarios en el código, hay dos escuelas. La primera dice que debes usar los comentarios para **clarificar lo que quisiste expresar con tu código**, mientras que la segunda dice que deberías **evitarlos al máximo** y comentar tu código es un mal necesario que sólo expresa tu falta de habilidad para no hacer código lo suficientemente claro.

¿A cuál de los dos consejos deberías hacerle caso? En este artículo explicaremos por qué creemos que deberías ver los comentarios como una **herramienta necesaria**, valiosa y muy útil, y cómo usarlos para no caer en el extremo que ha llevado a algunas personas a tener una mala actitud hacia ellos.

## Un sistema sin documentación esta incompleto

Como desarrollador estarás de acuerdo que un sistema que no tiene la _calidad suficiente_ si no tiene documentación, es decir, información acerca del sistema que comunique cosas como la razón de existir de ciertos módulos, valores y funciones.

Si, además, tienes que modificar este sistema, será una pesadilla entender todo lo que los programadores anteriores hicieron o intentaron hacer. Si tienes que _usar_ algo sin documentación, es el mismo caso: tienes estudiar el código para saber como usarlo.

### Los comentarios te pueden ayudar en el futuro

Los comentarios estarán ahí para darte información y recordaste lo que hiciste, pero sobre todo **por qué** lo hiciste. Recuerda que la mente humana busca la eficiencia máxima de recursos, por lo que es probable que elimine información que no ocupe inmediatamente y que no recuerdas a menudo, como por qué esa variable tenía el valor 730 y no otro.

### Los comentarios son una buena herramienta de diseño

John Ousterhout, en "A Philosophy of Software Design" recomienda **empezar** con los comentarios antes de programar.

### El lenguaje de programación no es suficiente para expresar todo lo necesario

Todos los lenguajes de programación están pensados para ser un subconjunto del lenguaje humano que elimine las ambigüedades, manteniendo el mayor poder expresivo posible. Esto nos lleva a sus limitantes: es imposible, o por lo menos impráctico, intentar expresar cada idea con el código.

En la práctica el tiempo y los recursos para lograr algo son limitados, por lo que a veces es más conveniente y fácil para todos explicar lenguaje humano algo que intentar expresarlo con código.

## ¿Cómo usar los comentarios para que sean valiosos?

No todos los comentarios son valiosos, hablemos de algunas formas de aprovecharlos lo mejor posible para que contribuyan positivamente a aumentar la calidad del proyecto.

### Escribe los comentarios primero

Una de las partes más importantes de los comentarios como documentación es que deben ser concretos, cercanos a la realidad y que proporcionen la mayor cantidad de información útil posible.

Para lograr esto, se tienen que crear lo más cerca que puedas a la _creación del código_. Pero como todos sabemos que después de escribir y probar (básicamente) el código vamos a sentir que ya está terminado, es buena práctica obligarte a escribirlos antes, justo como propone TDD con las pruebas.

De esta manera te asegurarás que tu código esté documentado incluso antes de escribirlo y te servirán como una **herramienta de diseño** que te ayudará a pensar mejor en la usabilidad de tus módulos y piezas de software.

### Crea comentarios acerca de la interfaz

La interfaz es el **medio de uso** que tus módulos o funciones presentan para que las demás partes de tu sistema lo usen. Lo primero que deberías documentar y explicar es **esta interfaz**, para que más personas a parte de ti puedan usar este pedazo de código.

Debes escribir comentarios claros sobre:

* **Cómo usar esa pieza de código**
* **Por qué existe esa parte del sistema**
* **Qué efectos tiene usarla**

Este tipo de comentarios son los que aportan mayor valor al sistema y si están lo suficientemente completos, con ejemplos y explicaciones claras, son una documentación válida que está en un muy buen lugar: es fácil de encontrar y no se va a perder enterrada entre otros documentes que después nadie va a consultar.


### Evita los comentarios sobre la implementación

Los comentarios sobre la implementación son aquello que describen _qué_ estas haciendo, como por ejemplo, sumar número, abrir un archivo, etc. Estos comentarios normalmente son innecesarios, ya que lo que se está haciendo es obvio si el código es lo suficientemente expresivo y siempre deberíamos buscar que sea así.

De hecho, estos son los comentarios que hacen que la gente odie a los comentarios en general, pues en vez de proporcionar información extra son una carga que hay que mantener y pueden confundir si no son actualizados.

Si realmente sientes que tienes que explicar _qué_ estás haciendo con cierta pieza de código, primero pregúntate si no hay una manera de reescribirlo para que sea obvio. Si no existe o no es práctica esta solución, entonces escribe el comentario de la manera más concisa posible, incluyendo la razón de la existencia de ese código.

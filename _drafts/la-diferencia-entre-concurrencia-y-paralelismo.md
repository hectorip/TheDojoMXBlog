---
title: "La diferencia entre concurrencia y paralelismo"
date: 2019-04-08
author: Héctor Patricio
tags: concurrencia paralelismo go elixir
categories: 
comments: true
excerpt: "Muchos programadores confunden la concurrencia con el paralelismo, aunque son conceptos que se relacionan, no son lo mismo"
header:
  overlay_image: #image
---

Los términos **concurrencia** y **paralelismo** siempre han sido relevantes en el entorno de la computación y desarrollo de software. Casi no hay ningún sistema serio que no aplique lo que significan para trabajar decentemente. Hablemos de la diferencia entre ellos y cómo podemos aplicarlos en nuestros programas.
Pero decir que uno es el otro es como decir que las naranjas y manzanas son iguales.

Empecemos por el concepto más sencillo: el paralelismo.

## Paralelismo

El paralelismo se refiere a la ejecución _simultánea_ de varios procesos computacionales, que pueden estar relacionados entre ellos o no.

Un programa con un un buen diseño concurrente puede aprovecharse automáticamente o con muy poco esfuerzo extra de una aquitectura de ejecución paralela, aumentando la velocidad del programa conforme aumentan los recursos de procesamiento. La concurrencia es entonces un requisit previo para poder aprovechar un sistema de ejecución paralela al máximo.

### Ejemplos de paralelismo

## Concurrencia

Esta palabra intuitivamente la entendemos como la confluencia o el encuentro de varias cosas o procesos en un sólo lugar al mismo tiempo. Cuando un lugar está lleno de gente decimos que "está muy concurrido". Esto nos puede llevar a confundir el término con paralelismo. En cuanto a las ciencias computacionales, es algo totalmente diferente: es una manera de diseñar, componer o estructurar programas. **Concurrencia**, entonces, se puede definir de la siguiente forma:

> La composición de elementos (funciones, procesos, programas, etc) que se ejecutan independientemente pero interactúan entre sí.

Hablamos de composición en el sentido de "acomodo" o "estructura" e incluso "diseño".

Por lo tanto, un programa concurrente es uno que se vale de distintos procesos indpendientes para lograr su objetivo.
Pongamos unos ejemplo de la vida real.

#### El podcaster

Piensa en una persona que quiere grabar un podcast. Para facilitarse la vida ha escrito su proceso en una lista de tareas:
1. Crear borrador de los temas y el script
2. Grabar el episodio
3. Editar y decorar el episodio
4. Publicarlo en los sitios de podcast mas populares

Si logramos hacer que estos procesos puedan correr de manera independiente, tenemos un proceso concurrente, aunque se ejecute secuencialmente (por falta de recursos). ¿Son estos procesos independientes? Lo cierto es que cada uno necesita una entrada (que PUEDE venir del proceso anterior), pero no necesariamente la entrada producida por el proceso anterior. Es decir:

1. Crear el borrador -> Independiente
2. Grabar el episodio -> Puede o no ocupar un borrador, es mejor idea tener uno.
3. Editar -> Requiere uuna grabación que editar y decorar y produce un episodio final.
4. Publicar -> Requiere un episodio que publicar

Por lo tanto, estos procesos se pueden ejecutar independientemente. Entonces, con estas tareas (y la manera de organizarlas) podemos tener un proceso de creación de podcasts concurrente. Imagina por ejemplo que el podcaster decide crear una parte del borrador, digamos 5 minutos, y grabarlos, sólo para escucharse a sí mismo y probar el tono y el _feeling_. Despues repite la operación hasta tener 30 minutos de contenido. Este es un proceso que podemos decir que es concurrente porque aunque no podía grabar y escribir el borrador al mismo tiempo, estas tareas se estaban completando 'al mismo tiempo', no hizo una después de otra hasta completarla.

Imagínate el proceso algo así:

![Proceso del podcaster](https://res.cloudinary.com/hectorip/image/upload/v1555440917/IMG_0033_sypjyx.jpg)


Concurrencia es **manejar** varias tareas en un periodo de tiempo, aunque no se ejecuten simultáneamente.

#### El ajedrecista.

Ahora imagina a un Gran Maestro del ajedrez al que retan a enfrentarse con 10 personas a ciegas al mismo tiempo.
El ajedrecista acepta y juega contra los 10 formados en círculo.

![El ajedrecista](https://res.cloudinary.com/hectorip/image/upload/v1555440939/IMG_0034_dyakuk.jpg)

### Ejemplos de programas concurrentes

Ahora hablemos de algunos ejemplos de programas concurrentes, de la vida real:

1. **Sistema operativo**. Un sistema operativo ejecuta muchas tareas relacionadas entre sí para lograr que un sistema de hardware sea usable para los humanos, por ejemplo: leer entrada del ratón y el teclado, mostrar el resultado de los procesos en pantallas, ejecutar el reloj, ejecutar muchos programas que hacen de tu experiencia agradable (spotify, administrador de ventanas), servicios de red. Aunque las computadoras actuales tienen varios procesdores, no se acercan al número de tareas con las que un sistema opertivo **trata** al mismo tiempo.

2. **Servidor Web**. Los servidores web están diseñados para atender a muchos clientes (usuarios) dentro de un corto espacio de tiempo. Un servidor web está tratando con varios usuarios al mismo tiempo sin que necesariamente todas sus tareas se ejecuten simultáneamente.

3. **Navegador**. Un navegador web es un sistema naturalmente concurrente. Cada una las pestañas que tienes abiertas puede contar como una de las tareas con las que el pobre navegador web tiene que trabajar para mantenerte contento. No es necesario que esté corriendo el código de todas al mismo tiempo para funcionar, sino que usa métodos diversos para identificar exactamente qué debe estar ejecutando en cada instante.

### Modelos de concurrencia

Vamos a mencionar algunas formas que se han diseñado de manejar varios procesos al mismo tiempo.


## Diferencias

Como resumen: la concurrencia tiene que ver con el diseño del software mientras que el paralelismo tiene que ver con la ejecucición.

Por ejemplo, un sistema operativo es concurrente y aplica a diversas técnicas para coordinar todos los procesos que necesita para que logre hacer una computadora usable para los humanos. Este sistema no necesariamente es paralelo (y por mucho tiempo no lo pudieron ser), ya que si no cuenta con más de un medio físico para la ejecución simultánea de tareas o procesos recurre a técnicas de compartimiento de procesador que hacen que para los humanos parezca que ejecuta muchas tareas al mismo tiempo.

## Conclusión
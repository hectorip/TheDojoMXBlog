---
title: "¿Por qué deberías aprender Elixir?"
date: 2019-06-02
author: Héctor Patricio
tags: elixir fp programación-funcional
comments: true
excerpt: "Elixir es un lenguaje que recientemente ha estado haciendo ruido. Aquí te contamos algunas cosas de él para que te animes a aprenderlo."
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1440/v1559453191/jr-korpa-1316724-unsplash_f1ujyj.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1440/v1559453191/jr-korpa-1316724-unsplash_f1ujyj.jpg
  overlay_filter: rgba(0, 0, 0, 0.5)
---

Elixir es un lenguaje de programación bastante reciente (creado cerca de 2012), pero que está haciendo mucho ruido y más considerando que no tiene ninguno de los nombres legendarios del área de sistemas atrás ni a alguna empresa prominente.

En este post vamos a hablar de por qué es buena idea aprender Elixir en 2019.

## Un poco de historia

Elixir es un lenguaje de programación creado por José Valim, que empezó a ser programado en 2011 y su versión 1.0 salió a la luz en 2014. Ahora en Junio 2019 va en su **versión 1.8**. _Nació con la idea de mejorar el rendimiento de los programas sin afectar la productividad de los programadores_. José Valim era un contribuidor al núcleo de Rails, hasta que se dio cuenta de que no podría escalar hasta el grado que necesitaba, sobre todo por Ruby y sus limitaciones. Ahí empieza la historia de Elixir y el aprovechamiento de la concurrencia provista por Erlang y su máquina virtual, **BEAM**.

En el siguiente documental explican por qué se creó y cómo es que resuelve algunos problemas para diferentes empresas:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/lxYFOM3UJzo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Elixir es como el hijo de Erlang y Ruby. La belleza de Ruby y el poder de Erlang.

## Características de Elixir

Platiquemos un poco de las características de este lenguaje que lo hacen muy adecuado para crear programas modernos, aunque aprovecha tecnología de hace 30 años.

### Funcional

Una de las primeras cosas que resalta de Elixir es que es un lenguaje funcional, como Erlang. En [otro post](/) explicamos las ventajas y características de la programación funcional pero recordemos un poco las dos principales:

1. Se basan en funciones puras
2. Los valores son inmutables

A partir de estas dos características se desprenden muchas otras que llevan a una mejor descomposición de los problemas, mejor rendimiento y mantenibilidad para los problemas adecuados:

1. Funciones de orden superior (o tratar las funciones como cualquier otro valor)
2. Evaluación retardada o perezosa
3. Transparencia referencial
4. Independencia de contexto de ejecución
5. Pipelines para transforamción de datos

Debemos tener presente que la programación funcional no es la mejor opción para todos los casos, sobre todo presenta dificultades cuando se tienen que mantener estructuras de datos muy grandes que se tengan que modificar constantemente, algunos lenguajes tiene trucos inteligentes pero sigue sin ser lo óptimo.

### BEAM - Erlang

La tecnología que está atrás de Elixir es Erlang y su máquina virutal, la [BEAM](http://erlang.org/faq/implementations.html). Esto quiere decir que los programas hechos con Elixir corren como su fuera un programa hecho en Erlang sobre el entorno de ejecución que originalmente fue creado para él. Además al correr sobre el mismo entorno, Elixir puede aprovechar todo lo que ya existe en Erlang, desde sus librerías hasta varias de las herramientas de desarrollo.

¿Por qué es tan importante la máquina virtual? La BEAM es la encargada de la ejecución de los programas creados con Erlang y [muchos otros lenguajes](https://github.com/llaisdy/beam_languages), entre ellos Elixir. Se encarga de distribuir el procesamiento y administrar la memoria, así como conectarse con los nodos necesarios para la ejecución del programa. Además adminsitra y levanta los procesos que los programas requieren. La BEAM es el soporte para las características que vienen.

### Distribuido

La BEAM está pensada para trabajar con sistemas distribuidos, específicamente puede funcionar a través de una red de computadoras y distirbuir el programa y la carga a través de todos los nodos que la componen. De esta manera puedes crear aplicaciones que aprovechen la memoria y el procesamiento de toda una red de computadoras.

Así nació Erlang y ahora puedes aprovechar estas características con Elixir. Por ejemplo, puedes llamar y mandar mensajes a un proceso que vive en una computadora al otro lado del mundo justo como si estuviera viviendo en tu misma computadora, siempre y cuando la BEAM tenga conectados los nodos.

Esto es una de las características que suma a una característica de la que vamos a hablar más tarde: **resiliencia**.

### Concurrente

Elixir y Erlang permiten crear programas concurrenrtes de manera sencilla. Su modelo de concurrencia está basado en **actores**, que son pequeños procesos muy ligeros que no comparten memoria entre ellos y se comunican mediante mensajes colocados en un *mailbox*. Este tipo de concurrencia permite crear también supervisores, que son procesos que "vigilan" a otros procesos y toman acciones cuando terminan.

Todo esto permite crear estructuras de procesos complejas que nos habilitan para lograr diferentes obejtivos. Un ejemplo son los **áboles de supervisión** (en realidad todas las aplicaicones de Erlang y Elixir lo tienen). Que es una estrucutura de procesos que permite crear un programa resistente a fallos.

Siendo uno de los puntos principales del lenguaje y la BEAM, existe un conjunto de patrones, librerías y procesos diseñados para aprovechar las características concurrentes llamado **OTP**.

### Resiliente

Las características de las que hemos platicado llevan al lenguaje a una característica muy importante. Las aplicaciones hechas en Elixir pueden llegar ser muy, muy resilientes. Las aplicaciones hechas en erlang pueden ofrecer **99.9999999%** de disponibilidad, lo que quiere decir que sólamente van a estar indisponibles 32 milisengundos en un año. A esta resiliencia contribuyen tres de las características antes mencionadas: la distribución de al computación y la memoria, la concurrencia y los árboles de supervisión.

### Velocidad

Al ser un lenguaje compilado y gracias a la BEAM, que aprovecha todos los núcleos de procesamiento disponibles, Elixir es un lenguaje muy rápido en general. Aquí una muesta del tiempo que tarda en responder una petición web usando un framework llamado Phoenix:

![Tiempo de respuesta de Phoenix](https://res.cloudinary.com/hectorip/image/upload/v1559515060/Screenshot_2019-06-02_17.36.52_sx8dgs.png)

### Fácil para empezar a programar

Elixir fue creado con el objetivo de ser divertido y fácil de aprender aún siendo un lenguaje funcional. Sigue la filosofía de Ruby. Hereda gran parte de la sintaxis y las ideas de Ruby (a final de cuentas de allí nació). Ruby nació para ser un lenguaje disfrutable y lo mismo Elixir. La sintaxis y operadores lo hacen fácil de entender una vez que entindes que no está basado en la sintaxis de C.

Por ejemplo, uno de los operadores más usados, el pipe, permite hacer cosas bastante legibles:

```elixir
import Enum, only: [map: 2, sum: 1, zip: 2]

calculados = [1, 2, 3, 4]
reales = [0.5, 0.2., 1.7, 5.9]

error = calculados
  |> zip(reales) 
  |> map(fn {c, r}-> :math.pow(c-r, 2) end)
  |> sum
```
Elixir es de **tipado dinámico**, es decir, no necesitas declarar y mantener los tipos de las varibles y de cada operación.

Lo anterior no quiere decir que todo sea fácil en Elixir. El modelo de programación que lo respalda (funcional), la sintaxis no basada en C y el modelo de [concurrencia](/2019/04/17/la-diferencia-entre-concurrencia-y-paralelismo.html) basado en actores no son cosas con las que tratemos todos los días si venimos de la programción no concurrente y en su mayor parte basada en la herencia de C.

### Grandes herramientas

Una caracterísitca que resalta de Elixir son las herramientas para desarrollo con las que cuenta. Primero, puede aprovecharse de todas las que Erlang provee y segundo porque los creadores pusieron especial atención en esto.
La principal herramienta para desrrollo en Elixir es [mix](https://elixir-lang.org/getting-started/mix-otp/introduction-to-mix.html) que permite desde iniciar un proyecto hasta monitorear un proyecto en producción mediante conectarse a la máquina virtual que lo está corriendo.

Otra de las herramientas/características que la BEAM tiene son **actulización de código en vivo** (hot code swapping). Esto es especialmente difícil de lograr con sistemas que mantienen un estado en memoria, pero por lo menos es posible y permitido por la máquina virtual.

Hablando por ejemplo de monitorear un programa que estea corriendo, la BEAM permite examinarlo hasta de manera visual:

![Visualizador de procesos de Erlang](https://res.cloudinary.com/hectorip/image/upload/v1559505687/Screenshot_2019-06-02_15.00.01_u1xiwd.png)

### Metaporgramación

La metagprogramación se refiere a la capacidad de algunos lenguajes de crear código (o su representación interna) con un programa hecho en el mismo lenguaje. Gran parte (casi todo) en Elixir está hecho con esta técnica, es decir, Elixir está implementado en Elixir.

Pero lo mejor es que el equipo deicidió darle estas capacidades a los usuarios del lenguaje. Así que, gracias a esto, podemos manejar el AST (Abstract Syntax Tree o Árbol de Sintaxis abstracta), que es la representación interna del lenguaje, como si fuera un estructura común de datos y crear nuestas propias macros y estructuras sintácticas.

Esta habilidad permite por ejemplo la creción de macros para crear tu propio mini-lenguaje adentro de Elixir, lo que generalmente se conoce como un DSL (Domain Specific Language), adaptado a lo que necesitas en el sistema que estés progrmando.

La siguiente imagen da un ejemplo de cómo puede lucir un lenguaje para un domino específico.

![Ejemplo de DSL en Elixir](https://res.cloudinary.com/hectorip/image/upload/v1559509232/20180416_1_rlvoac.png)

### Gran comunidad

La comunidad alrededor de Elixir es uno de los puntos más fuertes. Grandes programadores de otras comunidades y con mucha experiencia están apoyándolo y desarrollando el mismo lenguaje, librerías y herramientas para él, pero más importante, son muy abiertos y fomentan el trabajo de comunidad contestando dudas directamente y mentoreando a programadores más inexpertos.

Esto ha hecho que la comunidad de Elixir sea muy receptiva, cordial y que las herramientas y librerías estén creciendo mucho en el poco tiempo de vida que tiene.

## Desventajas

Nada es perfecto. Al empezar a programar en Elixir te puedes topar con algunas problemos, de los que ahora hablaremos.

### Reciente creación

Su juventud como lenguje hace que muchos de los problemas que te enfrentas sean recientes, no haya tantos programadores experimentados y la comunidad sea más pequña (aunque está creciendo). Esto también implica que encontrarás menos librerías y algunas tendrán aún fallas de algún tipo por no haber sido probadas completamente por una gran cantidad de usuarios.

Si vas a iniciar un proyecto que requiera muchos programadores, conseguir programadores de Elixir será más difícil que con otros lenguajes más longevos. Pero siempre puedes enseñarles 😉.

### Rendimiento crudo bajo en comparación con otras soluciones

La BEAM no es tan poderosa en procesamiento numérico como lo son otras máquinas virtuales (como la JVM) o como suluciones que compilan direcrtamente a código máquina (Rust o Go). Es mucho mucho más lenta que estos últimos, lo cuál no la hace una solción especialmente buena cuando se trata de procesar grandes cantidades de información por sí sola (procesmiento de imágenes, análisis y transforamción de datos). Para solventar esto, la BEAM soporta "plugins" llamados NIF's, escritos en otros lenguajes que permiten delegar esta tarea a módulos y funciones escritas en otro lenguaje más adecuado para la tarea en cuestión.

## Casos de Uso

Con las carcterísticas mencionadas anteriormente te podrás dar una idea de para qué es bueno elixir:

- **Sistemas de misión crítica**. Si necesitas un sistema que no se muera con nada y sea capaz de aguantar muchos tipos diferentes de fallas (incluso desconocidas) Elixir es una gran elección.

- **Sistemas web**. La naturaleza de uso de la web actual hace que Elixir sea una gran elección si quieres que tu sistema ocupe pocos recursos, sea confiable, escale fácilmente y aguante una cantidad brutal de usuario simultáneamente.

- **Sistemas en tiempo real ligero (soft real-time)**. Las características de Elixir lo hacen adecuado para manejar interacciones en tiempo real con muy muy poco atraso en la comunicación. Es adecuado para juegos, salas de chat, sistemas de notificaciones e incluso IoT.

- **Sistemas que tienen que trabajar sobre muchas máquinas**. La BEAM está especialmente hecha para eso.

## En dónde evitarlo

Las limitantes en cuanto al procesamiento de información cruda (number crunching) pueden hacer que Elixir no sea la mejor elección si la función principal de tu programa es algo que incluya:

- Muchas operaciones matemáticas sobre grandes cantidades de números: procesamiento y transformación de imágenes, análisis de video, etc.

## Recursos de aprendizaje.

En este post puedes ver unos cuantos recursos de aprendizaje: [Recusros de aprendizaje de Elixir](https://hectorip.com/2018/12/27/aprendiendo-elixir.html), pero en este blog vamos a ir subiendo algunos ejercicios para que puedas aprender más de él.

No dudes en comentarnos tus dudas y podemos compartir nuestras experiencias.
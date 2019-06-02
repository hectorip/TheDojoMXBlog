---
title: "¿Por qué deberías aprender Elixir?"
date: 2019-06-02
author: Héctor Patricio
tags: elixir fp programación-funcional
comments: true
excerpt: "Escribe aquí un buen resumen de tu artículo"
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1440/v1559453191/jr-korpa-1316724-unsplash_f1ujyj.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1440/v1559453191/jr-korpa-1316724-unsplash_f1ujyj.jpg
  overlay_filter: rgba(0, 0, 0, 0.5)
---

Elixir es un lenguaje de programación bastante reciente (cerca de 2012), pero que está haciendo mucho ruido y más considerando que no tiene ninguno de los nombres legendarios del área de sistemas atrás nin niguna empresa prominente.

En este post vamos a habalar de por qué es buena idea aprender Elixir en 2019.

## Un poco de historia

Elixir es un lenguaje de programación creado por José Valim, que empezó a ser programado en 2011 y su versión 1.0 salió a la luz en 2014. Ahora en Junio 2019 va en su **versión 1.8**. _Nació con la idea de mejorar el rendimiento de los programas sin afectar la productividad de los programadores_. José Valim era un contribuidor al núcleo de Rails, hasta que se dio cuenta de que no podría escalar hasta el grado que necesitaba, sobre todo por Ruby y sus limitaciones. Ahí empieza la historia de Elixir y el aprovechamiento de la concurrencia provista por Erlang y su máquina virtual, **BEAM**.

En el siguiente documental explican por qué se creó y cómo es que resuelve algunos problemas para diferentes empresas:

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/lxYFOM3UJzo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

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
5. Pipelines

Debemos tener presente que la programación funcional no es la mejor opción para todos los casos, sobre todo presenta dificultades cuando se tienen que mantener estructuras de datos muy grandes que se tengan que modificar constantemente, algunos lenguajes tiene trucos inteligentes pero sigue sin ser lo óptimo.

### BEAM - Erlang

La tecnología que está atrás de Elixir es Erlang y su máquina virutal. Esto quiere decir que los programas hechos con Elixir corren como su fuera un programa hecho en Erlang sobre el entorno de ejecución que originalmente fue creado para él. Además al correr sobre el mismo entorno, Elixir puede aprovechar todo lo que ya existe en Erlang, desde sus librerías hasta varias de las herramientas de desarrollo.

¿Por qué es tan importante la máquina virtual? La BEAM es la encargada de la ejecución de los programas creados con Erlang y [muchos otros lenguajes](https://github.com/llaisdy/beam_languages), entre ellos Elixir. Se encarga de distribuir el procesamiento y administrar la memoria, así como conectarse con los nodos necesarios. 

### Sistemas Distribuidos

La BEAM está pensada para trabajar con sistemas distribuidos, específicamente, puede funcionar a través de una red de computadoras y distirbuir el programa y la carga a través de todos los nodos que la componen.

### Fácil de aprender

Elixir fue creado con el objetivo de ser divertido y fácil de aprender aún siendo un lenguaje funcional.

### Grandes herramientas

Una caracterísitca que resalta de Elixir son las herramientas para desarrollo con las que cuenta. Primero, puede aprovecharse de todas las que Erlang provee y segundo porque los creadores pusieron especial atención en esto.

### Metaporgramación

La metagprogramación se refiere a la capacidad de algunos lenguajes de crear código (o su representación interna) con un programa hecho en el mismo lenguaje. Gran parte (casi todo) en Elixir está hecho con esta técnica, es decir, Elixir está implementado en Elixir.

Pero lo mejor es que el equipo deicidió darle estas capacidades a los usuarios del lenguaje. Así que, gracias a esto, podemos manejar el AST (Abstract Syntax Tree o Árbol de Sintaxis abstracta), que es la representación interna del lenguaje, como si fuera un estructura común de datos y crear nuestas propias macros y estructuras sintácticas.

Esta habilidad permite por ejemplo la creción de macros para crear tu propio mini-lenguaje adentro de Elixir, lo que generalmente se conoce como un DSL (Domain Specific Language), adaptado a lo que necesitas en el sistema que estés progrmando.

### Gran comunidad

La comunidad alrededor de Elixir es uno de los puntos más fuertes. Grandes programadores de otras comunidades y con mucha experiencia están apoyándolo y desarrollando el mismo lenguaje, librerías y herramientas para él, pero más importante, son muy abiertos y fomentan el trabajo de comunidad contestando dudas directamente y mentoreando a programadores más inexpertos.

Esto ha hecho que la comunidad de Elixir sea muy receptiva, cordial y que las herramientas y librerías estén creciendo mucho en el poco tiempo de vida que tiene.


## Desventajas

### Reciente creación
### Menos librerías

## Casos de Uso

## En dónde evitarlo

## Elixir Just feels right


## Recursos de aprendizaje
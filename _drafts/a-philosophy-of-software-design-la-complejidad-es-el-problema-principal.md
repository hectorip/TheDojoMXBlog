---
title: "A Philosophy of Software Design: Tres formas de identificar la complejidad"
date: 2020-02-12
author: Héctor Patricio
tags: ousterhout complejidad diseño-de-software posd
comments: true
excerpt: "Aprende a descubrir la complejidad en tus proyectos"
header:
  overlay_image: 
  teaser: 
  overlay_filer: rgba(0, 0, 0, 0.5)
---

> "Controlar la complejidad es la esencia de la programación" - Brian W. Kernighan

Muchas mentes brillantes dedicadas al desarrollo de software han estado de acuerdo en que el principal problema al crear y mantener programas es el manejo de la complejidad.

Podemos decir que algo complejo es aquello que está compuesto por muchas piezas relacionadas entre ellas. [Ousterhout](http://web.stanford.edu/~ouster/cgi-bin/home.php) lo define de manera práctica _como todo aquello que el software sea difícil de entender, escribir o mantener_.

> Complexity is more apparent to readers than writers. If you write a piece of code and it seems simple to you, but other people think it is complex, then it is complex.

> La complejidad es más visible para los lectores que para los escritores [del código].

Philosophy of Software Design habla de tres formas de identificar un programa más complejo de lo que debería ser:

1. Amplificación de cambios
2. Carga cognitiva
3. Desconocidos desconocidos

Identificar la complejidad es una habilidad crítica para el buen diseño de software, ter permitirá crear sistemas más simples y evitará que gastes recursos en desarrollar soluciones que son demasiado complejas.

## Amplificación de cambios

Este síntoma de la complejidad se hace obvio cuando estás haciendo un cambio que debió haber sido sencillo y tienes que tocar 7 archivos, 3 clase y 4 funciones. Se refiere a que una funcionalidad del programa está repartida en muchos lados y para lograr hacer un cambio hay que tocar muchas partes del sistema.


## Carga cognitiva

Si tienes que mantener muchas cosas en la cabeza para poder entender el sistema, es complejo.

## Desconocidos desconocidos

¿Tienes miedo de cambiar algo porque no sabes lo que pueda pasar y no hay ni documentación a la que puedas referirte? El sistema tiene información que no sabes que no sabes.


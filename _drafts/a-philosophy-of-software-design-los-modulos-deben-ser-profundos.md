---
title: "A Philosophy of Software Design: Los módulos deben ser profundos"
date: 2020-02-26
author: Héctor Patricio
tags: módulo PoSD ousterhout complejidad función
comments: true
excerpt: "Veamos algunos lineamientos para el diseño de funciones/clases/módulos que ayudarán a reducir la complejidad de tus sistemas de software."
header:
  overlay_image: 
  teaser: 
  overlay_filer: rgba(0, 0, 0, 0.5)
---

Para reducir la complejidad de los programas es importante tener técnicas definidas. La primera que vamos a analizar es la organización y separación de código a alto nivel, es decir separación en módulos.

Una definición fácil y amplia de "módulo" dada por ["A Philosophy of Software Design"](https://amzn.to/2H92nwA) es: _todo aquello que agrupe código, proveyendo encapsulamiento_, es decir que agrupe comportamiento en detrás de una interfaz.

Un módulo puede ser una función, una clase, un paquete o cosas similares dependiendo del lenguaje de programación. Un módulo incluso puede ser una API HTTP u otro programa.

Como resumen: **un módulo permite hacer _algo_ mediante una interfaz.**

## Interfaces


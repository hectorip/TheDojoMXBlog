---
title: "A Philosophy of Software Design: Desarrollo Táctico vs Estratégico"
date: 2020-02-11
author: Héctor Patricio
tags: a-philosophy-of-software-design complejidad 
comments: true
excerpt: "Dos diferentes formas de desarrollar sistemas de software"
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1200/v1581404404/will-francis-Rm3nWQiDTzg-unsplash_cxpkvl.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1200/v1581404404/will-francis-Rm3nWQiDTzg-unsplash_cxpkvl.jpg
  overlay_filer: rgba(0, 0, 0, 0.5)
---

Cuando desarrollas software tienes dos actitudes para escoger: desarrollas de forma rápida y sucia (desarrollo táctico) o de forma ordenada, planeada y pensando en el futuro. Cada uno de estos tipos de desarrollo o filosofías de desarrollo tiene ventajas y desventajas. Pero veamos a más detalle de qué trata cada uno.

## Desarrollo táctico

Está caracterizado por la alta velocidad inicial con la que empiezas a desarrollar y crear las funciones de tu programa. Con esta actitud, tu principal objetivo es tener _código que funcione_. Con esta forma de trabajo no gastas mucho tiempo buscando el mejor diseño para tu programa sino que te enfocas en terminas lo más rápido posible. Tu vista está en el corto plazo. 

Con tal de terminar con la tarea lo más pronto posible no importa si agregas algo de complejidad al sistema: código duro por aquí, duplicación por allá, manejo de excepciones deficiente(envolver todo en un try/catch), etc.

Este tipo de desarrollo es alentado por los negocios que quieren que su código o programa esté tan pronto como sea posible sin importar el costo. ¿Tiene uso este código y esta forma de pensar? Por supuesto: cuando se quiere construir un producto muy muy rápido y se tiene conciencia de que _será desechable_.

El desarrollo táctico produce programas que con el tiempo se van haciendo más y más difíciles de mantener, hasta que es tan impráctico que parece más fácil volver a hacerlo. **La velocidad de desarrollo se va reduciendo.**

Una vez que empiezas a programar un sistema de esta forma, es muy difícil cambiar. Y lo más triste es que la mayoría de las organizaciones y programadores prefieren este método.

## Desarrollo Estratégico

Este tipo de desarrollo se caracteriza por poner atención en el diseño y la calidad del código. Lo más importante no es directamente terminar la tarea pendiente sino también hacerlo de manera que facilite las tareas futuras y mantenga la complejidad bajo control. La tarea principal es _crear un muy buen diseño_.

Para el desarrollo estratégico **código que funciona no es suficiente**. En vez de introducir partes que hagan más complejo el código, buscas mejorar aunque sea una pequeña parte del código cada que trabajas en él.

Esto no quiere decir que harás todo el diseño por adelantado, sino que se va a ir creando un buen diseño de las partes que se vayan necesitando.

En pocas palabras, es tener una actitud de inversión en la base de código.

Esta actitud te hará ir más lento al principio, pero con el tiempo el equipo acelerará y podrá crear nuevas funciones muy rápido.

Ejemplos de desarrollo estratégico: probar varias implementaciones hasta encontrar la más limpia, documentar y comentar el código, limpiar y mejorar el código cada que sea posible.

La siguiente imagen ilustra cómo se comporta el avance total en las dos formas de programar:

![Comparación desarrollo táctico vs estratégico](https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1200/v1581404091/Untitled_Artwork_2_op8k0e.jpg)


¿Qué tipo de desarrollo conviene para tu proyecto según su tiempo de vida?

Este y los siguientes artículos están basados en el libro ["A Philosophy of Software Design"](https://amzn.to/2H92nwA) de John K. Ousterhout.

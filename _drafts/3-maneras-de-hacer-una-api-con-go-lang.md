---
title: "3 maneras de hacer una API con Go Lang"
date: 2019-11-23
author: Héctor Patricio
tags:
categories: 
comments: true
excerpt: "Escribe aquí un buen resumen de tu artículo"
header:
  overlay_image: #image
---

Go es uno de los lenguajes de reciente creación más exitosos de los últimos tiempos. Ya hablamos de [por qué deberías aprenderlo](/2019/09/01/por-que-deberias-aprender-go.html).

Ahora hablemos de un caso de uso práctico: **úsalo para crear una API**. En este artículo nos enfocaremos en la parte de comunicación. La funcionalidad básica de tu API puede o no adaptarse completamente a Go (no es es tan fácil de escribir como un lenguaje dinámico como Python), pero definitivamente es un lenguaje excelente para crear interfaces de comunicación web, debido a su alto rendimiento y eficiencia.

Puedes ver algunas de las comparativas en los siguientes artículos:

- [Comparando el rendimiento de Go, NodeJS y Elixir](https://stressgrid.com/blog/benchmarking_go_vs_node_vs_elixir/). TL;DR: Go y Elixir llegana  manejar más de 100k conexiones sin ningún problema, Node empieza con problemas desde las 30k y el más eficiente en cómputo y memoria utilizda por mucho es Go.
- [Comparación de frameworks web ligeros](https://github.com/mroth/phoenix-showdown). Este artículo es un poco viejo, pero el resumen es que Gin (un framework web ligero de Go) es el que más peticiones soporta por segundo y con una consistencia excelente.

![Comparativa de microframworks Web](https://res.cloudinary.com/hectorip/image/upload/v1574629781/Screenshot_2019-11-24_15.09.25_ozqwcu.png)


Ahora sí, hablemos de tres formas de crear una API sobre HTTP para tu próximo proyecto.

## La biblioteca estándar

Cuando hice mi primer proyecto en Go, gran parte de la investigación sobre qué usar para crear un proyecto web apuntaba los paquetes nativos de Go son el camino.

Go tiene una biblioteca estándar que cubre muchas de las necesidades de un desarrollador moderno.

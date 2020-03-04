---
title: "A Philosophy of Software Design: Ocultar información"
date: 2020-03-03
author: Héctor Patricio
tags: PoSD interfaces módulo complejidad diseño-de-software
comments: true
excerpt: "Ocultar información es una de las claves para reducir la complejidad, veamos algunas maneras de lograrlo."
header:
  overlay_image: #image
  teaser: #image
  overlay_filer: rgba(0, 0, 0, 0.5)
---

En [el artículo anterior]() vimos por qué es bueno que los módulos sean profundos, es decir, oculten muchos detalles de implementación y funcionalidades detrás de una interfaz lo más sencilla posible. En este y los siguientes artículos vamos a ver maneras prácticas de lograr esto, basado en ejemplos de ["A Philosophy of Software Design"](https://amzn.to/2H92nwA).

En este primer artículo hablaremos de cómo **ocultar información** que no es necesario saber para usar los módulos, ya que complicaría su uso, creando [carga cognitiva](), uno de los síntomas y consecuencias de la complejidad innecesaria.


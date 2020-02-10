---
title: "A Philosophy of Software Design: Desarrollo Táctico vs Estratégico"
date: 2020-02-08
author: Héctor Patricio
tags:
categories: 
comments: true
excerpt: "Dos diferentes formas de desarrollar sistemas de software"
header:
  overlay_image: 
  teaser: #image
  overlay_filer: rgba(0, 0, 0, 0.5)
---

Cuando desarrollas software tienes dos actitudes para escoger: desarrollas de forma rápida y sucia (desarrollo táctico) o de forma ordenada, planeada y pensando en el futuro. Cada uno de estos tipos de desarrollo o filosofías de desarrollo tiene ventajas y desventajas. Pero veamos a más detalle de qué trata cada uno.

## Desarrollo táctico

Está caracterizado por la alta velocidad inicial con la que empiezas a desarrollar y crear las funciones de tu programa. Con esta actitud, tu principal objetivo es tener _código que funcione_. Con esta forma de trabajo no gastas mucho tiempo buscando el mejor diseño para tu programa sino que te enfocas en terminas lo más rápido posible. Tu vista está en el corto plazo. 

Con tal de terminar con la tarea lo más pronto posible no importa si agregas algo de complejidad al sistema: código duro por aquí, duplicación por allá, manejo de excepciones deficiente(envolver todo en un try/catch), etc.

Este tipo de desarrollo es alentado por los negocios que quieren que su código o programa esté tan pronto como sea posible sin importar el costo. ¿Tiene uso este código y esta forma de pensar?

Una vez que empiezas a programar un sistema de esta forma, es muy difícil cambiar. Y lo más triste es que la mayoría de las organizaciones y programadores prefieren este método.

## Desarrollo Estratégico

Este tipo de desarrollo se caracteriza por poner atención en el diseño y la calidad _del código_.

Este y los siguientes artículos están basados en el libro ["A Philosophy of Software Design"](https://amzn.to/2H92nwA) de John K. Ousterhout.


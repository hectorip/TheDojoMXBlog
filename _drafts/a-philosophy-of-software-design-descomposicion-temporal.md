---
title: "A Philosophy of Software Design: Descomposición Temporal"
date: 2020-03-14
author: Héctor Patricio
tags: PoSD descomposición-temporal software-design complexity interfaces
comments: true
excerpt: "Una forma de dejar escapar información es mediante forzar el orden de las operaciones de un módulo. Veamos cómo evitarlo."
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1400/v1584251653/A240034B-230E-4BA2-843D-32357D921811_mwdnzk.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1400/v1584251653/A240034B-230E-4BA2-843D-32357D921811_mwdnzk.jpg
  overlay_filer: rgba(0, 0, 0, 0.5)
---

En el artículo pasado hablamos de una forma de evitar una fuga de información, que consiste en encapsular una decisión de diseño en un módulo.

Otra forma de dejar escapar información no relevante para los usuarios de una pieza de software es mediante obligarlos a usarla siempre de la misma forma, con el mismo orden de operaciones reglas de operación implícita. Esto se llama descomposición temporal. Hablemos más de ella.

## Qué es la descomposición temporal

> En descomposición temporal, la estructura de un sistema corresponde **al orden en el tiempo** en el que las operaciones **ocurrirán**. - John Ousterhout

La descomposición temporal implica repetir o separar una decisión de diseño por causa del _orden en que se usan diferentes partes del sistema_.

## Ejemplos

John Ousterhout menciona un ejercicio que puso a sus alumnos en el que tenían que crear un programa implementando el protocolo HTTP. Algunos equipos crearon una clase para recibir el mensaje desde la red y otra clase para leerlo, creando así un caso claro de descomposición temporal: como las operaciones sucedían en diferentes momentos (primero recibes y luego lees y procesas) los separaron lógicamente en dos clases que se usaban siempre una detrás de otra. La fuga de información se dio porque para recibir un de HTTP _tienes_ que leer parte del mensaje y entonces la lógica de lectura del mensaje está en _ambas clases_.

Otro ejemplo más o menos obvio es la lectura y escritura de archivos. Si quieres trabajar con archivos, el orden de las operaciones es la siguiente: 

1. Abrir
2. Leer y operar con información del archivo
3. Escribir el archivo

Un muy mal diseño 
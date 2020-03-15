---
title: "A Philosophy of Software Design: Descomposición Temporal"
date: 2020-03-14
author: Héctor Patricio
tags: PoSD descomposición-temporal software-design complexity interfaces
comments: true
excerpt: "Una forma de dejar escapara in"
header:
  overlay_image: #image
  teaser: #image
  overlay_filer: rgba(0, 0, 0, 0.5)
---

En el artículo pasado hablamos de una forma de evitar una fuga de información, que consiste en encapsular una decisión de diseño en un módulo.

Otra forma de dejar escapar información no relevante para los usuarios de una pieza de software que hagamos es mediante obligarlos a usarla siempre de la misma forma, con el mismo orden de operaciones reglas de operación implícita. Esto se llama descomposición temporal. Hablemos más de ella.

## Qué es la descomposición temporal

> En descomposición temporal, la estructura de un sistema corresponde **al orden en el tiempo** en el que las operaciones **ocurrirán**. - John Ousterhout
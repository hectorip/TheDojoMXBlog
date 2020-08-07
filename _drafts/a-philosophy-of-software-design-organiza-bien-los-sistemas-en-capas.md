---
title: "A Philosophy of Software Design: Organiza bien los sistemas en capas"
date: 2020-04-15
author: Héctor Patricio
tags:
comments: true
excerpt: "Resuelve problemas de organización de código mediante un sistema en capas."
header:
  overlay_image: 
  teaser: 
  overlay_filer: "rgba(0, 0, 0, 0.5)"
---

Hemos escuchado muchísimo acerca de los sistemas en capas como MVC, MVT, MV*, _MVADFGDFD_ etc. La mayoría de los sistemas actuales se organiza así: **en capas**.

Hablemos de por qué es efectiva esta forma de organización
de código, de sus características y cómo debemos organizar el código para sacar el máximo provecho.

## Características de los sistemas en capas

Sabemos que la mejor forma de organización de un proyecto es **descomponerlo** en partes independientes que **oculten** información de otras.

La comunicación entre las diferentes partes se da por medio de una **interfaz**. Esta interfaz, es la **API** del componente.

## Qué evitar

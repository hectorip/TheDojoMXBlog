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

Hemos escuchado muchísimo acerca de los sistemas en capas como _Modelo-Vista-Controlador_, _Modelo-Vista-Template, Modelo-Vista-*, _MVADFGDFD_ etc. y eso es poruque la mayoría de los sistemas actuales se organiza así: **en capas**.

Hablemos de por qué es efectiva esta forma de organización (o patrón de arquitectura)
de código, de sus características y cómo podemos aprovecharla para sacar el máximo provecho.

## Características de los sistemas en capas

Sabemos que la mejor forma de organización de un proyecto es **descomponerlo** en partes independientes que **oculten** información de otras.

La comunicación entre las diferentes partes se da por medio de una **interfaz**. Esta interfaz, es la **API** del componente, ya que será usada de manera automática por otra parte del programa.

En un sistema en capas el conjunto de elementos pertenecientes a una capa sólo se puede comunicar con la capa superior y con la capa inferior.

Si un sistema tiene 10 capas, cada componente puede comunicarse máximo con 2 capas.

En los sistemas más comunes, como el de 3 capas (MVC, MVT, MV*), sólamente la capa intermedia (el controlador, por ejemplo) puede comunicarse con dos capas, mientras que las otras sólo se comunican con la intermedia.


## Qué evitar

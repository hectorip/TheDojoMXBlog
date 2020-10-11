---
title: "Tipos de algoritmos criptográficos: cifrados de Bloque"
date: 2020-10-06
author: Héctor Patricio
tags:
categories:
comments: true
excerpt: "Escribe aquí un buen resumen de tu artículo"
header:
  overlay_image: #image
  teaser: #image
  overlay_filter: rgba(0, 0, 0, 0.5)
---

Ya hablamos de lo que es [la criptografía](/2019/11/12/criptografia-basica-para-programadores-que-es-la-criptografia.html), ahora empecemos a hablar de los tipos de
algoritmos criptográficos que existen, sus características y sus principales diferencias.

## Cifrado Simétrico

Empecemos hablando de los algoritmos que requieren una sola llave (privada o que hay que mantener secreta), para funcionar: los cifrados simétricos.

### Cifrados de Bloque

Los cifrados de bloque funcionan como su nombre lo dice: rompe el contenido a cifrar en bloques del mismo tamaño y mediante una combinación de estos bloques (modo de operación) genera el cifrado final.

Algunos ejemplos de estos algoritmos de cifrado son el DES (Estadounidense), GOST 28147-89 y el actual **AES**.

Un bloque cifrado es una _permutación pseudoaleatoria_ de bits, es decir un conjunto de bits que _parecen_ o son indistinguibles de bits generados completamente de manera aleatoria.
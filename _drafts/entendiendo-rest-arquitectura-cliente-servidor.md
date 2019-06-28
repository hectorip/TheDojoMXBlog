---
title: "Entendiendo REST: Arquitectura cliente-servidor"
date: 2019-06-22
author: Héctor Patricio
tags:
categories: 
comments: true
excerpt: "Escribe aquí un buen resumen de tu artículo"
header:
  overlay_image: 
  teaser: 
  overlay_filter: rgba(0, 0, 0, 0.5)
---

Ya hablamos de las [motivaciones detrás del estilo arquitectural REST](). Ahora empecemos con la primera de sus características o restricciones, que la empieza a definir: la arquitectura cliente-servidor.

Pero un momento, ¿acaso no es la única que existe para sistemas web o sistemas distribuidos?

## Otras arquitecturas web

La arquitectura para aplicaciones distribuidas más escucha es la cliente-servidor, pero no es ni de lejos la única. Analicemos otras arquitecturas y dónde se usan.

### Peer to Peer

En este estilo está compuesta por nodos equivalentes, es decir, que tiene la misma función (aunque pueden no tener la misma información) y que se distribuyen la carga que soporta el sistema entero según las capacidades de cada uno o se proporcionan servicios entre ellos.

En esta arquitectura no hay por definición un nodo más importante que otro y si alguno de toda la ted falla puede ser sustituido por otro si tiene la información replicada.

Las redes de torrents, el blockchain y programas como Ares o LimeWire funcionaban de esta forma.

Una red peer-to-peer puede lucir así:

![Ejemplo de red peer to peer](https://res.cloudinary.com/hectorip/image/upload/c_scale,w_871/v1561266301/PNG_image-CC8B051C8851-1_r78hfc.png)

### Pipe and Filter

Este patrón es el que siguen los pipelines de datos normalmente. La información pasa por una series de "filtros" que la procesan y van dejando la información en un nuevo estado.

## Explicación de cliente-servidor
## Ventajas
## Desventajas
## Conclusión
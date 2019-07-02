---
title: "Entendiendo REST: Arquitectura cliente-servidor"
date: 2019-06-22
author: Héctor Patricio
tags:
comments: true
excerpt: "Hablemos de la arquitectura cliente-servidor y por qué es adecuada para REST."
header:
  overlay_image: 
  teaser: 
  overlay_filter: rgba(0, 0, 0, 0.5)
---

> El propósito de construir software no es crear una topología de interacciones específicas, o usar un tipo particular de componente; es crear un sistema que cumpla y exceda las necesidades de la aplicación. - Thomas Fielding

Ya hablamos de las [motivaciones detrás del estilo arquitectural REST](){:taget=blank}. Ahora empecemos con la primera de sus características o restricciones, que la empieza a definir: la arquitectura cliente-servidor.

## ¿Qué es la arquitectura cliente-servidor?

Esta arquitectura de aplicación tiene dos componentes:

- **Cliente**: Es un programa o proceso que solicita un servicio y usa la información provista para sus propios objetivos.
- **Servidor**: Programa o proceso que ofrece un conjunto de servicios y espera por peticiones para ejecutar o dar estos servicios.

La principal característica de la arquitectura cliente-servidor es lograr una _separación de responsabilidades clara_, con el costo de un poco de aumento de complejidad en el sistema en general.

Recordemos que todos los diseños o arquitecturas implican un intercambio de valor entre varias características, en este caso un poco de simplicidad por la separación de responsabilidades claras.

## Ventajas

### Separación clara de responsabilidades

El cliente y el servidor tienen funciones completamente distintas y cada uno puede cambiar por su lado sin afectar al otro, a esto le podemos llamar "evolución independiente".

El ejemplo que tenemos es el del navegador y las páginas que visitamos normalmente en internet. Mientras sigan cumpliendo con el protocolo establecido de comunicación (HTTP) van a poder seguir comunicándose y transfiriendo información, sin interferir la manera en que estén implementados sus procesos internos.

### Bajo acoplamiento


## Desventajas

### Complejidad ligeramente aumentada
### Comunicación


Pero, un momento, ¿acaso no es la única que existe para sistemas web o sistemas distribuidos?

## Otras arquitecturas web

La arquitectura para aplicaciones distribuidas más escuchada es la cliente-servidor, pero no es ni de lejos la única. Analicemos otras arquitecturas y dónde se usan.

### Peer to Peer

En este estilo está compuesta por nodos equivalentes, es decir, que tiene la misma función (aunque pueden no tener la misma información) y que se distribuyen la carga que soporta el sistema entero según las capacidades de cada uno y a veces se proporcionan servicios entre ellos. Un mismo nodo puede cambiar entre funciones o roles en la red dependiendo de la demanda.

En esta arquitectura no hay por definición un nodo más importante que otro y si alguno de toda la red falla, puede ser sustituido por otro si tiene la información replicada.

Las redes de torrents, el blockchain y programas como Ares o LimeWire funcionaban de esta forma.

Una red peer-to-peer puede lucir así:

![Ejemplo de red peer to peer](https://res.cloudinary.com/hectorip/image/upload/c_scale,w_871/v1561266301/PNG_image-CC8B051C8851-1_r78hfc.png)

Las redes peer-to-peer son una de las mejores formas de crear sistemas distribuidos resistentes y descentralizados, es decir, que no concentran la información en un sólo punto que se vuelve el más delicado e importante de todos.

### Pipe and Filter

En este patrón, la información pasa por una series de "filtros" o nodos que la procesan y van dejando la información en un nuevo estado o con nuevas propiedades y que pasan la información al siguiente nodo. Este patrón es el que siguen los pipelines de datos normalmente, en el que la información que es producida por una fuente externa es procesada a través de una serie de pasos, que pueden incluir la recolección, limpieza, almacenamiento, etc.

## Conclusión

> The architectural styles chosen for a system’s design must conform to those needs, not the other way around.


Para los propósitos de REST la arquitectura Cliente-servidor es muy adecuada. Sus beneficios superan sus desventajas para este caso de uso particular.
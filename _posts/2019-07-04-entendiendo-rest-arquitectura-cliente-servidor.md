---
title: "Entendiendo REST: Arquitectura cliente-servidor"
date: 2019-07-04
author: Héctor Patricio
tags:
comments: true
excerpt: "Hablemos de la arquitectura cliente-servidor y por qué es adecuada para REST."
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1260/v1562217908/krzysztof-kowalik-KiH2-tdGQRY-unsplash_v0vf7l.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1260/v1562217908/krzysztof-kowalik-KiH2-tdGQRY-unsplash_v0vf7l.jpg
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

Hablemos de los beneficios que trae usar la arquitectura cliente-servidor.

### Separación clara de responsabilidades

La funcionalidad del sistema se divide en dos partes (por lo menos), como el nombre lo indica en parte de dar los servicios (generalmente de datos) y la parte de atender al usuario (humanos o programa) final.

El cliente y el servidor tienen funciones completamente distintas y cada uno puede cambiar por su lado sin afectar al otro, a esto le podemos llamar "evolución independiente".

El ejemplo que tenemos es el del navegador y las páginas que visitamos normalmente en internet. Mientras sigan cumpliendo con el protocolo establecido de comunicación (HTTP) van a poder seguir comunicándose y transfiriendo información, sin interferir la manera en que estén implementados sus procesos internos.

### División de complejidad

La misma división de la que hablamos en el punto anterior permite dividir la complejidad en dos partes por lo que cada una por su lado es más fácil de entender y desarrollar que el sistema completo.

Por lo tanto se sigue el mismo principio que se usa para desarrollar software complejo en general: divide y vencerás. Esto permite que podamos dividir el trabajo limpiamente en diferentes etapas de desarrollo o entre diferentes equipos, que lo único que requieren es una interfaz de comunicación clara.

Esto no quiere decir que la complejidad _general_ se reduzca. De esto hablaremos en las desventajas.

## Desventajas

Todo en la vida viene con desventajas y otra vez: intercambios de valor entre diferentes partes de la aplicación. Analicemos algunas de estos intercambios que hacemos al aplicar la arquitectura cliente-servidor.

### Complejidad general aumentada

Cuando dividimos la aplicación y funciones completas en dos partes, aunque la complejidad de cada parte es menos que la complejidad en general, la complejidad completa aumenta porque hay que agregar elementos al sistema:

- Interfaces de comunicación entre cliente y servidor
- Mantenimiento o forma de recuperación del estado general de la aplicación
- Protocolos de comunicación de red cuando es el caso


Pero, un momento, ¿acaso no es la única que existe para sistemas web o sistemas distribuidos?

## Otras arquitecturas

La arquitectura para aplicaciones distribuidas más escuchada es la cliente-servidor, pero no es ni de lejos la única. Analicemos otras dos arquitecturas comunes y dónde se usan. Si quieres ver la lista completa que Fielding analiza puedes checar la sección 2 de [su tesis doctoral](https://www.ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf).

### Peer to Peer

En este estilo está compuesta por nodos equivalentes, es decir, que tiene la misma función (aunque pueden no tener la misma información) y que se distribuyen la carga que soporta el sistema entero según las capacidades de cada uno y a veces se proporcionan servicios entre ellos. Un mismo nodo puede cambiar entre funciones o roles en la red dependiendo de la demanda.

En esta arquitectura no hay por definición un nodo más importante que otro y si alguno de toda la red falla, puede ser sustituido por otro si tiene la información replicada.

Las redes de torrents, el blockchain y programas como Ares o LimeWire funcionaban de esta forma.

Una red peer-to-peer puede lucir así:

![Ejemplo de red peer to peer](https://res.cloudinary.com/hectorip/image/upload/c_scale,w_871/v1561266301/PNG_image-CC8B051C8851-1_r78hfc.png)

Las redes peer-to-peer son una de las mejores formas de crear sistemas distribuidos resistentes y descentralizados, es decir, que no concentran la información en un sólo punto que se vuelve el más delicado e importante de todos.

### Pipe and Filter

En este patrón, la información pasa por una series de "filtros" o nodos que la procesan y van dejando la información en un nuevo estado o con nuevas propiedades y que pasan la información al siguiente nodo. Este patrón es el que siguen los pipelines de datos normalmente, en el que la información que es producida por una fuente externa es procesada a través de una serie de pasos, que pueden incluir la recolección, limpieza, almacenamiento, etc.

![Ilustración de pipe and filter](https://res.cloudinary.com/hectorip/image/upload/c_scale,w_800/v1562217820/PNG_image-C00985E33227-1_mevaqa.png)


## Conclusión

> The architectural styles chosen for a system’s design must conform to those needs, not the other way around.


Para los propósitos de REST la arquitectura Cliente-servidor es muy adecuada. Sus beneficios superan sus desventajas para este caso de uso particular.
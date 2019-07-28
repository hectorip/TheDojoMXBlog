---
title: "Entendiendo REST: conexión sin estado"
date: 2019-07-05
author: Héctor Patricio
tags: REST stateless thomas-fielding
comments: true
excerpt: "¿Cómo mantener la información entre conexiones en un sistema REST?"
header:
  overlay_image: 
  teaser: 
  overlay_filter: rgba(0, 0, 0, 0.5)
---

Hemos venido hablando de las características que componen a un sistema REST. En el último artículo [hablamos de la arquitectura cliente-servidor](/2019/07/04/entendiendo-rest-arquitectura-cliente-servidor.html). Ahora pasemos a la siguiente caractarística-limitante que Thomas Fielding establece para los sistemas REST: **conexión sin estado**.

## ¿A qué nos referimos con "el estado"?

El estado de una aplicación son todos los datos que usa para operar en un momento determinado.
Como ejemplo podemos pensar en una aplicación de ventas en línea. El estado de esta aplicación, para un usuario específico son sus datos de identificación, su carrito de compras y los productos que ha estado viendo o que ha visto.

## Conexión sin estado

En una conexión sin estado consideramos 1) Que la conexión no es persistente, es decir, no se mantiene un canal de comunicación abierto que pueda mantener en memoria la información de los procesos actuales. 2) Que no podemos (ni debemos) asumir que el servidor mantendrá los datos del cliente automáticamente por medio de reconocer al cliente.


## Ventajas de mantener el servidor sin estado

1. Replicación de servidores. Permite replicar los servidores más fácilmente, al no tener que mantener el estado o conexiones persistentes una conexión sin estado puede permitir que la petición sea atendida por cualquier servidor que tenga el mismo código que las peticiones anteriores, ya que toda la información necesaria para atender esas peticiones estará incluida.
2. Escalabilidad. Esto es una consecuencia inmediata de la ventaja anterior: poder replicar los servidores permite distribuir la carga entre muchas computadoras y aplicar técnicas de balanceo para poder atender a muchos más clientes de lo que se podría en un sistema que requira mantener estados.
2. Las conexiones persistentes son innecesarias.
3. Información cacheable?
4.


## Desventajas

## Conexiones con estado

## Conclusión
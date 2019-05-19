---
title: "Diseño de una API RESTful"
date: 2019-05-17
author: Héctor Patricio
tags:
categories: 
comments: true
excerpt: "Escribe aquí un buen resumen de tu artículo"
header:
  overlay_image: #image
---

En el [artículo anterior](2019/05/06/diseno-y-desarrollo-de-una-api-desde-cero.html) hablamos un poco de lo que es una API RESTful. En este artículo la definiremos a cabalidad, con ejemplos y veremos las ventajas y desventajas desde el punto de vista de desarrollo y arquitectura.

Antes de empezar con lo nuesto, hablemos que lo que NO es una API RESTful.

## Esto no es RESTful

Actualmente, muchos desarrolladores (yo me contaba entre ellos), llaman API REST a cualquier Servicio Web que corra sobre HTTP, sirva recursos (objetos o elementos que representan un objeto) o cosas parecidas y use JSON como meido de comunicaión.
De estas cosas, sólo la parte de servir recursos (en realidad _representaciones_ de recursos) tiene que ver con una API RESTful. El estilo Arquitectural RESTful no forza el uso de HTTP y mucho menos de JSON.

La mayoría de las API's que nos proveen de un servicio no son completamente RESTful, algunas se acercan pero alguna de sus características rompe con el estilo arquitectural.
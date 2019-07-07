---
title: "Entendiendo REST: conexión sin estado"
date: 2019-07-05
author: Héctor Patricio
tags: REST 
comments: true
excerpt: "¿Cómo mantener la información entre conexiones en un sistema REST?"
header:
  overlay_image: #image
  teaser: #image
  overlay_filter: rgba(0, 0, 0, 0.5)
---

Hemos venido hablando de las características que componen a un sistema REST. En el último artículo [hablamos de la arquitectura cliente-servidor](/2019/07/04/entendiendo-rest-arquitectura-cliente-servidor.html). Ahora pasemos a la siguiente caractarística-limitante que Thomas Fielding establece para los sistemas REST: **conexión sin estado**.

## ¿A qué nos referimos con 'el estado'?
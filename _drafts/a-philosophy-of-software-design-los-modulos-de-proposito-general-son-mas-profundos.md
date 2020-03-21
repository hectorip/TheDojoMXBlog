---
title: "A Philosophy of Software Design: Los módulos de propósito general son más profundos"
date: 2020-03-18
author: Héctor Patricio
tags: PoSD módulos generalización
comments: true
excerpt: "Crear módulos o clases demasiado específicas puede llevar a tu código a ser difícil de mantener, veamos algunas maneras de encontrar el equilibrio"
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1400/v1584726013/D750CDED-7745-4A56-8B3D-5CD33D2893E6_vqdgzb.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1400/v1584726013/D750CDED-7745-4A56-8B3D-5CD33D2893E6_vqdgzb.jpg
  overlay_filer: rgba(0, 0, 0, 0.6)
---

Una burla común hacia los programadores es que todo lo queremos hacer demasiado general, nos piden algo y pensamos en todos los casos en los que podría ser usado en el universo y queremos construir eso.

Hay muchos consejos en contra de escribir código que abarque muchos casos. En este artículo vamos a hablar de las ventajas y desventajas de módulos de propósito general. Además hablaremos de algo muy importante: el equilibrio.

## Grados de especificidad

Puedes pensar en la especialización de un módulo       
Un módulo específico está dedicado a cumplir una sola función en el sistema y _su uso está restringido sólo a esa función_.

El caso más extremo del código específico es el que llamamos "hardcoding". Es tan específico que sólamen

## ¿Por qué hacer módulos de propósito general?

El principal motivo que [A Philosophy of Software Design](https://amzn.to/3ba4MEj) recomienda es porque los módulos de propósito general [son más profundos](https://blog.thedojo.mx/2020/03/02/a-philosophy-of-software-design-los-modulos-deben-ser-profundos.html#dise%C3%B1o-de-m%C3%B3dulos) es decir, encierran más funcionalidad con una interfaz más pequeña.

Hacerlo contribuye a que tu código esconda más información y por lo tanto su uso sea más simple.

## Cuándo hacer módulos específicos



## Conclusión

Crear módulos de "no tan específicos" puede ayudarte a:

1. Ocultar mejor la información
2. Crear interfaces más concisas
3. Reutilizar mejor el código

Tienes que buscar el equilibrio entre crear un módulo tan específico que sólo uses una vez contra un módulo que cubra todos los casos del mundo. El equilibrio está en un módulo que no sea difícil de utilizar para tu problema a la mano pero que puede ser (o este siendo) utilizado en varios lugares si es el caso.

En el próximo artículo hablaremos de los sistemas en capas y cómo aprovechar sus particularidades para crear diseños que dominen la complejidad.
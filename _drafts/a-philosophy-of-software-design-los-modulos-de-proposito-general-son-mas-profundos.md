---
title: "A Philosophy of Software Design: Los módulos de propósito general son más profundos"
date: 2020-03-21
author: Héctor Patricio
tags: PoSD módulos generalización module class
comments: true
excerpt: "Crear módulos o clases demasiado específicas puede llevar a tu código a ser difícil de mantener, veamos algunas maneras de encontrar el equilibrio"
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1400/v1584726013/D750CDED-7745-4A56-8B3D-5CD33D2893E6_vqdgzb.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1400/v1584726013/D750CDED-7745-4A56-8B3D-5CD33D2893E6_vqdgzb.jpg
  overlay_filer: rgba(0, 0, 0, 0.6)
---

Una burla común hacia los programadores es que todo lo queremos hacer _demasiado general_. Nos piden algo y pensamos en todos los casos en los que podría ser usado en el multiverso e intentamos construir eso.

Hay muchos consejos **en contra** de escribir código que abarque muchos casos. En este artículo vamos a hablar de las ventajas y desventajas de módulos de **propósito general**. Además hablaremos de algo muy importante: el equilibrio.

## Especificidad de un módulo

Puedes pensar en la especialización de un módulo (o del código en general) como en continuo que va desde lo más general (las bibliotecas estándar) hasta código que sólo sirve para un uso muy acotado.

![Gráfica del continuo de especificidad]()

Un módulo específico está dedicado a cumplir una sola función en el sistema y _su uso está restringido sólo a esa función_. Si los pensáramos como conectores para un dispositivo como un celular podrías decir que es la conexión especial que Nokia o Sony Ericsson se inventaron en su tiempo para cargar.

Un módulo de propósito general se puede usar para varios casos con _poca modificación_, o creando un módulo específico a partir de él. En el mismo ejemplo de los dispositivos electrónicos puede compararse al estándar USB que sirve para múltiples cosas y puede ser usado en muchos aparatos diferentes.

El caso más extremo del código específico es el que llamamos _"hardcoding"_. Es tan específico que sirve sólo para una instancia muy pequeña y _no es fácil de modificar en producción_. Se entiende como _hardcoding_ a poner directamente en el código un valor fijo que pudiera variar en el futuro: configuración de IP's, bases de datos, nombres de usuario, etc. Y es uno de los casos extremos de [programación táctica](https://blog.thedojo.mx/2020/02/11/a-philosophy-of-software-design-programacion-tactica-vs-estrategica.html#desarrollo-t%C3%A1ctico). Por lo tanto, y esto todos lo sabemos, es una **muy mala  práctica** para crear código mantenible e incluso para la practicidad en el desarrollo.

El siguiente nivel de especificidad y con el que casi todos nos quedamos contentos es cuando creamos un módulo (una clase, por ejemplo), para una función específica de nuestro sistema y que _sólo puede usarse ahí_.

Usemos como ejemplo para entender los niveles de especificidad una aplicación para clasificar libros.

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

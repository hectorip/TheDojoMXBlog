---
title: "¿Qué es DevOps?"
date: 2019-12-31
author: Héctor Patricio
tags:
categories: 
comments: true
excerpt: ""
header:
  overlay_image: 
  teaser: #image
  overlay_filer: rgba(0, 0, 0, 0.5)
---

**DevOps** es un término de recientemente creación (2013) que representa un cultura de trabajo enfocada en resolver los problemas que han sido persistentes en la entrega y servicio en el área de productos tecnológicos.

En este artículo platicaremos qué significa y sus fundamentos.

Adelanto: DevOps no es un rol, una palabra mágica y mucho menos automatización de servidores.

## ¿Por qué importa?

> En las eras económicas anteriores, los negocios creaban valor moviendo átomos. Ahora crean valor moviendo bits. - Jeffrey Snover

Ahora todas las empresas son empresas de tecnología. Las que no aprovechan la tecnología ya están siendo superadas por las que sí lo hacen. Y las que lo hacen mal en su momento serán superadas por las que usan mejor la tecnología.

> Cada industria y compañía que no traiga el software al corazón de su negocio será cambiada radicalmente sin previo aviso. - Jeffrey Immelt

Así que es importante que las empresas aprendan a manejar lo mejor posible la tecnología y a crear valor o aumentar el valor que producen mediante ella.

## Los problemas

Si has trabajado en desarrollo de software, infraestructura o en el área de IT de alguna empresa tal vez no necesito contarte esto. Todo lo relacionado con productos digitales está plagado de proyectos no cumplidos en tiempo, nunca terminados, pasados de presupuesto, atención a clientes internos extremadamente deficiente, etc.

No conforme con eso hay millones de historias de terror de cómo los negocios no se interesan en lo mínimo por mejorar estas áreas, sólo exigiendo cada vez más cosas y poniendo fechas irrazonables.

Otras historias cuentan los actos heróicos que las personas que trabajamos en estas áreas hemos tenido que hacer para cumplir con los compromisos adquiridos: trabajar toda la noche por varios días seguidos, cambios de último momentos, largas horas en despliegues y re-establecimiento de servicios, etc. O se descubre que el sistema no cumple con los requerimientos legales de protección información y ahora hay que trabajar horas extras para cumplirlo.

Y por último la vista del lado de la operación del negocio: cada que se va a poner en producción un cambio, un nuevo producto o se va a actualizar algo todos temen que algo catastrófico pase con cierta razón. Ha pasado que por culpa de estos cambios los sistemas que soportan la operación diaria se caen por horas haciendo perder al negocio clientes, dinero y reputación.

Todos estos problemas son lo que DevOps ataca con 3 principios o "tres caminos". Pero para habilitar esto antes se necesita algo de la organización.

## Todos los involucrados trabajan para lo mismo

Sobre todo en empresas grandes, donde es más común dividir en departamentos debido a la gran cantidad de trabajo disponible, es normal que **cada departamento busque sólo sus propios intereses** y cumplir con sus métricas de desempeño sin poner en primer lugar lo más importante: la producción de valor para el negocio en general.

Así que la primera precondición para que se pueda alcanzar verdadera productividad es que los involucrados comprendan que todos trabajan con el fin de crear cosas de valor para que el negocio siga funcionando y pueda hacerlo cada vez mejor. Esto implica eliminar la burocracia, las guerras entre departamentos y la reducción de trabajo que sólo se hace por demostrar que se tiene algo que hacer como tristemente ha estado marcado por este estigma el departamento de Seguridad de la Información o su equivalente.

Si la actividad qu se está haciendo no contribuye de alguna forma a crear valor para el negocio debería ser eliminada.

Esta condición por sí misma es difícil de cumplir y sin ella no es posible lograr las demás. ¿Quiénes son los encargados poner las condiciones para que se cumpla? La dirección. La dirección de la empresa tiene la responsabilidad de elegir personas razonables, buenas en sus campos y dispuestas a cooperar para que la empresa o el proyecto progresen más allá de su ego. Repito, **sin esto lo demás es imposible o inútil**.

Una vez cumplida la precondición de cooperación con personas dispuestas y hábiles a su nivel podemos hablar de los tres caminos.

## El primer camino: Flujo

![Primer camino de DevOps](https://res.cloudinary.com/hectorip/image/upload/c_scale,w_800/v1579042628/4E94ED23-0268-4F59-A101-1CF009540E01_pssljp.jpg){:align-center}

El primer principio de DevOps establece que debe haber un flujo constante de valor en el área de tecnología de información o de sistemas, como lo quieras llamar. Algo de valor es todo aquello que permite al negocio seguir operando o incrementar los beneficios que obtiene de las operaciones.

El objetivo principal es **minimizar el tiempo** que tarda una característica/producto/servicio en entregarse desde que solicita hasta que empieza a cumplir con su función.

Debido a que el desarrollo de software es una actividad poco predecible, DevOps se enfoca en la parte de la cadena de entrega de valor que va desde que el área de desarrollo termina algo hasta que es puesto en manos de los usuarios finales. Pero no le interesa sólo eso, ya que las personas encargadas del desarrollo deben seguir ciertas prácticas para facilitar el resto del camino.

Acelerar esta entrega beneficia en gran manera a la forma en que se desarrolla software de calidad.

Si estás en una empresa pequeña o en una _startup_ puede que seas tú mismo el que desarrolle y tenga que mantener los programas en operación (producción). Así que reducir la fricción entre estas dos actividades te beneficiará aún más.

¿Qué prácticas permiten lograrlo?

- **Reducir el trabajo en progreso.** Mientras menos actividades sin terminar existan, más difícil es administrarlas y notar todo el trabajo pendiente. Tener pocas actividades en progreso permite calcular mejor cuánto tardará en terminarse un nuevo requerimiento y atender los errores más rápidamente.

Algo que notar de las prácticas de DevOps es que muchas están extraídas de los movimientos de _Lean Manufacturing_.

## El segundo camino: Retroalimentación rápida

![Segundo camino de DevOps](https://res.cloudinary.com/hectorip/image/upload/c_scale,w_800/v1579042628/F68161CA-BF97-4E71-B78B-9310C00CD254_sjiled.jpg){:align-center}

El segundo camino por el que el valor fluye en las organizaciones que implementan DevOps es de regreso: Debe existir un flujo de información desde los sistemas en producción hacia los equipos que están desarrollando los productos y los demás equipos relacionados con esta tarea.


## El tercer camino: Cultura de aprendizaje y experimentación

Después de implementar el camino hacia el cliente y de regreso, DevOps establece que se tiene que crear un cultura de aprendizaje que permita mediante ciclos de retroalimentación mejorar la forma general en la que se trabaja.

La siguiente imagen completa los tres caminos de DevOps:


![Los tres caminos de devops](https://res.cloudinary.com/hectorip/image/upload/c_scale,w_800/v1579042629/0548901A-3BF6-49BF-8556-B0B12D45F0A9_zgljnk.jpg){:align-center}

La empresa debe asegurarse de que los equipos de trabajo están mejorando constantemente mediante el aprendizaje continuo.

Esto puede lograrse mediante varias prácticas:

- Experimentación, por ejemplo pruebas A/B
- Introducción de fallas intencionalmente (_chaos engineering_)
- Mediciones cada vez más precisas mediante software especializado
- Agendar tiempo para actividades dedicadas a mejorar el equipo como _Improvement Katas_

Este paso depende de que los dos anteriores se hayan logrado, ya que

## Conclusión

[http://bit.ly/36t59HK](DevOps no es un rol en la empresa) por Domingo Suárez
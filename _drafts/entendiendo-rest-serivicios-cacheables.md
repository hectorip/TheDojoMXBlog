---
title: "Entendiendo REST: Serivicios cacheables"
date: 2019-08-04
author: Héctor Patricio
tags:
categories: 
comments: true
excerpt: "Los servicios REST deben ser cacheables, aprendamos lo que esto significa y cómo podemos lograrlo."
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1200/v1570679826/laura-ockel-nIEHqGSymRU-unsplash_gsspla.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1200/v1570679826/laura-ockel-nIEHqGSymRU-unsplash_gsspla.jpg
  overlay_filter: rgba(0, 0, 0, 0.6)
---

La tercera característica que Thomas R. Fielding establece para los sistemas **REST** es la capacidad de que su información sea cacheable. Veamos lo que esto significa. Empecemos por definir el cahché.

## Qué es _el caché_

Originalmente el caché se refiere a un tipo especial de memoria _muy rápida_ en los procesadores, que guarda temporalmente información que tiene gran probabilidad de volver a ser utilizada _dentro de poco tiempo_. Al evitar que el procesador volviera a consultar la RAM (muy lenta en comparación con la memoria caché), las operaciones se realizan a mucha mayor velocidad.

La memoria caché de los procesadores tiene una gran desventaja: **es muy muy pequeña**. Esto presenta retos:

- ¿Qué guardo aquí para maximizar la eficacia de este espacio de almacenamiento?
- ¿Cómo decido cuándo borrar o sobre-escribir la información que tengo aquí?
- ¿Qué pasa si la información original cambia mientras estoy ocupando los datos guardados en la memoria caché? A final de cuentas esta información es una copia.

Hablaremos más adelante de estas preguntas en nuestro propio contexto, pero hay técnicas para poder contestar con cierta eficacia estas preguntas.

Así que puedes pensar en el caché como en una memoria que es más rápida que la que normalmente se utiliza con el objetivo de hacer un sistema más rápido y a veces más eficiente.

## Caché en los sistemas REST

Esta característica se basa en las dos de las que ya hablamos: [servicios sin estado](/2019/07/04/entendiendo-rest-arquitectura-cliente-servidor) y [arquitectura cliente-servidor](/). Lo que se define como "cacheabilidad" en los sistemas REST es la capacidad de estos sistemas para etiquetar de alguna forma las respuestas para que sistemas intermedios (muchas veces transparentes para los desarrolladores de las funcionalidades y para los usuarios).

## Ventajas del caché

El caché se establece como una de las características de REST porque proporciona ventajas para el uso y la escalabilidad de los sistemas.

### Aumenta la percepción de velocidad

Al guardar las respuestas que es más probable que vuelvan a salir, un sistema REST puede contestar una gran cantidad de sus peticiones a la velocidad que el caché lo permita, es decir, muy rápido generalmente.



### Consumo de recursos reducido



### Sistemas más fáciles de escalar

## Retos de cachear

Vida del caché.
Frescura del caché.
Memoria total

## Conclusión

El caché es una parte de los sistemas REST que les permite funcionar mejor cuando tenemos bastante carga. Mantenerlo funcionando bien es un reto, pero los sistemas que quieren ser escalables y resistentes deben implementar alguna forma de cachear.

En el siguiente artículo veremos la cuarta restricción de los sistemas REST: la interfaz uniforme, la más amplia de las restricciones, pero una de las más útiles.
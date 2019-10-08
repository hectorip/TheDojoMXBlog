---
title: "Entendiendo REST: Serivicios cacheables"
date: 2019-08-04
author: Héctor Patricio
tags:
categories: 
comments: true
excerpt: "Los servicios REST deben ser cacheables, aprendamos lo que esto significa y cómo podemos lograrlo."
header:
  overlay_image: # cache
  teaser: 
  overlay_filter: rgba(0, 0, 0, 0.5)
---

La tercera característica de los sistemas **REST** es la capacidad de que su información es cacheable. Veamos lo que esto significa.

## Qué es _el caché_

Originalmente el caché estaba relacionado con un tipo especial de memoria _muy rápida_ en los procesadores, que guarda temporalmente información que tiene gran probabilidad de volver a ser utilizada _dentro de poco tiempo_. Al evitar que el procesador volviera a consultar la RAM (lenta en comparación con la memoria caché), las operaciones se realizan a mucha mayor velocidad.

La memoria caché de los procesadores tiene una gran desventaja: es muy muy pequeña. Esto presenta retos:
- ¿Qué guardo aquí para maximizar la eficacia de este espacio de almacenamiento?
- ¿Cómo decido cuándo borrar o sobre-escribir la información que tengo aquí?
- ¿Qué pasa si la información original cambia mientras estoy ocupando los datos guardados en la memoria caché?

Hablaremos más adelante de estas preguntas en nuestro propio contexto.

## Ventajas del caché

Permite responder más rápidamente.
Menos procesamiento.
Sistemas más escalables y resistentes.

## Retos de cachear

Vida del caché.
Frescura del caché.
Memoria total

## Conclusión

El caché es una parte de los sistemas REST que les permite funcionar mejor cuando tenemos bastante carga. Mantenerlo funcionando bien es un reto, pero los sistemas que quieren ser escalables y resistentes.

En el siguiente artículo veremos la cuarta restricción de los sistemas REST: la interfaz uniforme, la más amplia de las restricciones, pero una de las más útiles.

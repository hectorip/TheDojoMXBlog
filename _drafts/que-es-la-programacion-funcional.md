---
title: "¿Qué es la programación funcional?"
date: 2019-03-24
author: Héctor Patricio
tags:
categories: 
comments: true
excerpt: "¿Por qué se ha escuchado tanto de la programación funcional recientemente? En este artículo la explicamos de manera concisa"
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1280/v1553485527/john-moeses-bauan-690280-unsplash_atpm3w.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1280/v1553485527/john-moeses-bauan-690280-unsplash_atpm3w.jpg
---

En los últimos años ha estado cobrando relevancia (de nuevo) la programación funcional. ¿Qué diferencias tiene con los estilos más usados?
En este artículo hablaremos de sus dos caracterísitcas más distintivas y el tipo de programas que se pueden crear con ella.

## Definición

Se puede definir la programación funcional como sigue:

> Estilo de programación en el que se usan principalmente **funciones puras** y valores **inmutables**.

Eso es todo. Ahora tenemos que definir dos términos más.

## Funciones puras

Una función pura se refiere a una que no hace referencia a nada fuera de ella para trabajar.
Los ejemplos esta vez los pondremos en JavaScript, ya que es el lenguaje más común en el que la programación funcional está teniendo auge.

```javascript
tasaIVA = 0.16;

/*
Función impura
*/
function calcularIVA(subtotal) {
  return subtotal * tasaIVA;
}

/* Esta función es pura */
function calcularIVAPura(subtotal, tasa) {
  return subtotal * tasa;
}
```

La primera función, `calcularIVA`, toma una variable que está fuera de ella para calcular su resultado. Esto es malo por varias razones, entre ellas:
* Si vemos la función por separado, tener uno o varios valores que no sabemos de dónde vienen hace el código poco mantenible y entendible.
* Si alguna parte del código modifica el valor sin que no nos demos cuenta, nuestros cálculos serán erróneos

En cambio, la función `calcularIVAPura` es una función que no depende de valores que no sabemos de dónde vienen para trabajar. Tiene la característica de que siempre que la llamemos con los mismos argumentos, va a devolver el mismo valor. Tampoco modifica nada en el exterior.

Las funciones puras proporcionan las siguientes ventajas:

* **Transparencia referencial**. Dentro de un contexto en el que se use la función, sabiendo que la función siempre que sea llamada con ciertos parámetros devolverá lo mismo, podemos sustituir la función con su valor directamente. Esto hace a las funciones puras *cacheables* (a través de técnicas como la programación dinámica y la [memoización](http://nereida.deioc.ull.es/~lpp/perlexamples/node170.html)) y *predecibles*. Pongamos un ejemplo más claro:

```javascript
function factorial(n) {
  if(n <= 1){
    return 1
  } 
  return n * factorial(n-1)
}

function ()

```

<!-- * **Predecibles** -->
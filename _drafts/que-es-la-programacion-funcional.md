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

En los últimos años ha estado cobrando relevancia (de nuevo) la **programación funcional**. ¿Qué diferencias tiene con los estilos más usados?
En este artículo hablaremos de sus dos caracterísitcas más distintivas y el tipo de programas que se pueden crear con ella.

## Definición

Se puede definir la programación funcional así:

> Estilo de programación en el que se usan principalmente **funciones puras** y valores **inmutables**.

Eso es todo, todas las demás cosas que lees cuando se menciona la programación funcional se derivan de estas dos características. Ahora tenemos que definir estas dos características y ver como nos proporcionan amplias capacidades para crear programas altamente legibles, rápidos y que pueden procesar grandes cantidades de datos.

## Funciones puras

Una función pura es una que no hace referencia a nada fuera de ella para trabajar. En los lenguajes que pueden usar el estilo funcional, todo se puede tratar como si fuera una función.
Los ejemplos esta vez los pondremos en JavaScript, ya que es el lenguaje más común en el que la programación funcional está teniendo auge.

```javascript
tasaIVA = 0.16;

/*
Función impura
*/
function calcularIVA(subtotal) {
  return subtotal * tasaIVA; // tasaIVA está definido fuera del ámbito de esta función
}

/* Esta función es pura */
function calcularIVAPura(subtotal, tasa) {
  return subtotal * tasa;
}
```

La primera función, `calcularIVA`, toma una variable que está fuera de ella para calcular su resultado. Esto es poco recomendable por varias razones, entre ellas:
* Si vemos la función por separado, tener uno o varios valores que no sabemos de dónde vienen hace el código poco mantenible y entendible.
* Si alguna parte del código modifica el valor sin que nos demos cuenta, nuestros cálculos serán erróneos.
* Modificar los datos que están afuera y saber exactamente a todo lo que vamos a afectar cuando el programa crezca es muy difícil.
* Los más importante: **las funciones no dependen del contexto de ejecución, sólo de sus parámetros**.

En cambio, la función `calcularIVAPura` es una función que no depende de valores que no sabemos de dónde vienen para trabajar. Tiene la característica de que siempre que la llamemos con los mismos argumentos, va a devolver el mismo valor. Tampoco modifica nada en el exterior. Cuando modifiquemos un valor sabemos exactamente a qué vamos a afectar. 

Veamos ahora una a una de las ventajas que proporciona usar funciones puras.

### Transparencia referencial

Dentro de un contexto en el que se use la función, sabiendo que la función siempre que sea llamada con ciertos parámetros devolverá lo mismo, *podemos sustituir la función con su valor directamente*. Esto nos permite crear programas más legibles inicialmente.

La tranparencia referencial hace que las funciones sean *cacheables* (a través de técnicas como la programación dinámica y la [memoización](http://nereida.deioc.ull.es/~lpp/perlexamples/node170.html)) y *predecibles*: al saber que una función llamada con los mismos parámetros podemos almacenar ese valor en vez de volver a llamar la función y usarlo directamente. Si la función es costosa en tiempo o procesamiento, el cachearla hará nuestro programa más eficiente.

<!-- ¿Qué ventajas da esto, podrías preguntarte? Pensemos en algunas cosas que propociona la transparencia referencial: -->

### Evaluación diferida (*lazy evaluation*)

Para los lenguajes funcionales más puros, todo se puede tratar como una función. Al saber que las funciones no dependen del contexto para funcionar correctamente, puedo evaluarlas ahora mismo o más tarde. Para evitar procesamiento innecesario, los lenguajes funcionales difieren la evalución de las funciones y valores hasta que realmente se requiera el valor para alguna otra operación. Mientras el valor está sólamente definido, sin haber sido procesado. La evaluación diferida es muy conveniente sobre todo al trabajar con colecciones de datos grandes u operaciones gigantes. Algunas de las ventajas de la evaluación diferida son las siguientes:

* **Ahorro en tiempo de procesamiento**. Si defino un valor que es una función que corre sobre una colección de un millón de elementos, no tendré que esperar al procesamiento inicial porque no lo hará hasta que realmente ocupe los valores. Si por alguna razón no se ocupa ese valor más adelante en el programa, ese procesamiento ya nos lo ahorramos definitivamente.
* **Ahorro en memoria**. Cuando definimos colecciones muy grandes, los lenguajes con evaluación diferida no reservarán la memoria que van a ocupar inmediatamente, sino hasta que hagamos referencia a este valor para su procesamiento. De igual manera, si nunca se ocupó este valor o se canceló en algún punto del programa, nos ahorramos esa memoria.
* **Colecciones diferidas**. Algunos lenguajes de programación incluyen colecciones que nunca cargan en memoria todos lo valores que
van necisitar nunca, sino que los van generando uno a uno. Esto permite crear colecciones **infinitas** conceptualmente, o procesar conjuntos de datos muy muy grandes sin staurar la memoria.


### Concurrencia

Lo repetimos: al no depender del contexto de de evaluación sino únicamente de sus valores de entrada, las funciones pueden ser corridas cuando sea y *donde sea*. Esto permite que las funciones puedan ser ejecutadas en un proceso concurrentes. Si el lenguaje de programción lo permite, estos procesos concurrentes se pueden ejecutar *paralelamente*.

Una aplicación de esto es el patrón [MapReduce](https://research.google.com/archive/mapreduce-osdi04-slides/index-auto-0002.html) que Google propuso para proceamiento de grandes cantidades de datos, y que es la base de [Hadoop](https://hadoop.apache.org/).

Por último, debemos notar que la concurrencia y el paralelismo se llevan bien, pero no son lo mismo. Para aclararlo te recomendamos la [siguiente plática de Rob Pike](https://blog.golang.org/concurrency-is-not-parallelism), uno de los creadores de el lenguaje Go (que no es funcional). Resumen: concurrencia es la composición de diferentes procesos independientes, mientras el paralelismo es la ejecución *simultánea* de estos procesos.

Como puedes ver, la programación funcional se posiciona como una muy buena opción para tratamiento y procesamiento de GRANDES cantidades de datos, y sus patrones han inspirado arquitecturas de procesamiento famosas.

### 






```javascript

```


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
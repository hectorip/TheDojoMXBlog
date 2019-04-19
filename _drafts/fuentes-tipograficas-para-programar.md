---
title: "Fuentes tipográficas para programar"
date: 2019-04-18
author: Héctor Patricio
tags: fuente editor ide
categories: 
comments: true
excerpt: "Las mejores fuentes para tu editor de código."
header:
  overlay_image: #image
---

Este post es una actualización [de otro](https://medium.com/@HectorIP/fuentes-tipogr%C3%A1ficas-para-programadores-7d93c55f1223) que hice hace como dos años.


# Fuentes tipográficas para programadores

Fuentes tipográficas para programadores

La mayoría de los desarrolladores de software pasa más de 4 horas usando su computadora para producir nuevas creaciones. Por eso, personalizar el entorno de programación se ha convertido en uno de los temas más relevantes para los desarrolladores de software, ya que a parte de expresar nuestros gustos, nos permite ser más productivos y estar más contentos en general con el trabajo día a día. No dudo que el lugar en el que más pasamos tiempo los desarrolladores sea el editor de texto o IDE, y, por lo tanto, aprender a personalizarlo es bastante importante. Uno de los aspectos más importantes del editor de texto es la fuente tipográfica.

Algo bueno de los últimos tiempos es la gran cantidad de desarrolladores que han surgido y esto incentiva la creación de más valores adaptados a nuestras necesidades, creados por nosotros mismos o por las industrias, y la tipografía ha sido un campo prolífico.

En éste artículo presentaré las fuentes que me parecen más interesantes diseñadas para programar, además de otras que aunque no fueron diseñadas para los programadores exclusivamente, hacen un gran trabajo. Aunque parezca un tema superfluo, tener un entorno adaptado a nuestros gustos, tanto estética como funcionalmente, es increíblemente efectivo para ser más productivos. Pero antes de empezar unas notas acerca de la tipografía.

Las fuentes usadas usadas en entornos cotidianos, como este post, en los procesadores de texto, en la mayoría de los textos impresos, libros y revistas son fuentes *espaciadas proporcionalmente*. Eso quiere decir que las letras ocupan espacio horizontal proporcional a lo anchas que son, así la **i** y la **m** ocupan diferente espacio horizontal:
> *iii*
> *mmm*

Esto facilita la lectura o el escaneo de **palabras enteras**, por lo que nos permite leer más fluidamente. Sin embargo, tiene algunas desventajas, como que los signos de puntuación, las letras delgadas y otros símbolos son fáciles de pasar por alto. Algo que no conviene en la programación.

Por la razón anterior, y [otras mencionadas en esta pregunta de Stack Overflow](http://stackoverflow.com/questions/218623/why-use-monospace-fonts-in-your-ide), los programadores estamos acostumbrados a usar fuentes *monoespaciadas*. En este tipo de fuentes las letras ocupan un espacio fijo sin importar el ancho de la letra. Así se puede crear una “cuadrícula” de letras. Veamos otra vez el ejemplo de las letras **i** y **m**:

    iii

    mmm

¿Cómo ayuda esto a los programadores? Aquí un ejemplo:
> !i

    !i

¿En qué tipo de fuente es más legible la expresión anterior? Al dar un espaciado fijo a cada letra podemos distinguir mejor los dos caracteres que existen. Y el tipo de expresiones como la anterior son bastante usadas por los programadores.

Después de entender esto sabemos porque muchas de las fuentes usadas para programar llevan en su nombre “Mono”, quiere decir que es una fuente monoespaciada. Ahora sólo un detalle más acerca de algunas fuentes, las ligaduras.

## Ligaduras

Las ligaduras en las fuentes tipográficas suceden cuando el set de caracteres se ha diseñado para que algunos conjuntos especiales de dos o tres caracteres puedan ser representados con un solo trazo o glifo. Lo normal era en letras como la **f** y la **i**, para que el espacio no quedara desproporcionado. Puedes leer más a detalle sobre las ligaduras tradicionales en este artículo: [Ligaduras](http://www.tiposconcaracter.es/ligaduras/). Aquí hay unos ejemplos de las ligaduras tradicionales:

![](https://cdn-images-1.medium.com/max/2000/0*kZ5QtY4t8GMhrtLl.jpg)

Ahora bien, las ligaduras se pueden usar para mostrar caracteres especiales más legibles y entendibles como en el caso de los conjuntos de caracteres: =>, !=, ==. Varias fuentes han aprovechado las ligaduras para poder llevar esto a la realidad. Lo triste de esto es que no todos los editores de texto, IDE’s y terminales los soportan. Algo que debe quedar claro que sólo cambia la *representación* del texto, no los caracteres realmente escritos, por lo que no produce ningún problema con el código fuente.

Ahora sí hablemos de algunas de las fuentes bonitas que podemos usar. Lo que debe quedar claro a partir de ahora es que es cuestión de puras preferencias.

### Fira Code

![](https://cdn-images-1.medium.com/max/2000/0*_wmY1HhArgNtf--1.jpg)

Una fuente con ligaduras diseñada exclusivamente para programadores. Open source y gratuita, la pueden encontrar en su [repositorio de Github](https://github.com/tonsky/FiraCode). Es derivada de Fira Mono y añade las ligaduras. Aunque si usan Sublime Text (como yo), no notaran diferencia. Pero podemos votar para que añadan soporte para ligaduras [aquí](http://sublimetext.userecho.com/topics/4719-does-sublimetext-support-programming-ligatures-fontlike-fira-code/).

Aquí un ejemplo de cómo cambian los caracteres en ligadura, extraído del repo de Github:

![](https://cdn-images-1.medium.com/max/2160/0*8Ud6Ss4VPLcR2nKi.png)

Si le quieren dar una oportunidad la pueden probar con [Atom](https://atom.io/).

### Monoid

Fuente monoespaciada semicondensada, también con ligaduras. Esta fuente al ser más condensada que Fira Code, permite tener más texto (código) en la pantalla, sin perder demasiada legibilidad. En [Medium](https://medium.com/larsenwork-andreas-larsen/designing-a-coding-font-b10cabd594fc#.chvb73c3c) explica las decisiones de diseño que tomó a través de varios artículos.

![](https://cdn-images-1.medium.com/max/2000/0*judcRlccKzjXz-8F.png)

### Hasklig

Fuente diseñada por y para programadores de Haskell (aunque no limitada para ellos), debido al extenso uso que hace de los símbolos compuestos como =>, ==, >-, -<<, ::, el creador decidió hacer un fork de la fuente Source Code Pro y añadirle ligaduras. Se puede descargar en su [repositorio de Github](https://github.com/i-tu/Hasklig). 
 Aquí un ejemplo de cómo luce:

![](https://cdn-images-1.medium.com/max/2000/0*J4JomQCofwrPbqAV.png)

Y aquí cómo se verían esos carácteres en [Source Code Pro](https://github.com/adobe-fonts/source-code-pro):

![](https://cdn-images-1.medium.com/max/2000/0*OOk-BjFh8OLHN19E.png)

### Input

Input es una familia de fuentes tipográficas específicamente diseñadas para programadores, con propuestas bastante interesantes: ofrece fuentes proporcionales, monoespaciadas, serif y sans-serif.

¿Fuentes proporcionales para el código? David Jonathan Ross, el diseñador, dice que las fuentes monoespaciadas ni siquiera llegan a tomar en cuenta el grosor de la fuente, por lo que a veces el resaltado de la sintaxis puede producir resultados extraños, debido a que su espacio horizontal se mantiene constante, así las letras anchas se aplastan y las mayúsculas parecen estiradas al lado de las minúsculas.

![](https://cdn-images-1.medium.com/max/2000/0*aRObIWuheijDt52-.png)

Para resolver esto, su fuente proporcional intenta importar los atributos que hacen que una fuente monoespaciada sea atractiva: símbolos de puntución grandes, espaciado generoso y caractéres fáciles de reconocer individualmente

![](https://cdn-images-1.medium.com/max/2000/0*DRcoyMX3o-_lh5RH.png)

Una gran cualidad de esta fuente es que es completamente personalizable. Se pueden personalizar carácteres como **i**, **a**, **l**, **0** (cero) y también se puede escoger que tan condensada (espacio horizontal) está la fuente, este es muy valioso en el caso de tener una pantalla pequeña con líneas de código largas.

En su [página oficial](http://input.fontbureau.com) pueden encontrar una muestra, esto es un ejemplo de cómo puede llegar a verse:

![](https://cdn-images-1.medium.com/max/2000/0*iuA1UTTDs1xqUjBY.png)

El ejemplo anterior es con fuente monoespaciada, a mí me sigue gustando más.

En la [página de personalización](http://input.fontbureau.com/download/?customize) pueden descargarla completamente gratis para uso personal, en el caso de usarse en publicaciones y en web se tiene que pagar por ella.

### Operator Mono

Esta fuente la vi usada en un tutorial [Laracasts](http://laracasts.com) y me enamoré de ella, es una fuente monoespaciada sans-serif, diseñada para progrmadores y diseñadores, que tiene una característica que la hace muy notable: la cursiva cambia completamente de estilo, se vuelve una fuente más estilizada, simulando las letras de script o manuscritas.

![](https://cdn-images-1.medium.com/max/2046/0*Jf0p8R5uMnhStfHR.png)

Sus creadores pusieron [especial énfasis en las llaves y los corchetes](http://www.typography.com/blog/tag/Monospace).

Esta fuente no tiene ligaduras, no es Open Source y tiene un costo de $199 USD por los 10 estilos básicos. Se puede comprar en su [sitio oficial](http://www.typography.com/fonts/operator/overview/). Aquí un ejemplo de cómo luce en Atom:

![](https://cdn-images-1.medium.com/max/2000/0*mClbMI4fabyYpVHe.png)

Si el tema de resaltado de sintaxis que usas hace buen uso de las cursivas esta fuente luce absolutamente hermosa.

## Conclusión

Podemos ver que existen suficientes tipos de fuentes listas para diferentes gustos así que no hay pretexto para que hagamos nuestro entorno más agradable adaptado a lo que más nos funcione.

En [Programming Fonts](http://programmingfonts.org/) puedes encontrar más opciones si no te convenció ninguna de las que mostramos aquí. O también podrías usar siempre la default del sistema, es otra opción.

*Originally published at [hectoripm.com](http://hectoripm.com/fuentes-para-programadores/) on June 10, 2016.*

---
title: "Inducción y Deducción según Polya"
date: 2019-12-14
author: Héctor Patricio
tags: polya problem-solving how-to-solve-it
comments: true
excerpt: "Aprende de los conceptos de inducción y deducción según George Polya los explica en How to Solve It"
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1400/v1575746191/verne-ho-0LAJfSNa-xQ-unsplash_prh7gv.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1400/v1575746191/verne-ho-0LAJfSNa-xQ-unsplash_prh7gv.jpg
  overlay_filter: rgba(0, 0, 0, 0.5)
---

Este es el tercer artículo acerca del libro ["How to Solve It"](https://amzn.to/2P8HJA8) de George Polya. Puedes ver los dos artículos anteriores aquí:

- [Técnicas para resolver problemas](/2019/09/27/tecnicas-para-resolver-problemas.html)
- [Heurística](/2019/10/03/el-arte-de-resolver-problemas-la-heuristica.html)

Con este artículo cerraremos con las ideas que George Polya desarrolló para resolver problemas.

### Deducción

Tratar de resolver problemas por deducción significa **aplicar principios o
conocimiento general a un caso específico**. Por ejemplo para un problema
práctico en el que tenemos encontrar la longitud de un cable tensor para una
antena, sabemos que podemos aplicar el teorema de Pitágoras.

Algunos ejemplos para los programadores:

- Encontrar el elemento más grande o más pequeño en una lista. (Una forma de resolverlo es ordenar los elementos).
- Revisar que un elemento no está repetido en una colección de elementos. (Indexado)
- Asegurarse de que las operaciones son atendidas en el orden en que se solicitaron en un entorno con múltiples ejecutores. (Colas)

Lo difícil de la deducción es encontrar *qué principios, teoremas o formas
de resolución de problemas aplican para el problema que tenemos que resolver*. Para esto nos pueden ayudar las técnicas platicadas en los artículos anteriores: ¿He resuelto un problema similar? *¿Qué técnica fue usada?* ¿Qué principios sirvieron para la resolución de ese problema? Y, a mi parecer la más útil: ¿puedo usar el resultado o el proceso de resolución de un otro problema?

## Inducción

> La inducción es el proceso de descubrir **leyes generales** mediante la **observación y combinación** de casos particulares. - *George Polya*

La inducción es uno de los mecanismos de resolución de problemas más difíciles de llevar a la práctica. Funciona en forma inversa a la deducción:

Consiste en partir de observaciones específicas (ejemplos y contra-ejemplos) y llevarlas a **generalizaciones** que puedan ser aplicadas en otros casos o que apliquen en muchas otras situaciones situaciones.

Polya deja claro una cosa: aunque en las ciencias físicas y naturales la inducción es completamente válida y natural, las matemáticas son un área mayormente deductiva, debes poder tener **demostraciones** de que

### Inducción matemática

Polya habla de otro tipo de inducción de la que opina que no debería llamarse así, y que comparte muy poco con el proceso que acabamos de describir y puede llegar a confundir a la gente: la **inducción matemática**. Este tipo de inducción se refiere al método que los matemáticos emplean para **demostrar** que cierta aserción es un teorema o no.

Si has estudiado matemáticas no la confundas.

### Inducción en el desarrollo de software

El desarrollo de software no es un área que viva aislada de las demás áreas y seguro te has encontrado con este tipo problemas si ya llevas tiempo desarrollando:, las personas que requieren el software llevan **ejemplos** de  problemas que regularmente tienen que resolver.

Nuestros clientes, en general, no se han dado a la tarea de establecer las reglas por las que algo funciona de la manera en que lo hace, ni las excepciones, ni los casos únicos. Es nuestra tarea casi siempre **descubrir las reglas que subyacen a la operación del negocio de los clientes.** Esto es una forma de inducción.

Este paso es completamente necesario para desarrollar software, ya que son **estas reglas** las que ponemos en los programas, las probamos con los tests y lo que hace valioso al software.

Así que tenemos que ser lo más hábiles que nuestras circunstancias lo permitan haciendo inducción. **¿Cómo podemos mejorar?**

## Desarrollando tus capacidades de Inducción

Polya da un montón de consejos para aplicar la inducción como el "descubrimiento" de las reglas que están bajo un problema.

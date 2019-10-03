---
title: "El arte de resolver problemas: la heurística"
date: 2019-09-27
author: Héctor Patricio
tags:
comments: true
excerpt: "La heurística te ayudará a resolver mejor los problemas que se te presentan como programador. Veamosla más detenidamente."
header:
  overlay_image: 
  teaser: 
  overlay_mask: rgba(0, 0, 0, 0.5)
---

> La heurística habla del **comportamiento humano** frente a los problemas. - George Polya

En un [artículo anterior](2019/09/27/tecnicas-para-resolver-problemas.html) analizamos la estructura básica de un problema y la estructura de resolución que George Polya propone para intentar resolverlos.

Polya analiza a fondo la estructura del proceso de resolución de problemas. Aquí hablaremos de **la heurística**, de la que escribió en [**"How to solve it"**](https://math.hawaii.edu/home/pdf/putnam/PolyaHowToSolveIt.pdf){:target="_blank"}, un compendio que pensó originalmente como un análisis de esta.

## Definición

La palabra heurística viene de una raíz griega que transmite la idea de **descubrimiento o invención**. La heurística históricamente ha estado relacionada con **estudiar los medios por los que se descubre o inventa algo**. Su campo de estudio abarca la lógica, la psicología y la filosofía, pero no se puede acotar a ninguna de las tres áreas.

Polya estudia y define la heurística moderna _el arte de resolver problemas_, porque en eso consiste el proceso: descubrir una solución(en los problemas en los que hay que _encontrar algo_) o inventar algo (en los problemas en los que hay que _crear una demostración_).

Podemos echar mano de lo que nos enseña al atacar problemas muy difíciles de los que no tenemos la mínima idea de cómo resolver o no podemos idear un plan confiable para resolverlos (recuerda que crear un plan es el punto medular de la resolución de un problema).

## Heurística moderna

La heurística actualmente busca entender el proceso de resolución de problemas, pero particularmente las operaciones mentales relacionadas con ese proceso.

> La experiencia en la resolución de problemas u observar a otros resolver problemas debe ser la base de la heurística. - G. Polya

Se busca encontrar patrones y propiedades comunes en una gran variedad de problemas, por lo que se puede decir que la heurística tiende a la generalidad, estudia procedimientos que son independientes del dominio del problema.
Polya habla de múltiples métodos y procedimientos para avanzar en la resolución de un problema complicado.

Analicemos algunos de ellos:

- **Variación del problema**. ¿Puedo variar por lo menos temporalmente alguna de las partes del problema? ¿Puedo cambiar los datos, las condiciones o la solución?
- **Descomposición y recombinación**. Esta operación mental implica entender y separar las partes esenciales de un problema y tratar de re-crearlo con un nuevo entendimiento o crear un problema ligeramente diferente.
- **Regresar a las definiciones**. Comprender los términos usados en cada parte del problema a veces implicará que busquemos lo que algo significa desde sus raíces. Esto nos puede ayudar a entender mejor el problema así como a introducir elementos auxiliares que ayuden en la resolución.
- **Generalización, especialización y analogías**. Estas tres operaciones son una forma de variar un problema. ¿Puedo hacer el problema más amplio, para resolver un caso más general y después aplicar los resultados o el método a mi problema original? ¿Existe un problema similar al que estoy resolviendo que pueda resolver más fácilmente?
- **Notación adecuada**. Una vez entendido el problema, sobre todo para problemas matemáticos, es muy importante introducir notación que nos pueda ayudar a trabajar sobre el problema. Para los problemas matemáticos y en ciencias en general, ya existen estas notaciones estándar. Para nuestros problemas tenemos que inventar una que la mayoría de los implicados puede entender y usar.
- **Suponer, pero comprobar las suposiciones**. Para avanzar en la resolución de un problema muchas veces hay que dar cosas por supuesto, como en el caso de las comprobaciones por reducción al absurdo. Polya afirma que no está mal suponer cosas temporalmente mientras más adelante encontremos una forma de comprobar o rechazar esas suposiciones.
- **Trabajar en reversa**. Muchas veces sabemos _como luce_ la solución, o tenemos que comprobar que una solución supuesta es correcta. Trabajar en reversa significa avanzar de la solución hasta nuestro estado actual, trabajando paso por paso hasta poder encontrar la cadena de transformaciones necesarias para conectar esos estados.

- **Aspectos psicológicos: determinación, esperanza y éxito**.


La heurística es práctica y puede tener buena influencia en la enseñanza.
## Algoritmos heurísticos

Ahora hablemos de aprovechar estas ideas a la programación, con una clase de algoritmos conocidos como algoritmos heurísticos.

Un algoritmo heurístico en vez de garantizar siempre la mejor solución en cada paso del programa, acepta soluciones parciales o suficientemente buenas. Este tipo de algoritmos funciona muy bien en casos donde hay demasiadas soluciones posibles como para probarlas todas (fuerza bruta) o muchas de ellas (como los algoritmos de _backtracking_).

La principal diferencia a tener en cuenta cuando hablamos o tratamos con este tipo de algoritmos es que **no garantizan la respuesta correcta o la respuesta óptima**, aunque en algunos casos son la mejor forma de lograrlo. Fuera de la programación, la heurística es un método para llegar a la respuesta correcta aceptando temporalmente soluciones intermedias no óptimas, semi-erróneas o incompletas.

<!-- Hay varias técnicas que se pueden clasificar como heurísticas para crear algoritmos. entre ellas algunos algoritmos voraces (greedy). -->

## Ejemplos

La mejor manera de entender la heurística es con algunos ejemplos.

### Ejemplo 1

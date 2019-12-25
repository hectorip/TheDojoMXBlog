---
title: "Las matemáticas que debes saber para programar"
date: 2019-12-25
author: Héctor Patricio
tags: math, matemáticas, aprender
comments: true
excerpt: "¿Qué tantas matemáticas necesitas para programar? En este artículo lo veremos."
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1440/v1576990677/franck-v-tOjIx_NyzFo-unsplash_iu91kg.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1440/v1576990677/franck-v-tOjIx_NyzFo-unsplash_iu91kg.jpg
  overlay_filter: rgba(0, 0, 0, 0.5)
---

Cuando se habla de **matemáticas** mucha gente empieza a sentirse fastidiada y a temer, porque generalmente se habla de cosas que no son de su agrado. Sin embargo, las matemáticas son la base de muchas otras ciencias y sobre de todo de la computación. Podríamos considerar las ciencias de la computación como **una rama de las matemáticas**.

Pero para programar con eficacia no necesitas saber muchas matemáticas, de hecho con el entendimiento básico es suficiente. En este artículo hablaremos de aquello que debes dominar.

## Matemáticas Básicas

Empecemos hablando brevemente de las matemáticas que debes conocer como programador y como ser humano.

### Operaciones básicas

Saber operar con números en la vida cotidiana es una habilidad que todos necesitamos. Pero más importante aún es entender el significado de estas operaciones:

- ¿Qué significa una multiplicación?
- ¿Qué significa una división?
- ¿Qué significado tiene el elevar un número a una potencia?

Entender esto te ayudará a **resolver problemas** que es la actividad principal que se realiza cuando programas. Todo lo demás está alrededor de esto.

### Probabilidad y estadística

Tener las nociones de estas áreas es una las herramientas más útiles a la hora de resolver problemas y sobre todo atacarlos prácticamente. Varias de las áreas de la ciencia de la computación basan sus resultados y procesos en estas dos áreas.

Un ejemplo es la **criptografía**: los algoritmos de cifrado como el AES actual trabajan con una llave que es usada para cifrar y descifrar el mensaje. Asignar el tamaño de la llave depende totalmente de la _probabilidad_ de que un atacante sea capaz de adivinar la llave en un número de intentos razonable. Ahora imagina que la llave tiene 128 bits de longitud. Aquí entra otro par de conceptos importantes para la computación.

### Combinaciones y permutaciones

¿Cuál es el número de llaves diferentes que se pueden generar con 128 bits? La respuesta es: 2^128 (2 elevado a la potencia 128). *¿Cómo llegamos a esa respuesta?* Esto se conoce como **conteo** en matamáticas y las bases son la **permutación** y la **combinación** de elementos. En este caso es la permutación es de 2 elementos que permiten repetición en 128 lugares.

¿Qué probabilidad hay de que alguien encuentre esa llave por suerte en el primer intento?

La respuesta es 1/2^128.

La criptografía y varias áreas están llenas de probabilidad y estadística (como el aprendizaje automático y el análisis de datos, aunque más avanzadas).

Si sientes que necesitas un recordatorio de esto Khan Academy tiene cursos en español que enseñan desde lo más básico: [Conteo, combinaciones y permutaciones en Khan Academy](http://bit.ly/2rrL4mb).

## Lógica (Matemáticas discretas)

Las matemáticas discretas son una de las áreas más abstractas de las matemáticas cuando las vemos en papel pero en realidad tratamos con ellas a diario. Podemos definir las matemáticas discretas como el estudio de las cosas que se pueden contar, sean finitas o infinitas.

La **lógica** es uno de los campos de estudio de las matemáticas discretas. La lógica se enfoca en estudiar **el razonamiento** y sobre todo si el razonamiento es *correcto*.
Para lograr esto la lógica se vale del estudio de las **proposiciones** (o afirmaciones) y sus relaciones. Una proposición es un enunciado que dice algo que puede ser *verdadero* o *falso*. En matemáticas se dice que tiene un **valor de verdad**.

Dos proposiciones se pueden relacionar mediante un *conector* (en electrónica: compuertas lógicas, en programación son operadores booleanos). Los conectores más conocidos son el **or** (o) y el **and**(y).

Esto da origen a demostraciones tanto matemáticas como prácticas. En el desarrollo de sistemas se pueden usar para demostrar que tu algoritmo o solución es correcto, es decir, va a funcionar con los datos de entrada propuestos que cumplan con los valores de verdad.

¿Son absolutamente necesarias para programar? Las demostraciones no, pero serán útiles si quieres crear demostraciones de que un algoritmo funciona sin tener que crear miles de ejemplos que convenzan a alguien. **Lo que sí es necesario entender es el funcionamiento de los conectores lógicos, no hay programa que se escape de ellos.**

### Conjuntos

El estudio de los conjuntos es una parte de las matemáticas discretas que se enfoca en estudiar elementos (objetos) que se agrupan por alguna característica en común. Los conjuntos son de gran utilidad para resolver muchos problemas matemáticos y la criptografía actual esta fuertemente basada en algunos problemas que tienen que ver con el cálculo de ciertos conjuntos.

¿Me srive para trabajar en el día a día? Para cierto tipo de problemas es más cómodo trabajar con conjuntos que con los tipos de datos comunes de colecciones a los que estamos acostumbrados los programadores. Tratar tu colección (lista, tupla, etc.) como un conjunto matemático te permitirá efectuar operaciones como la **intersección de conjuntos** (elementos en común), la **unión** (todos los elementos únicos encontrados en dos o más conjuntos). Si el lenguaje de programación tiene este tipo de dato te va a dar un buen empujón.

Por cierto, el resultado de las consultas en SQL (lenguaje de manejo de datos para la mayoría de las bases de datos) se comortan como conjuntos matemáticos.

¿Quieres aprender matemáticas discretas? Aquí tienes un pequeño curso: [Curso de matemáticas discretas](http://bit.ly/2EWToND).

Eso es todo lo que necesitas para programar básicamente. Mientras mejor seas en estos campos, mejor podrás aprovecharlos para progrmar mejor o para entender mejor los programas de otros.

# Matemáticas avanzadas y especificas

En muchas áreas de la programación se usan matemáticas más avanzadas, sobre todo en áreas que están sonando mucho recientemente: análisis de datos e inteligencia artificial. Si quieres entender a fondo estas y otras áreas del desarrollo de sistemas, es conveniente tener un conocimiento amplio en algunas de las siguientes áreas:

- **Probabilidad y estadística avanzada**. Saber acerca de variables aleaterias, distribuciones de probabilidad, análisis bayesiano, etc. Esto te permitirá analizar datos tanto exploratoria como predictivamente.
- **Álgebra lineal**. El álgebra y la resolución de ecuaciones que representan líneas en el plano cartesiano. Esto te ayudará a tratar con conjuntos de datos. Muchas de los resultados de los algoritmos de Machine Learning son ecuaciones lineales.
- **Ecuaciones diferenciales**. Esto es la resolución de sistemas de ecuaciones y sus derivadas. Esto tiene aplicaciones en todo lo que tenga que ver con cambios respecto a alguna variable, como el tiempo.

Hablé de los campos finales pero para entender esto debes saber antes cosas como:

- Geometría Analítica
- Álgebra
- Trigonometría
- Cálculo Integral y diferencial
- Cálculo Vectorial

Por suerte, para los campos de los que hablá arriba no tienes que saber todo esto, a menos que quieras ser el desarrollador de los algoritmos originales. Generalmente somos usuarios de bibliotecas creadas por genios que ya hacen lo que necesitamos.

## No te preocupes :)

Fuera de las matemáticas básicas y un control decente e intuitivo de la lógica, no es necesario que seas [Terence Tao](http://bit.ly/2StKLCz), a menos que el campo en el que estés trabajando esté directamente relacionado con eso, tal
como tendrías que saber lo suficiente de finanzas si estuvieras haciendo una app financiera o de administración de empresas si estuvieras haciendo una aplicación o plataforma para este campo.

Aquí hay un video curso en el que se explican más ampliamente lo que algunos llaman ["matemáticas para programadores"](http://bit.ly/2rvD6Zi)
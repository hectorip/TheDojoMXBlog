---
title: "Técnicas para resolver problemas"
date: 2019-09-08
author: Héctor Patricio
tags: matemáticas maths polya books libros
comments: true
excerpt: "¿Cuántas veces te has enfrentado a problemas de los que no tienes ni idea de cómo empezar a resolver? George Polya escribió un libro completo sobre eso en 1928."
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1200/v1566189999/91gQt6wB-KL_t7svba.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1200/v1566189999/91gQt6wB-KL_t7svba.jpg
  overlay_filter: rgba(0, 0, 0, 0.5)
---

George Polya fue uno de los matemáticos más prolíficos del Siglo XX, un matemático de primera clase (de esos que descubren e inventan cosas) pero que mantenía un interés por la educación y le enseñanza de las matemáticas, algo muy peculiar.

Polya escribió varios libros, entre ellos está "How to solve it" un tratado de 4 partes en el que explica de manera muy detallada cómo resolver problemas matemáticos principalmente, pero también cómo aplicar este conocimiento a otras áreas de la vida.

Todos los desarrolladores nos hemos encontrado con problemas que nos dejan perplejos y que no tenemos idea de por dónde empezar a resolver. Las técnicas explicadas por Polya te pueden ayudar a desarrollar tus capacidades de resolución de problemas.

Empecemos por hablar de la estructura los problemas de los que Polya habla en su libro.

## Estructura de un problema

Polya define un problema un enunciado o texto con tres partes:

1. **Los datos**. Es la información que tenemos disponible para resolver el problema.
2. **Las condiciones**. Describen la relación que existe entre los datos y la solución, pero también la forma, los límites y características de la solución buscada.
3. **La incógnita o lo desconocido**. Es la información que buscamos y que cumple con las condiciones del problema.

Es muy importante conocer la composición de un problema para poder aplicar las técnicas descritas en el libro. Cualquier problema matemático debería **cumplir con estas características**, pero no todos los problemas de la vida real cumplen con esta estructura tal y como la necesitamos o esperamos, por lo que deberíamos ser capaces de entender los problemas que se son presentan y estructurarlos lo mejor posible según esta definición.

Para resolver un problema deberías ser capaz de contestar las siguientes preguntas:

1. ¿Qué estoy buscando? ¿Cuál es la incógnita?
2. ¿Qué datos tengo disponibles? ¿Son suficientes los datos que tengo para resolver el problema?
3. ¿Qué condiciones tiene que cumplir la incógnita? ¿Qué relación hay entre los datos y la incógnita?

Ahora hablemos de de los tipos de problemas de los que Polya hace distinción.

## Tipos de problemas

Polya hace la distinción entre dos tipos diferentes de problemas que hay que tratar de manera ligeramente diferente para poder resolverlos de mejor manera, aunque la estructura sea la misma.

### 1. Problema para encontrar

Estos son los problemas básicos que nos ponían en la escuela primaria: "Hallar el área de un terreno cuadrado de 10m por lado", "Encuentra la diámetro de una circunferencia con un perímetro de 12cm". En este tipo de problemas hay que encontrar un "resultado", que puede ser numérico o no. En la vida real este tipo de problemas son la mayoría de los que nos encontramos.

Como programadores podríamos tener estos ejemplos de este tipo de problemas:

- ¿Qué complejidad tiene este algoritmo que acabo de programar?
- ¿A cuántos usuarios simultáneos podré atender con este servidor con 4GB de RAM?
- ¿Cuánto tiempo va a tardar en subir mi millón de archivos si lo paralelizo? ¿Cuánto va a tardar si no lo paralelizo?


Varios de estos problemas suenan demasiado simples porque ya los tenemos bien trabajados a base de repetición. Pero otros que no tienen una respuesta numérica pueden ser un poco más complicados:

- ¿Qué base de datos debería usar para servir notificaciones en tiempo real?
- ¿Qué lenguaje de programación debo usar para un sistema que estará emebebido en un millón de dispositivos electrónicos mandando notificaciones críticas cada segundo?
- ¿Qué sistema de comunicación puedo usar entre dos dispositivos que no cuentan con una conexión confiable a internet?

### 2. Problemas para demostrar

> "Demuestre que la línea de mayor longitud que toca dos puntos de una circunferencia pasa por el centro del círculo". 

Esto es un ejemplo de un problema para demostrar. Estos implican la comprobación o refutación de una aserción (hipótesis) enunciada en el problema. Estos problemas generalmente nos los ponían en la preparatoria o universidad, por su naturaleza son un poco más difíciles en general.

Para un desarrollador podríamos poner problemas para demostrar como:

- "Demuestra que es imposible un bloqueo mutuo entre procesos con el algoritmo usado actualmente".
- "¿Cómo sabemos que evitamos todas las condiciones de carrera en el sistema actual?"
- "Comprueba que el máximo tiempo que puede tardar el sistema en responder es menor que X"

Espero que con estos ejemplos haya quedado clara la diferencia entre los diferentes tipos de problemas.

### Problemas matemáticos, acertijos y problemas de la vida real

Polya habla en sus libro sobre todo de un tipo muy especial de problemas: **los problemas matemáticos**.

Un problema matemático bien definido cuenta con:

1. Datos suficientes para resolución
2. No tiene datos sobrantes
3. Condiciones no contradictorias o imposibles de cumplir

Por extensión, los acertijos cumplen con las mismas características, y se dan algunos de ejemplos de ellos en el libro.
Pero los problemas de la vida real son muy diferentes, ya que estos pueden no cumplir con las características completas
de un problema bien definido. Así que uno de los pasos previos para resolver un problema de la vida real es intentar definir lo mejor posible el problema por resolver.

## Cómo empezar a resolver un problema
Polya plantea cuatro etapas de resolución de un problema:

1. Entendimiento
2. Planeación
3. Ejecución
4. Retrospectiva

Hablemos de cada una, para entender claramente cómo podemos mejorar nuestras posibilidades de resolución de un problema.

### Entendimiento

> Es tonto contestar una pregunta que no entiendes. Es triste trabajar por un fin que no deseas. - **G. Polya**

El entendimiento del problema consiste primero en asegurarnos de que **entendemos el planteamiento verbal del problema**, si no tenemos ni siquiera un planteamiento verbal, debemos empezar por crearlo.

Para decir que comprendemos el problema, tenemos que conocer los datos que se dan, las condiciones a satisfacer y la incógnita o lo que hay que demostrar.

Esta parte puede llevar gran parte del tiempo total dedicado al problema, ya que es el fundamento de los próximos pasos, sin la que no se puede continuar.

 ### Planeación

El siguiente paso es trazar un plan para atacar el problema. Esta es la parte más difícil, ya que implica conocimiento profundo del problema y es casi un esbozo de la solución.

 ### Ejecución

 Es hora de llevar a cabo los pasos establecidos en la planeación. En esta etapa hay que ejecutar cada uno de los pasos que establecimos en la planeación de ejecución del problema. Polya dice que aquí es donde hay que ser rigurosos con lo que hacemos, verificando que lo que hacemos tenga sentido y sea estrictamente correcto.

 ### Retrospectiva

Revisar los resultados, ver si podemos hacer algo diferente, si nuestro resultado cumple con lo esperado y si podemos encontrar o derivar el resultado de alguna otra forma ahora que ya sabemos cuál es.

### Las preguntas de Polya

Polya estableció una serie de preguntas que pueden guiarte en la solución de un problema. Estas preguntas las repite vez tras vez en el libro y en verdad son iluminadoras si estás atorado en algún problema que no puedes resolver. A continuación las listamos.

- ¿He resuelto un problema **relacionado**? ¿Conozco un **problema que se aproxime**?
- ¿Estoy usando todos los datos?
- ¿Puedo cambiar algo del problema para hacerlo más fácil?
  - ¿Puedo cambiar los datos?
  - ¿Puedo cambiar las condiciones?
  - ¿Puedo cambiar la incógnita?
  - ¿Qué debería mantener?
- 

## Heurística - El arte resolver problemas

> Tenemos que cambiar nuestra posición una y otra vez. - **G. Polya**

La frase anterior deja clara la actitud que se debe tener respecto a algunos problemas.
Cuando no tienes idea del procedimiento a seguir para resolver un problema, existe una forma de experimentar para poderlo resolver efectivamente.

Esta forma de experimentación consiste en aceptar soluciones parciales, semi-erróneas y asumidas (o completamente inventadas) para avanzar en la resolución del problema. Si una de estas soluciones nos ayuda avanzar en el problema, es aceptada.

## Inducción y Deducción

Polya apoyándose en la sabiduría de otros.

## Análisis y Síntesis

Análisis: proceso para entender y descomponer un problema, planear los pasos necesarios. Ida.
Síntesis: ejecución de los pasos para llevar a cabo los resultados del análisis. Regreso.


## Para recordar

Para resolver un problema:
  - Asegúrate de entender el problema completamente: qué datos tienes, qué relación hay entre los datos y la incógnita y lo que tienes que encontrar.
  - Planea cómo vas a atacar el problema
  - Si estás detenido en la resolución de un problema puedes:
    - Variar los datos, las condiciones o el resultado esperado.
    - Pensar en otros problemas que se le parezcan: puedes usar el método que usaste para resolverlos o el resultado.
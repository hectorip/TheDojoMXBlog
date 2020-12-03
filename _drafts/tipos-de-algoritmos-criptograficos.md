---
title: "Tipos de algoritmos criptográficos: cifrados de Bloque"
date: 2020-11-26
author: Héctor Patricio
tags:
comments: true
excerpt: "¿Sabes que es un cifrado de bloque? En este artículo hablamos de eso y te damos algunos ejemplos."
header:
  overlay_image: #image
  teaser: #image
  overlay_filter: rgba(0, 0, 0, 0.5)
---

Ya hablamos de lo que es [la criptografía](/2019/11/12/criptografia-basica-para-programadores-que-es-la-criptografia.html), ahora empecemos a hablar de los tipos de
algoritmos criptográficos que existen, sus características y sus principales diferencias. En este artículo hablaremos de los cifrados de bloque.

### ¿Qué es un cifrado de bloque?

Los cifrados de bloque trabajan sobre un conjunto de bits de tamaño fijo, produciendo un texto cifrado del mismo tamaño. Para cifrar datos de tamaño arbitrario como sucede en la vida real, se utiliza el algoritmo de cifrado de bloque combinado con diferentes técnicas llamadas **Modos de Operación**.

Algunos ejemplos de estos algoritmos de cifrado son el DES (Estadounidense), GOST 28147-89 (Ruso) y el actual **AES**.

Un bloque cifrado debe ser _permutación pseudo-aleatoria_ de bits, es decir, un conjunto de bits que sean _indistinguibles de bits generados completamente de manera aleatoria_. Es como si aventaras un montón de bits y dijeras que esa es la salida de tu algoritmo.

Esta propiedad evita que un atacante obtenga información sobre el contenido del mensaje que fue cifrado.

## Ejemplos de Cifrado de Bloque

Veamos algunos ejemplos de cifrados de bloque y sus características principales. Algunos se usan mientras que otros ya cayeron en el olvido.

### DES y Triple DES

El **Data Encryption Standard** era el algoritmo que más se usaba en la década de los 90, lo suficientemente seguro para el poder de cómputo de aquel entonces. Usa una llave de 56 bits y bloques de 64 bits. Debido a estas características, el poder de cómputo actual hace que sea demasiado fácil de romper con hardware decente, así que su uso está completamente desrecomendado. Por ejemplo, el tamaño de bloque hace que sea vulnerable a ataques de "codebook" en el que

Su sucesor, el Triple DES realiza tres veces el mismo proceso usando tres llaves diferentes, con un tamaño de llave de 168 bits. Esto evita que sea posible romperlo a base de fuerza bruta, pero este proceso provee sólamente una seguridad de 112 bits, por lo que se considera ineficiente (usas el cómputo de tres DES para obtener seguridad de una llave del doble de tamaño) y por lo tanto su uso no es recomendado también.

### AES

Debido a las visibles fallas de DES y triple DES, la NIST (National Institute of Standards and Technology de Estados Unidos) quería un algoritmo de cifrado que fuera dado a conocer públicamente y "capaz de proteger la información sensible del gobierno por los próximos cien años".

El **Advanced Encryption Standard** (Estándar de cifrado avanzado), es en realidad un subconjunto de los cifrados posibles de otro algoritmo llamado [Rijndael](https://csrc.nist.gov/csrc/media/projects/cryptographic-standards-and-guidelines/documents/aes-development/rijndael-ammended.pdf) y que fue el ganador del concurso que la NIST hizo para seleccionar el nuevo algoritmo de cifrado estándar que sustituiría a DES.

Rijndael fue creado por analistas criptográficos Belgas con objetivos claros: que fuera rápido y simple. Es una familia de cifrados que permiten cifrar bloques en múltiplos de 32 bits, desde 128 hasta 256 bits (128, 160, 192, 224, 256 bits). Las longitudes de llaves posibles son los mismos desde 128 hasta 256 bits.

AES es Rijndael con bloques de **128 bits** y llaves que pueden ser de 128, 192 o 256 bits.

AES aplica internamente una misma operación múltiples veces dependiendo del tamaño de la llave, y esto le permite se más seguro aumentando el tamaño de la llave. Esto es lo que se conoce como los "rounds" de AES, usando 10 para llaves de 128 bits, 12 para 192 bits y 14 para 256 bits.

AES tiene un diseño de operaciones concurrentes, que es fácilmente paralelizable y puede implementarse muy eficientemente en hardware, de hecho los procesadores modernos normalmente lo traen implementado en sus circuitos, es parte del conjunto de instrucciones del procesador.

La seguridad de AES según ciertos criptanalistas (por ejemplo, los creadores de Twofish) está completamente rota _teóricamente_, ya que hay ataques que pueden romper el cifrado de 14 ciclos (los ciclos completos que hace la versión de la llave de 256 bits) con ciertas condiciones, con 2^176 operaciones (lo cuál es un ataque que no se puede llevar a la práctica fácilmente).

Los ataques mencionados anteriormente no tienen nada de prácticos, es decir, no se pueden llevar a la realidad en entornos normales, por lo que no se piensa por ningún lado que la seguridad de AES está comprometida. Si necesitas un algoritmo de cifrado confiable y rápido, con AES no te puedes equivocar.

## Otros algoritmos

Como finalistas del concurso de la NIST hay otros algoritmos que vale la pena mencionar:

1. **Serpent.** Es un algoritmo de cifrado de bloque que está pensado completamente para ser resistente. Aplicaca una operación repetidamente (rounds) pero a diferencia de AES la aplica 32 veces. Los criptanalistas han logrado romper 12 de esos 32 rounds, por lo que se piensa que tiene bastante espacio de reserva para continuar siendo seguro. La desventaja contra AES es que es 3 veces más lento.

2.
### Modos de operación

Un modo de operación es la forma en que se aplica un cifrado de bloque a un texto no cifrado que no es del tamaño exacto del bloque.

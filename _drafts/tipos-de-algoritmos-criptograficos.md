---
title: "Tipos de algoritmos criptográficos: cifrados de Bloque"
date: 2020-10-06
author: Héctor Patricio
tags:
categories:
comments: true
excerpt: "Escribe aquí un buen resumen de tu artículo"
header:
  overlay_image: #image
  teaser: #image
  overlay_filter: rgba(0, 0, 0, 0.5)
---

Ya hablamos de lo que es [la criptografía](/2019/11/12/criptografia-basica-para-programadores-que-es-la-criptografia.html), ahora empecemos a hablar de los tipos de
algoritmos criptográficos que existen, sus características y sus principales diferencias. En este artículo hablaremos de los cifrados de bloque.

### Cifrados de Bloque

Los cifrados de bloque cifran un conjunto de bits de tamaño fijo, produciendo un texto cifrado del mismo tamaño. Para cifrar datos de tamaño arbitrario, el contenido completo se va cortando en los bloques del tamaño que el algoritmo acepta y combinando los textos cifrados con otro algoritmo conocido como **modo de operación**.

Algunos ejemplos de estos algoritmos de cifrado son el DES (Estadounidense), GOST 28147-89 (Ruso) y el actual **AES** ().

Un bloque cifrado es una _permutación pseudoaleatoria_ de bits, es decir, un conjunto de bits que son indistinguibles de bits generados completamente de manera aleatoria. Es como si aventaras un montón de bits y dijeras que es es la salida de tu algoritmo.

Esta propiedad evita que un atacante obtenga información sobre la información que fue cifrada.

## Ejemplos de Cifrado de Bloque

Veamos algunos ejemplos de cifrados de bloque y sus características principales.

### DES

### Triple DES

### Serpent

### Twofish

Uno de los autores de

### AES

La NIST quería un algoritmo de cifrado dado a conocer públicamente "capaz de proteger la información sensible del gobierno por los próximos cien años".

El **Advanced Encryption Standard** (Estándar de cifrado avanzado), es en realidad un subconjunto de los cifrados posibles de otro algoritmo llamado [Rijndael](https://csrc.nist.gov/csrc/media/projects/cryptographic-standards-and-guidelines/documents/aes-development/rijndael-ammended.pdf) y que fue el ganador del concurso que la NIST hizo para seleccionar el nuevo algoritmo de cifrado estándar que sustituiría a DES.

Rijndael fue creado por analistas criptográficos Belgas con objetivos claros: que fuera rápido y simple. Es una familia de cifrados que permiten cifrar bloques en múltiplos de 32 bits, desde 128 hasta 256 bits (128, 160, 192, 224, 256 bits) y lo mismo para las llaves.

AES es Rijndael con bloques de **128 bits** y llaves que pueden ser de 128, 192 o 256 bits.

AES aplica internamente una misma operación múltiples veces dependiendo del tamaño de la llave, y esto le permite se más seguro aumentando el tamaño de la llave.

Gracias al diseño concurrente de AES, es fácilmente paralelizable y puede implementarse muy eficientemente en hardware, de hecho los procesadores modernos normalmente traen lo traen implementado en sus circuitos y se puede es parte del conjunto de instrucciones del procesador.

La seguridad de AES según ciertos analistas criptográficos está completamente rota _teóricamente_, ya que hay ataques que pueden romper el cifrado de 14 ciclos (los ciclos completos que hace el )

### Modos de operación

Un modo de operación es la forma en que se aplica un cifrado de bloque a un texto no cifrado que no es del tamaño exacto del bloque.

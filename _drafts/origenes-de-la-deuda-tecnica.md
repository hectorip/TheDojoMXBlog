---
title: "Orígenes de la deuda técnica"
date: 2020-10-16
author: Héctor Patricio
tags: deuda-técnica arquitectura diseño-de-software
comments: true
excerpt: "¿Qué es la deuda técnica y cómo podemos hacer para dominarla al máximo?"
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1400/v1585958469/17CDCA65-B853-4433-AE63-AACCFF577A3B_ufg1pl.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1400/v1585958469/17CDCA65-B853-4433-AE63-AACCFF577A3B_ufg1pl.jpg
  overlay_filter: rgba(0, 0, 0, 0.5)
---

Tuvimos una plática con **Sagrario Meneses** sobre la **deuda técnica** y cómo podemos atacarla. En este artículo te presentamos un pequeño resumen de lo que es y algunas experiencias sobre su manejo.

## ¿Qué es la deuda técnica?

La definición corta de deuda técnica es: **todo aquello que hace que el software sea más difícil de producir**.

Esto incluye algunas cosas como:

- Los valores fijos que pueden cambiar en el futuro y en realidad deberían ser fáciles de cambiar sin tener que modificar el código (_hardcoding_)

- Falta de información: cuando nadie sabe sobre cómo trabaja cierta parte del sistema o qué hace cierta pieza de código

- Falta de distribución de información y conocimiento: cuando muy pocas personas saben sobre una parte del sistema y se convierten en cuello de botella

- Falta de diseño explícito

- Malas elecciones sobre diseño o tecnologías

Sagrario comparó la deuda técnica con **deberle dinero a la mafia**: no la puedes negociar, y cuando te supera estás en grandes problemas. Así que más vale que la aprendamos a controlar porque la deuda técnica puede hacer colapsar tu sistema.

## Formas de hacer visible la deuda técnica

Sagrario recomendó una forma que nos parece súper efectiva para hacer visible (literalmente) la deuda técnica: ponerlo en tablero de control en un espacio físico idealmente, que esté a la vista tanto del equipo técnico como del equipo administrativo.

## Prácticas para evitarla y dominarla

Para poder reducir la deuda técnica hacen falta principalmente dos
cosas:

1. Pruebas, principalmente unitarias. Esto permitirá encontrar los errores más rápidamente, pero además refactorizar sin miedo.
2. Lineamientos estrictos respecto a las acciones en el proyecto.

## Otros temas


## Conclusión

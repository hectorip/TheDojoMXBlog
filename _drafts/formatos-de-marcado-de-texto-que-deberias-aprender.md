---
title: "Formatos de marcado de texto que deberías aprender"
date: 2019-12-17
author: Héctor Patricio
tags: markdown restructured-text asciidoc latex
categories: 
comments: true
excerpt: "A veces tienes que crear documentos de texto con un algún tipo de formato visual. Aprende lenguajes de marcado que te facilitarán la vida."
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1400/v1576563210/raychan-QtHYdJsBRFU-unsplash_mpyus4.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1400/v1576563210/raychan-QtHYdJsBRFU-unsplash_mpyus4.jpg
  overlay_filter: rgba(0, 0, 0, 0.5)
---

Parte del trabajo de un desarrollador es crear documentos con un formato fácil de entender y agradable a la vista, para crear documentación, registrar decisiones, escribir manuales, etc. La forma común de hacerlos es un procesador de textos como Word o Google Docs, pero generalmente batallamos sobre todo con el formateo y embellecimiento de documento.

En este artículo te platicaré de **tres alternativas** que pueden hacer tu vida más fácil: Markdown, reStructuredText, AsciiDoc.

Todos estos lenguajes pueden producir múltiples formatos de salida: HTML, PDF, Word, entre otros. Y lo mejor es que estas salidas son personalizables.

## Markdown

Es el formato de marcado de texto simple más conocido por ser el usado en muchos lados (GitHub, por ejemplo) para darle un poco de formato semántico al texto.

Puedes crear los estilos de texto más comunes directamente: 

* **negritas**
* _cursivas_
* [enlaces](/)
* Imágenes:

![Imagen de ejemplo](https://res.cloudinary.com/hectorip/image/upload/c_scale,w_100/v1559453194/luis-dille-1098834-unsplash_vndt6g.jpg)

También permite crear listas no numeradas, como la anterior, numeradas, tablas y una serie de títulos de diferente jerarquía equivalentes a los headers de HTML (h1, h2... h6).

De hecho, esta entrada está escrita con Markdown. Markdown es tan popular que existen aplicaciones completamente dedicadas a él como [MacDown](http://bit.ly/2M7YmLL
), [Focused](http://bit.ly/38Zhohc) y [Typora](http://bit.ly/2S4MX38). Además, diferentes empresas han creado sus propios dialectos o adaptaciones para que sea más fácil de usar en su caso específico.

Si aún no lo sabes usar, vale la pena que le eches un ojo: (Guía de Markdown en español)[http://bit.ly/38S2l8G]. Tardarás unos minutos en aprender lo básico que es muy útil para el 80% de los casos en los que lo ocuparas.

Markdown es muy bueno para crear documentos individuales pero, ¿qué pasa si el texto que quieres escribir es más extenso? Tal vez el texto está compuesto por muchas partes, como un libro. Tal vez necesites incluir un índice de temas o de palabras.

Las siguientes herramientas están mejor que preparadas que Markdown para eso, permiten crear cuerpos de textos más.

## reStructuredText

Este formato de texto es adecuado para crear cuerpos de texto más complejos que con Markdown. Tienes por lo menos las mismas capacidades de formateo de texto que con Markdown: negritas, cursivas, cabeceras, links, imágenes, listas, tablas, etc.

Pero reST provee más cosas, ya que fue creado para ser el lenguaje de documentación de herramientas de software, específicamente en docutils[](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#quick-syntax-overview).

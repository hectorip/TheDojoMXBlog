---
title: "Criptografía básica para programadores: ¿Qué es la criptografía?"
date: 2019-11-01
author: Héctor Patricio
tags:
categories: 
comments: true
excerpt: "Aprende las bases de la criptografía para tenerla en cuenta en tus programas."
header:
  overlay_image: #image
---

Es muy común escuchar de "encriptación" (la palabra correcta en español es _cifrado_), llaves, algoritmos criptográficos y cosas parecidas, sobre todo con el surgimiento de Bitcoin y Blockchain.

Uno de los temas menos tratados por programadores de software común (para usuarios y sistemas que no impliquen el uso de seguridad a medida), es el correcto uso de los algoritmos criptográficos y muchas veces ni siquiera conocemos lo suficiente de ellos, sino que confiamos en lo que las herramientas pre-establecen (que gran parte de las veces fue diseñado por expertos y eso está bien).

Pero un poco de conocimiento sobre criptografía no te hará daño, sobre todo si programas sistemas que necesiten seguridad (todos), y sí puede evitarte errores fatales.

Esta serie de artículos tratará de todo lo que un programador debe saber acerca de la aplicación correcta de algoritmos criptográficos a sus desarrollos, y un poco de su funcionamiento interno.

Empecemos por lo más básico. ¿Qué es exactamente la criptografía?

## Definición de Criptografía

La criptografía moderna se puede considerar una rama de las matemáticas (_otra vez_) y la computación enfocada en encontrar y crear formas de convertir información clara y con algún significado en _información imposible de entender por entidades que no cuenten con la autorización para hacerlo, aunque la tengan en su poder_.

La palabra quiere decir literalmente **"escritura oculta"**. Y también se puede definir el campo como el encargado de encontrar algoritmos o procedimientos que permitan ocultar mensajes que sólo puedan ser descifrados por aquellos que tengan la llave.

La criptografía implica _esconder_ información explícitamente (los atacantes pueden saber que esa información está oculta e incluso hasta tener los mensajes ocultos en su poder), de manera que quien tenga la información correcta (que les concede la autorización) pueda obtener la información original desde los datos ininteligibles.

Este proceso de ocultar la información se llama **cifrado** (también se usa _encriptado_, como un barbarismo), mientras que el proceso de recuperar la información se llama **descifrado** (o _desencriptado_ 🙄).

Los procesos de cifrado modernos requieren generalmente **una llave o conjunto de llaves**, para realizar los procesos de cifrado y descifrado.

La criptografía es la base de todos los mecanismos de seguridad informática modernos, y a menudo se usa una conbinación de ellos para proteger un sistema.

## Uso en el software actual

## Esteganografía

La esteganografía es la técnica, relacionada con la criptografía, **de hacer la información invisible**, generalmente ocultándola dentro de otro tipo de información.

Con técnicas criptográficas comunes el que un atacante tenga disponible la información cifrada no hace necesariamente que nuestra información quede expuesta, a menos que el algoritmo criptográfico sea débil o el atacante tenga suficientes recursos para romperlo. En muchos casos incluso suponemos que los atacantes tienen acceso a esta información, como en el caso de la comunicación e internet en el que en cualquier parte de la red puede haber alguien interceptando nuestra información.

Las técnicas esteganográficas buscan ocultar completamente la información, hacerla invisible a través de ocultarla dentro de otros tipos de mensajes. En la antigüedad, por ejemplo en un libro que parecía hablar de magia, se ocultó un tratado acerca de criptografía y esteganografía, que sólo fue revelado hasta que se encontró la llave correcta.

Con la llegada de los medios digitales, en la que todo puede ser representado por medio de bits, en realidad se puede ocultar información de cualquier tipo en cualquier otro tipo de mensajes, pero se siguen usando medios físicos.

## Conclusión

Aprender criptografía puede darte una buena ventaja. 

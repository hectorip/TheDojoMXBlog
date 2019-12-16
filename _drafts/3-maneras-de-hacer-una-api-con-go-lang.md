---
title: "3 maneras de hacer una API con Go Lang"
date: 2019-11-23
author: Héctor Patricio
tags:
categories: 
comments: true
excerpt: "Escribe aquí un buen resumen de tu artículo"
header:
  overlay_image: #image
---

Go es uno de los lenguajes de reciente creación más exitosos de los últimos tiempos. Ya hablamos de [por qué deberías aprenderlo](/2019/09/01/por-que-deberias-aprender-go.html).

Ahora hablemos de un caso de uso práctico: **úsalo para crear una API**. En este artículo nos enfocaremos en la parte de comunicación. La funcionalidad básica de tu API puede o no adaptarse completamente a Go (no es es tan fácil de escribir como un lenguaje dinámico como Python), pero definitivamente es un lenguaje excelente para crear interfaces de comunicación web, debido a su alto rendimiento y eficiencia.

Puedes ver algunas de las comparativas en los siguientes artículos:

- [Comparando el rendimiento de Go, NodeJS y Elixir](https://stressgrid.com/blog/benchmarking_go_vs_node_vs_elixir/). TL;DR: Go y Elixir llegana  manejar más de 100k conexiones sin ningún problema, Node empieza con problemas desde las 30k y el más eficiente en cómputo y memoria utilizda por mucho es Go.
- [Comparación de frameworks web ligeros](https://github.com/mroth/phoenix-showdown). Este artículo es un poco viejo, pero el resumen es que Gin (un framework web ligero de Go) es el que más peticiones soporta por segundo y con una consistencia excelente.

![Comparativa de microframworks Web](https://res.cloudinary.com/hectorip/image/upload/v1574629781/Screenshot_2019-11-24_15.09.25_ozqwcu.png)


Ahora sí, hablemos de tres (4) formas de crear una API sobre HTTP para tu próximo proyecto. Pero antes hablemos de una opción simple que no cubre muchos casos pero que se oye recomendada muchas veces.

## La biblioteca estándar

Cuando hice mi primer proyecto en Go, gran parte de la investigación sobre qué usar para crear un proyecto web apuntaba los paquetes nativos de Go son el camino.

Go tiene una biblioteca estándar que cubre muchas de las necesidades de un desarrollador moderno, si has programado en él podrás estar de acuerdo en que se siente como subirte en hombros de gigantes para programar, debido a que los que lo  diseñaron y construyeron son las mismas personas que sentaron las bases para los sistemas operativos modernos. _Imagínate cuánta experiencia tienen_.

En la biblioteca estándar podemos encontrar un paquete que se llama `net/http` con el que puedes hacer muy pocas líneas de código lo que único un servidor web (la base de tu API): recibir peticiones HTTP, procesarlas (mejor dicho: hacer que algúna otra pieza más de tu sistema la procese) y devolver una respuesta HTTP. El ciclo básico request-response.

Aquí hay un ejemplo:

```go
package main

import (
	"fmt"
	"net/http"
)

// Implementando un servidor HTTP básico, que responde con
func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe("localhost:8080", nil) // iniciando el servidor
}

// handler recibe la petición http y la procesa para devolver una respuesta http
func handler(response http.ResponseWriter, request *http.Request) {
	fmt.Fprintf(response, "Hola Go API's")
}
```
Si tu API es muy sencilla, expone muy pocas URL's y sabes que no requerirás mucho en campo de las peticiones HTTP (procesamiento de parámetros, manejo de rutas, etc.) la librería estándar es una solución excelente, pero para otros casos se queda un poco corta.

Por eso te presentamos las opciones más comunes y algunos ejemplos.

## Gorilla Web Toolkit

![Gorilla Web Toolkit logo](https://avatars2.githubusercontent.com/u/489566?s=200&v=4)

[Gorilla Toolkit](https://www.gorillatoolkit.org/) es una conjunto de herramientas para Go en web que entre otras cosas tiene un web router llamado Gorilla Mux que podríamos pensar como la parte principal de nuestro servidor web y que cubre la mayoría de funciones que la biblioteca estándar deja sin cubrir.

## Gin

Gin es un framework web para Go bastante completo que clama ser el más rápido de todos los frameworks web para Go.


## Beego

## Conclusión

Existen múltiples opciones para crear tu API en Go. Cada una tiene puntos específicos por los que podrías decidir usarla, pero en nuestra experiencia la que se adapta a la mayor cantidad de circunstancias es Gin, que además tiene más componentes que las demás. Esta es una opinión basada en los casos en los que lo hemos usado.
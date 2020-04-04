---
title: "Tres maneras de hacer una API con Go"
date: 2019-11-23
author: Héctor Patricio
tags: go apis beego gorilla-mux gin-go go-lang
comments: true
excerpt: "Exploramos tres formas en las que puedes crear una API con Go el lenguaje enfocado en la eficiencia de los programas permitiendo productividad para los programadores"
header:
  overlay_image: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1440/v1576986565/clint-adair-BW0vK-FA3eg-unsplash_iamab8.jpg
  teaser: https://res.cloudinary.com/hectorip/image/upload/c_scale,w_1440/v1576986565/clint-adair-BW0vK-FA3eg-unsplash_iamab8.jpg
  overlay_filter: rgba(0, 0, 0, 0.5)
---

Go es uno de los lenguajes modernos más usados. Ya hablamos de [por qué deberías aprenderlo](/2019/09/01/por-que-deberias-aprender-go.html).

Ahora hablemos de un caso de uso práctico: **úsalo para crear una API HTTP**. En este artículo nos enfocaremos en la parte de comunicación HTTP.

La funcionalidad básica de tu API puede o no adaptarse completamente a Go (no es es tan fácil de escribir como un lenguaje dinámico como Python), pero definitivamente es un lenguaje excelente para crear interfaces de comunicación web, debido a su alto rendimiento y eficiencia.

Puedes ver algunas de las comparativas en los siguientes artículos:

- [Comparando el rendimiento de Go, NodeJS y Elixir](https://stressgrid.com/blog/benchmarking_go_vs_node_vs_elixir/). TL;DR: Go y Elixir llegan a manejar más de 100k conexiones sin ningún problema, Node empieza con problemas desde 30k y el más eficiente en cómputo y memoria utilizada por mucho es Go.

- [Comparación de frameworks web ligeros](https://github.com/mroth/phoenix-showdown). Este artículo es un poco viejo, pero el resumen es que Gin (un framework web ligero de Go) es el que más peticiones soporta por segundo y con una consistencia excelente.

![Comparativa de micro-frameworks Web](https://res.cloudinary.com/hectorip/image/upload/v1574629781/Screenshot_2019-11-24_15.09.25_ozqwcu.png)

Hablemos de tres formas de crear una API sobre HTTP para tu próximo proyecto. Pero antes hablemos de una opción simple que no cubre muchos casos pero que se oye recomendada muchas veces.

## La biblioteca estándar

Cuando hice mi primer proyecto en Go, gran parte de la investigación sobre qué usar para crear un proyecto de una API web apuntaba a los **paquetes nativos** de Go.

Go tiene una biblioteca estándar que cubre **muchas** de las necesidades de un desarrollador moderno. Si has programado en él podrás estar de acuerdo en que se siente como subirte en hombros de gigantes, debido a que los que lo diseñaron y construyeron son _las mismas personas que sentaron las bases para los sistemas operativos modernos_. Imagínate cuánta experiencia tienen.

En la biblioteca estándar podemos encontrar un paquete que se llama `net/http` con el que puedes hacer, en muy pocas líneas de código, un servidor web con ruteo sencillo (la base de tu API). Puedes recibir peticiones HTTP, procesarlas y devolver una respuesta HTTP. El ciclo básico request->response.

Aquí hay un ejemplo:

```go
package main

import (
	"fmt"
	"net/http"
)

// Implementando un servidor HTTP
func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe("localhost:8080", nil) // iniciando el servidor
}

// handler recibe la petición http y la procesa para devolver una respuesta http
func handler(response http.ResponseWriter, request *http.Request) {
	fmt.Fprintf(response, "Hola Go API's") // Falta responder JSON
}
```

Si tu API es **muy** sencilla, expone muy pocas URLs y sabes que no requerirás mucho en campo de las peticiones HTTP (procesamiento de parámetros, manejo de rutas, etc.) la biblioteca estándar es una solución excelente, pero para otros casos se queda un poco corta.

Por eso te presentamos las opciones más comunes y algunos ejemplos.

## Gorilla Web Toolkit

![Gorilla Web Toolkit logo](https://avatars2.githubusercontent.com/u/489566?s=200&v=4){: .align-center}

[Gorilla Toolkit](https://www.gorillatoolkit.org/) es una conjunto de herramientas para web que, entre otras cosas, tiene un web router llamado **Gorilla Mux** que es la parte principal del servidor web y que cubre la mayoría de funciones que la biblioteca estándar deja sin cubrir:

## Gin



Gin es un framework web para Go bastante completo que clama ser el más rápido de todos los frameworks web para Go.
## Beego

## Conclusión

Existen múltiples opciones para crear tu API en Go. Cada una tiene puntos específicos por los que podrías decidir usarla, pero en nuestra experiencia la que se adapta a la mayor cantidad de circunstancias es Gin, que además tiene más componentes que las demás.


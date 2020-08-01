---
title: "Cuatro formas de hacer una API con Go"
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

La funcionalidad básica de tu API puede o no adaptarse completamente a Go (no es es tan fácil de escribir como un lenguaje dinámico como Python), pero definitivamente es un **lenguaje excelente** para crear interfaces de comunicación web, debido a su alto rendimiento y eficiencia.

Puedes ver algunas de las comparativas en los siguientes artículos:

- [Comparando el rendimiento de Go, NodeJS y Elixir](https://stressgrid.com/blog/benchmarking_go_vs_node_vs_elixir/). TL;DR: Go y Elixir llegan a manejar más de 100k conexiones sin ningún problema, Node empieza con problemas desde 30k y el más eficiente en cómputo y memoria utilizada _por mucho_ es **Go**.

- [Comparación de frameworks web ligeros](https://github.com/mroth/phoenix-showdown). Este artículo es un poco viejo, pero el resumen es que Gin (un framework web ligero de Go) es el que más peticiones soporta por segundo y con una consistencia excelente.

![Comparativa de micro-frameworks Web](https://res.cloudinary.com/hectorip/image/upload/v1574629781/Screenshot_2019-11-24_15.09.25_ozqwcu.png)

Hablemos de tres formas de crear una API sobre HTTP para tu próximo proyecto. Pero antes hablemos de una opción simple que no cubre muchos casos pero que se oye recomendada por todo internet.

## La biblioteca estándar

Cuando hice mi primer proyecto en Go, gran parte de la investigación sobre qué usar para crear un proyecto de una API web apuntaba a los **paquetes nativos** de Go.

Go tiene una biblioteca estándar que cubre **muchas** de las necesidades de un desarrollador moderno. Si has programado en él podrás estar de acuerdo en que se siente como subirte en hombros de gigantes, debido a que las personas que lo diseñaron y construyeron son _las mismas personas que sentaron las bases para los sistemas operativos modernos_. Imagínate cuánta experiencia tienen.

En la biblioteca estándar podemos encontrar un paquete que se llama `net/http` con el que puedes hacer, un servidor web con ruteo sencillo (la base de tu API) **con muy pocas líneas de código**. Puedes recibir peticiones HTTP, procesarlas y devolver una respuesta HTTP. El ciclo básico request -> response.

Aquí hay un ejemplo:

```go
package main

import (
	"fmt"
	"net/http"
)

// Implementando rutas HTTP
func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe("localhost:8080", nil) // iniciando el servidor
}

// handler recibe la petición http y la procesa para devolver una respuesta http
func handler(response http.ResponseWriter, request *http.Request) {
	fmt.Fprintf(response, "Hola Go API's") // Falta responder JSON
}
```

Si tu API es sencilla, expone pocas URLs y sabes que no requerirás mucho en campo de las peticiones HTTP (procesamiento de parámetros, manejo de rutas, etc.) la biblioteca estándar es una solución buena, pero para otros casos se queda un poco corta, ya que tendrías que implementar varias cosas a mano.

Su uso es sencillo como acabas de ver. Usar un framework web tiene el costo de agregar complejidad a **cambio de funcionalidades que no tienes que desarrollar tú**. Pero aquí te compartimos un artículo en el que un experto hablá de por qué _él_ prefiere no usar frameworks: [Why I Don't Use Go Web Frameworks](https://medium.com/code-zen/why-i-don-t-use-go-web-frameworks-1087e1facfa4).

Por eso te presentamos las opciones más comunes y algunos ejemplos.

## Gorilla Web Toolkit

![Gorilla Web Toolkit logo](https://avatars2.githubusercontent.com/u/489566?s=200&v=4){: .align-center}

[Gorilla Toolkit](https://www.gorillatoolkit.org/) es un conjunto de herramientas para web que, entre otras cosas tiene:

- Un router más completo que el de la biblioteca estándar: *Gorilla Mux*. Es compatible con el tipo de dato nativo de Go para las peticiones. Además incluye:
  - Sub-routers (para mejor organización)
  - Reversión de URL's (generar URL's a partir del nombre)
  - Matches complejos
- Middlewares: logging, compresión, recuperación
- Manejo de sesiones con cookies seguras
- Implementación de Websockets y RPC
- Conversión de valores de entrada en `struct` de Go

Gorilla Toolkit **no es un framework**, puedes usar cada de sus herramientas por separado, como las vayas necesitando. Así que puede empezar con la librería estándar y agregar lo que necesitas de Gorilla poco a poco.

Aquí tienes un ejemplo muy básico usando **mux**:

```go

import "gorilla/mux"


```

## Gin

[Gin](https://github.com/gin-gonic/gin)
Gin es un framework web para Go bastante completo que clama ser el más rápido de todos los frameworks web para Go.

## Beego


[Beego](https://beego.me/)

## Echo

[Echo](https://echo.labstack.com/)

## Conclusión

Existen múltiples opciones para crear tu API en Go. Hay para escoger dependiendo de tus gustos y de las prioridades de tu proyecto.
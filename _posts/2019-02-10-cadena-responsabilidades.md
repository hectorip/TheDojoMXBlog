---
title: "cadena-responsabilidades"
date: 2019-02-10
author: Esteban Galicia
tags: python patrones SOLID Responsability Chain
comments: true
excerpt: "Los patrones de diseño como eje central en el desarrollo de software"
header:
  image: #image
---

# Cadena de responsabilidad

Hace unas semanas me enfrente a un tema de procesar un mensaje de un usuario y darle tratamiento por medio de un algoritmo de Natrual Language Processing. Antes de pasar el mensaje por el set de algoritmos apropiados hay que darle una serie de tratamientos:

 1. Eliminar los acentos y sólo dejar en ASCII el mensaje.
 2. Pasar el mensaje a lowercase.

A primera luz, un código que puede fácilmente satisfacer es:
```python
message = "Dios bendiga a los héroes que nos dieron el internet."
message = message.lower()
message = message.replace("á","a").replace("é","e") \
    .replace("í","i").replace("ó","o").replace("ú","u")
print(message)
# dios bendiga a los heroes que nos dieron el internet.
```
Funcionó, se cumplió el objetivo.

El problema sobrevino en el momento que los algoritmos posteriores requieren más modificaciones en la cadena original.
Poco a poco se fue agregando y agregando código para tareas como eliminar emojis, eliminar signos de puntuación, contraer palabras como *hooooooola* en *hola* y en el futuro no se sabe que más cosas habrá que hacer a la cadena original, pueden ser cosas tan diversas como "A cada cadena que se procese quiero que se quede un historial de la cadena original", en ese momento hay que ir a reescribir código quebrantando el principio [****open/closed****](https://en.wikipedia.org/wiki/Open–closed_principle) "_software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification_".

## El salvador

El patrón de diseño *Chain of responsibility* como premisa principal es que mas de una entidad de software pueda atender una petición.

```python
def to_lower(message=""):
    if not isinstance(message,str):
        raise ValueError("Message is not a string")
    return message.strip().lower()

def to_ascii(message):
    if not isinstance(message,str):
        raise ValueError("Message is not a string")
    message = message.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    return message

def to_disk(message):
    FILENAME = "historial.log"
    if not isinstance(message,str):
        raise ValueError("Message is not a string")
    with open(FILENAME,"a",encoding="UTF-8") as fp:
        fp.write(f"{message}\n")
    return message


class Pipe:
    def __init__(self,message):
        self._message = message
        self.processors = []

    def add_process(self,process_function):
        self.processors.append(process_function)

    def run(self):
        for process in self.processors:
            self._message = process(self._message)
        return self._message

pipe=Pipe("Dios bendiga a los héroes que nos dieron el internet.")
pipe.add_process(to_disk)
pipe.add_process(to_lower)
pipe.add_process(to_ascii)
new_message=pipe.run()
print(new_message)

```
El código anterior es un código más profesional, más mantenible ya que cumplimos con el principio open/close y de paso de resposnabilidad única.

Podemos ir agregando funciones de procesamiento de manera más legible, y también podemos quitarlas a voluntad dado que el nivel de acoplamiento es muy bajo. A todo ésto hay que añadir la ventaja de facilidad al escribir test unitarios que da pie para el CI/CD.

Se puede ver que es una sobre ingeniería para algo tan sencillo, sin embargo puede proveer un ejemplo claro/práctico de la aplicación del patrón.

Saludos y no dudes en ejercer tu derecho de réplica :) , discutamos un poco al respecto :D

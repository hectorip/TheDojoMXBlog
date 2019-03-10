---
title: "Producción y desarollo en Django"
date: 2019-03-09
author: Esteban Galicia
tags: Django producción deploy despliegue
categories: 
comments: true
excerpt: "Una manera para manejar producción y desarrollo sin tanto esfuerzo."
header:
  overlay_image: https://res.cloudinary.com/dg89awi0p/image/upload/v1552160611/rawpixel-1135756-unsplash.jpg
  teaser: https://res.cloudinary.com/dg89awi0p/image/upload/v1552160611/rawpixel-1135756-unsplash.jpg
---


# Para no salir herido al combinar desarrollo y producción en Django.


> Se usará Django >= 2.0

> Se usará Python >= 3.6

## Problemática.

Mientras desarrollba en Django, me encontré con un problema,  requería hacer múltiples pruebas con el ORM para generar consultas complejas a base de datos.
Para hacer la prueba se ejecuta:
```python
python manage.py shell
```
Con lo que se abrirá una consola de Python, en dicha consola se puede importar un modelo y con ese modelo hacer las pruebas requeridas.

```python
from blog.models import Post

all_posts = post.objects.all()
```

Todo opera bien hasta que debemos importar múltiples modelos, al modificar un modelo se debe detener la consola `Ctrl+C` y ejecutarla de nueva cuenta, y de nueva cuenta cargar todos los modelos.

A fin de no perder tiempo cargando los modelos en cada detención de la consola se opta por usar una herramienta llamada [`django-extensions`](https://django-extensions.readthedocs.io/en/latest/)

La instalo en mi proyecto usando:

```sh
pip install 
```

y agregándola a mis apps

```python
INSTALLED_APPS = (
    ...
    'django_extensions',
)
```

Hecho eso, puedo ejecutar una consola donde se cargan ya todos los modelos listos para hacer consultas a la base de datos. Traducción: ahorramos mucho tiempo. 

```sh
python manage.py shell_plus
```

El siguiente problema que hallé es que esta herramienta no debe estar en producción, solo es para propósitos de desarrollo.

Pero, ¿Qué hacer?, ¿La agrego y quito de `INSTALLED_APPS` manualmente a cada push que haga en  mi repositorio?, esa estrategia es muy propensa al error y a la hora de desplegar podemos tener un error por no tener instalada la herramienta.

La forma que me ha gustado más hasta ahora es hacer uso del paquete `sys` de Python, con el que puedo con uno de sus módulos leer los argumentos con los que se ejecuta la aplicación de Django.

```python
import sys
.
.
.
DEBUG_COMMAND = set('shell_plus', 'shell', 'runserver')

DJANGO_RUN_ARGS = set(sys.argv)

if len(DJANGO_RUN_ARGS.intersection(DEBUG_COMMAND))>0:
    INSTALLED_APPS.append('django_extensions')

```

En `DEBUG_COMMAND` se definen los comandos que se ejecutan solo en desarrollo, hay que recordar que `runserver` se agrega también en el set dado que NO se debe pasar a producción la ejecución de Django por medio de dicho mecanismo, para producción lo correcto es pasarlo con un WSGI server diseñado para producción como [guinicorn](https://gunicorn.org).

`DJANGO_RUN_ARGS` es la variable que guardará los argumentos con los que se ejecuta Django.

Ambas variables son un set, así es sencillo comprobar que argumentos serán catalogados como de desarrollo por medio de la intersección de ambas variables, el que haya elementos en la intersección implica que por lo menos uno de los argumentos se cataloga como de desarrollo.

Y bueno, solo falta agregar que después de la condicional se pueden agregar tanto código como se requiera.

No olvides comentar tu experiencia usando esta estrategia para manejar desarrollo y producción en Django.
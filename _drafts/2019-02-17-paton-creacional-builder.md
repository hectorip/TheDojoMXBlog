---
title: "paton creacional builder"
date: 2019-02-17
author: Esteban Galicia
tags:
comments: true
excerpt: ""
header:
  image: #image
---


#### Propósito
Permitir generar objetos complejos


Al hacer algún proyecto nos enfrentamos a la creación de instancias muy a menudo, los argumentos en el constructor de dichas instancias pueden crecer.



```python
class Order:
  def __init__(self, main_meal, second_meal, soda):
    self.main_meal = main_meal
    self.second_meal = second_meal
    self.soda = soda


# One order
order_1 = Oder("Hamburger","Chips","Lemon")
```

Hasta aquí el trabajo está hecho y pasan 3 años.
Ahora, después de ese tiempo nos piden ampliar el menú, también se darán postres, bebidas calientes, y paquetes de comida de cumpleaños.

```python
class Order:
  def __init__(self, main_meal, second_meal, soda, dessert, hot_drink, birthday_package):
    self.main_meal = main_meal
    self.second_meal = second_meal
    self.soda = soda
    self.dessert = dessert
    self.birthday_package = birthday_package


# Birthday package
order_1 = Oder(None, None, None, None, "ultra cheese")


# Another order
order_2 = Order("Hotdog" ,None ,"Orange" ,"Sunday" ,None)
```
Ya está ,problema resuelto, ¿Verdad? (cubre la clase de tu vista y dí que significa cada parámetro posicional del inicializador).
La clase se comienza a utilizar en múltiples módulos y paquetes del proyecto, hay muchos bugs por simplemente no recordar el orden correcto de los parámetros.

Hagamos parámetros nombrados y valores por defecto:

```python

class Order:
  def __init__(self, main_meal = None, second_meal = None, soda = None, dessert = None, hot_drink = None, birthday_package = None):
    self.main_meal = main_meal
    self.second_meal = second_meal
    self.soda = soda
    self.dessert = dessert
    self.birthday_package = birthday_package


# Birthday package
order_1 = Oder(birthday_package = "ultra cheese")


# Another order
order_2 = Order(main_meal = "Hotdog" ,soda = "Orange" ,dessert = "Sunday")

```
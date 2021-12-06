# Definiciones

Módulo

Es cualquier archivo de Python. Generalmente, contiene código que puede reutilizarse.


Paquete

Es una carpeta que contiene un conjunto de módulos, siempre posee el archivo "__init__.py"

ejemplo-modulo-paquetes.PNG


## ¿Qué son los tipados?

Son una clasificación de los lenguajes de programación, dependiendo de cómo trata a sus tipos primitivos se pueden clasificar en:

* Estático. Son los que levantan los errores de tipo en tiempo de compilación.

``` java
String str = "Hello" // Variable tipo String
srt = 5 // ERROR: no se puede convertir un tipo de dato en otro de esta forma.
```

* Dinámico. Son los que levantan los errores de tiepo en tiempo de ejecución.

``` python
str = "Hello" # Variable tipo String
str = 5 # La variable ahora es de tipo Entero
```

* Tipado débil.

```

```

* Tipado fuerte.

``` python
x = 1
y = "2"
z = x + y # ERROR: NO podemos hacer esta operacion con tipos de datos distintos entre sí
```
# Tipos de Datos Abstractos

En Python todo es un objeto y tiene un tipo. Representación de datos y foras de interactuar con ellos.

Formas de interactuar con un objeto.

* Creación.
* Manipulación.
* Destrucción.

Ventajas.

* Decomposición.
* Abstracción.
* Encapsulación.

Estructura para las Clases

```python

# Definición de Clase

class <nombre_de_la_clase>(<super_clase>):

    def __init__(self, <params>): # Constructor
        <expresion>

    def <nombre_del_metodo>(self, <params>):
        <expresion>

```

Ejemplo real.

```python
# Definicion

Class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'

# Uso
>>> david = Persona('David', 35)
>>> erika = Persona('Erika', 32)

>>> david.saluda(erika)
'Hola Erika, me llamo David'

```

## Instancias

La clase es un molde, a los objetos creados se les conoce como instancias. Cuando se crea una instancia, se ejecuta el método __init__. TOdos los métodos de una clase reciben implícitamente como primer parámetro **self**.

## Decomposición

Consiste en partir un problema en problemas más pequeños.Las clases permiten crear mayores abstracciones en forma de componentes. Cada clase se encarga de una parte del problema y el programa se vuelve más f+ácil de mantener.

## Abstracción

Hace referencia a la ocultación de la complejidad intrínseca de una aplicación al exterior, centrándose sólo en como puede ser usado.


## Decoradores

Son una forma sencilla de llamar **funciones de orden mayor**, es decir, funciones que toman otra función como parámetro y/o retornan otra función como resultado. Un decorador añade capacidades a una función sin modificarla.

ES un closure que tiene una funcionalidad adicional

### Funciones como objetos de primera-clase

En Python las funciones son objetos que pueden se pasados y utilizados como argumentos al igual que cualquier otro objeto.

```python
def presentarse(nombre):
    return f"Me llamo {nombre}"

def estudiemos_juntos(nombre):
    return f"Hey {nombre}, aprendamos Python"

def consume_funciones(funcion_entrante):
    return funcion_entrante("David")
```

```python
def decorador(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura

def saludo():
    print('Hola!')

saludo()
# Outout
# Hola!

saludo = decorador(saludo)
saludo()
# Output
# Esto se añade a mi función original
# Hola!
```


Implementación del decorador
```python
def decorador(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura

@decorador
def saludo():
    print('Hola!')

saludo()
```

## Generador

Es una función que guarda un estado

## Polifor
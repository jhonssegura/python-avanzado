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

```python
# Generator Expression

my_list = [0,1,4,7,9,10]

my_second_list = [x*2 for x in my_list] # List Comprehension
my_second_gen = (x*2 for x in my_list) # Generator Expression
```

Es más sencillo y con todoas las ventajas de un iterador.

## Sets

Son una colección desordenada de elementos únicos e inmutables.

```python
my_set = {3,4,5}
print("my_set =", my_set)

my_set2 = {"Hola", 23.3, False, True}
print("my_set2 =", my_set2)

my_set3 = {3, 3, 2}
print("my_set3 =", my_set3)

my_set4 = {[1, 3, 4], 4}
print("my_set4 =", my_set4)
```

Convertir estructuras de datos en sets

```python
my_list = [1,1,2,3,4,4,5]
my_set = set(my_list)
print(my_set)

my_tuple = ("Hola", "Hola", "Hola", 1)
my_set2 = set(my_tuple)
print(my_set2)

# Output
# {1,2,3,4,5}
# {'Hola', 1}
```

Añadir elementos a un set

```python
my_set = {1,2,3}
print(my_set)

# Añadir un elemento
my_set.add(4)
print(my_set)

# Añadir múltiples elementos
my_set.update([1,2,5])
print(my_set)

# Añadir múltiples elementos
my_set.update((1,7,2), {6,8})
print(my_set)

# Output
# {1,2,3}
# {1,2,3,4}
# {1,2,3,4,5}
# {1,2,3,4,5,6,7,8}
```

Eliminar elementos a un set

```python
my_set = {1,2,3,4,5,6,7}
print(my_set)

# Borrar un elemento existente
my_set.discart(1)
print(my_set)

# Borrar un elemento existente
my_set.remove(2)
print(my_set)

# Borrar un elemento inexistente
my_set.discard(10)
print(my_set)

# Borrar un elemento inexistente
my_set.remove(12)
print(my_set)

# Output
# {1,2,3,4,5,6,7}
# {2,3,4,5,6,7}
# {3,4,5,6,7}
# {3,4,5,6,7}
# KeyError
```

Borrado de elemento aleatorio o todos los elementos.

```python
my_set = {1,2,3,4,5,6,7}
print(my_set)

# Borrar un elemento aleatorio
my_set.pop()
print(my_set)

# Limpiar el set
my_set.clear()
print(my_set)

#Output
# {1,2,3,4,5,6,7}
# {2,3,4,5,6,7}
# set()
```

Unión entre sets

```python
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 | my_set2
print(my_set3)

# Output
# {3,4,5,6,7}
```

Intersección entre sets

```python
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 & my_set2
print(my_set3)

# Output
# {5}
```

Diferencia entre sets

```python
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 - my_set2
print(my_set3)

my_set4 = my_set2 - my_set1
print(my_set4)

# Output
# {3,4}
# {6,7}
```

Diferencia simétrica

```python
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 ^ my_set2
print(my_set3)

# Output
# {3,4,6,7}
```

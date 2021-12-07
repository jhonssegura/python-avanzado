# Definiciones

## Módulo

Es cualquier archivo de Python. Generalmente, contiene código que puede reutilizarse.


## Paquete

Es una carpeta que contiene un conjunto de módulos, siempre posee el archivo "__init__.py"

ejemplo-modulo-paquetes.PNG


## ¿Qué son los tipados?

Son una clasificación de los lenguajes de programación, dependiendo de cómo trata a sus tipos primitivos se pueden clasificar en:

* **Estático.** Son los que levantan los errores de tipo en tiempo de compilación.

``` java
String str = "Hello" // Variable tipo String
srt = 5 // ERROR: no se puede convertir un tipo de dato en otro de esta forma.
```

* **Dinámico.** Son los que levantan los errores de tipo en tiempo de ejecución.

``` python
str = "Hello" # Variable tipo String
str = 5 # La variable ahora es de tipo Entero
```

* **Tipado débil.** Son los que tratan con menos severidad a los datos de diferentes tipos.

``` javascript
const x = 1;
const y = "2";
const z = x + y; // 12
```

* **Tipado fuerte.** Son los que tratan con mayor severidad a los datos de diferentes tipos.

``` python
x = 1
y = "2"
z = x + y # This will fail
```

## Tipado Estático en Python
A partir de la versión 3.6 de Python, se puede especificar el tipo de dato de manera estática.

```python
a: int = 5
print(a)

b: str = 'Hola'
print(b)

c: bool = True
print(c)

def suma (a: int, b: int) -> int:
    return a + b

print(suma(1,2)) # Devolvera un entero7

print(suma('1', '2')) # Devolvera 12 
```

En los casos se desee trabajar con estructuras de datos mutables.

```python
from typing import Dict, List

positives: List[int] = [1, 2, 3, 4, 5]

# Diccionario
users: Dict[str, int] = {
    'argentina': 1,
    'mexico': 34,
    'colombia': 45,
}

# Lista
countries: List[Dict[str, str]] = [
    {
        'name': 'Argentina',
        'people': '450000'.
    },
    {
        'name': 'México',
        'people': '9000000',
    },
    {
        'name': 'Colombia',
        'people': '99999999999',
    },
]
```

En el caso se desee trabajar con estructuras de datos inmutables.

```python
from typing import Tuple

numbers: Tuple[int, float, int] = (1, 0.5, 1)
```

Casos más complejos.

```python
from typing import Tuple, Dict, List

CoordinatesType = List [Dict[str, Tuple[int, int]]]

coordinates: CoordinatesTYpe = [
    {
        'coord1': (1, 2),
        'coord2': (3, 5)
    },
    {
        'coord1': (0, 1),
        'coord2': (2, 5)
    },
]
```

El Módulo **mypy** nos permite indicar a Python que marque error cuando se envie un tipo de dato diferente al tipo que se definió. 

## Scope

Una variable solo está disponible dentro de la región donde fue creada.


### Local Scope

Corresponde al ámbito de una función, donde las variables van a ser accesibles únicamente en esta región y no serán visibles en otras.

```python
def my_func():
y = 5
print(y)

my_funct() # 5

```

### Global Scope. 

Al declarar una o más variables en esta región, podrán ser accesibles desde cualquier parte del código.

```python
y = 5

def my_func():
print(y)

def my_other_func():
print(y)


my_func() # 5
my_other_func() # 5
```

## Closures

Son una forma de acceder a variables de otros **scopes** a través de una **nested function**, esta recuerda el valor que imprime aunque a la hora de ejecutarla no esté dentro de su alcance.  

Reglas para encontrar un Closure.

* Debemos tener una nested function.

* La nested function debe referenciar un valor de un scope superior.

* La función que envuelve a la nested function también debe retornarla .

```python
def main():
    a = 1
    def nested():
        print(a)
    
    return nested

my_func = main()
my_func()

# Retorna el valor (1)
```

Aunque se elimine al scope, se mantiene el valor. 

```python
def main():
    a = 1

    def nested():
        print(a)

    return nested

my_func = main()
my_func()

del(main)

my_func()

# Retorna dos veces el valor (1)
```

Ejemplo implementación.

```python
def make_multiplier(x):

    def multiplier(n):
        return x * n

    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))

# Output
# 30
# 20
# 80
```

### ¿Dónde aparecen los closures?

* Cuando se tiene una clase que tiene solo un método, se aplican closures para hacerla más elegante.

* Cuando se trabajan con decoradores.


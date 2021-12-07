# Funciones

## Args y Kwargs

### Uso de *args

Permiten definir funciones cuyo número de argumentos es variable.


```python
def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s

suma(1, 3, 4, 2)
# Salida 10

suma(1, 1)
# Salida 2
```

Su uso es totalmente arbitrario, por lo cual puede ser llamado cuando se desee.

### Uso de **Kwargs

Nos permite dar un nombre a cada argumento de entrada, pudiendo acceder a ellos dentro de la función a través de un diccionario.

## Recursividad

Es un concepto que permite resolver problemas o tareas donde las mismas pueden ser divididas en subtareas cuya funcionalidad es la misma. Dado que los subproblemas a resolver son de la misma naturaleza, se puede usar la misma función para resolverlos.

Una función recursiva es aquella que está definida en función de sí misma, por lo que se llama repetidamente a si misma hasta llegar a un punto de salida.

Posee dos seciones de código claramente divididas.

* La función se llama a sí misma.
* Tiene que existis siempre una condición en la que la función retorna sin volver a llamarse.


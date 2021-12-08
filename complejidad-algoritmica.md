# Complejidad Algorítmica

## Aproximaciones

* Cronometrar el tiempo en el que corre un algoritmo.

* Contar los pasos con una medida abstracta de operación.

* Contar los pasos conforme nos aproximamos al infinito.

## Crecimiento asintótico

* No importan variaciones pequeñas.
* EL enfoque se centra en lo que pasa conforme el tamaño del problema se acerca al infinito.
* Mejor de los casos, promedio, peor de los casos.
* Big O.
* Nada más importa el término de mayor tamaño.

```python
# Ley de la suma

def f(n):
    for i in range(n):
        print(i)


    for i in range(n):
        print(i)

# O(n) + O(n) = O(n+n) = O(2n) = O(n)
```

```python
# Ley de la multiplicación

def f(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# O(n) * O(n) = O(n*n) = O(n²)
```

```python
# Recursividad múltiple

def fibonacci(n):

    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 1)

# O(2**n)
```

## Clases de Complejidad Algorítmica

* O(1) Constante
* O(n) Lineal
* O(log n) Logarítmica
* O(n log n) log lineal
* O(n**2) Polinomial
* O(2**n) Exponencial

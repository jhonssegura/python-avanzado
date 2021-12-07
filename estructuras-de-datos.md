# Estructuras de Datos 

## Iteradores

Son una estructura de datos para guarar datos infinitos.

```python
# Creando un iterador

my_list = [1,2,3,4,5,6]
my_iter = iter(my_list)

# Iterando un iterador

print(next(my_iter))

# Cuando no quedan datos, la excepción StopIteration es elevada
```

```python
# Creando un iterador

my_list = [1,2,3,4,5,6]
my_iter = iter(my_list)

# Iterando un iterador

while True: # Indicamos que se ejecute infinitamente
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break
```


import random

def busqueda_lineal(lista, objetivo, iter_bin=0):
    match = False
    
    for elemento in lista: # 0(n)
        
        iter_bin+=1
        if elemento == objetivo:
            match = True
            break

    return (match, iter_bin)

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    (encontrado, iter_bin) = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Iteraciones busqueda binaria: {iter_bin}')
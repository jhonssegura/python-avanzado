

def morral(tamano_normal, pesos, valores, n):

    if n == 0 or tamano_normal == 0:
        return 0

    if pesos[n - 1] > tamano_normal:
        return morral(tamano_morral, pesos, valores, n - 1)

    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
            morral(tamano_morral, pesos, valores, n - 1))

if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 50 
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado) # Debe devolver 220
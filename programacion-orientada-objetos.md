# Programación Orientada a Objetos

## Polimorfismo.

Objetos de diferentes clases pueden ser accedidos utilizando la misma interfaz, mostrando un comportamiento distinto según cómo sean accedidos.

## Herencia

Es un proceso mediante el cual se puede crear una clase hija que hereda a una clase padre, compartiendo sus métodos y atributos. La clase hija puede sobreescribir los métodos o atributos, o incluso definir unos nuevos.

## Encapsulación

Permite agreupar datos y su comportamiento. Controla el accesi a dischos datos. Previene modificaciones no autorizadas.

### Getters



### Setters



```python
class CasillaDeVotación

    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self.__pais}')


>>> casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])
>>> casilla.region
# Output
# None

>>> casilla.region = 'Ciudad de Mexico'
>>> casilla.region
# Output
# 'Ciudad de Mexico'
```

## Herencia

Permite modelar una jeraquía de clases. Permite compartir comportamiento común en la jerarquía. Al padre se le conoce como superclase y al hijo como subclase.


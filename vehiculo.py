from abc import ABC, abstractmethod


class Vehiculo(ABC):
    def __init__(self, marca: str, modelo: str, precio_base: float):
        if precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que 0.")
        self.__marca = marca
        self.__modelo = modelo
        self.__precio_base = precio_base

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def precio_base(self):
        return self.__precio_base

    @abstractmethod
    def impuesto(self) -> float:
        pass

    def precio_final(self) -> float:
        return self.__precio_base + self.impuesto()

    def ficha(self) -> str:
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}"

    def __str__(self) -> str:
        return f"{self.ficha()} - Precio Final: ${self.precio_final():,.2f}"

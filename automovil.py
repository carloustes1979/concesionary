from vehiculo import Vehiculo


class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, precio_base: float, puertas: int):
        super().__init__(marca, modelo, precio_base)
        if puertas <= 0:
            raise ValueError("El número de puertas debe ser mayor que 0.")
        self.__puertas = puertas

    @property
    def puertas(self):
        return self.__puertas

    def impuesto(self) -> float:
        impuesto = 0.08 * self.precio_base
        if self.__puertas == 5:
            impuesto -= 0.01 * self.precio_base
        return impuesto

    def ficha(self) -> str:
        return f"Automóvil - {super().ficha()}, Puertas: {self.__puertas}"

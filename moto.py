from vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, precio_base: float, cc: int):
        super().__init__(marca, modelo, precio_base)
        if cc <= 0:
            raise ValueError("El cilindraje debe ser mayor que 0.")
        self.__cc = cc

    @property
    def cc(self):
        return self.__cc

    def impuesto(self) -> float:
        if self.__cc <= 250:
            return 0.05 * self.precio_base
        else:
            return 0.09 * self.precio_base

    def ficha(self) -> str:
        return f"Moto - {super().ficha()}, Cilindraje: {self.__cc}cc"

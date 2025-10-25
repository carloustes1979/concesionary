from automovil import Automovil
from moto import Moto
from tabulate import tabulate


def main():
    vehiculos = [
        Automovil("Toyota", "Corolla", 85000, 5),
        Automovil("Mazda", "3", 90000, 4),
        Moto("Yamaha", "XTZ", 15000, 250),
        Moto("Kawasaki", "Ninja", 35000, 600)
    ]

    tabla = []
    total_inventario = 0

    for v in vehiculos:
        tabla.append([
            v.ficha(),
            f"${v.precio_base:,.2f}",
            f"${v.impuesto():,.2f}",
            f"${v.precio_final():,.2f}"
        ])
        total_inventario += v.precio_final()

    print(tabulate(tabla, headers=["Vehículo", "Precio Base", "Impuesto", "Precio Final"], tablefmt="grid"))
    print(f"\nTotal del inventario: ${total_inventario:,.2f}")


if __name__ == "__main__":
    main()

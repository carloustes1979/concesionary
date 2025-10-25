# 🚗 Concesionario POO en Python

Mini sistema de concesionario que aplica **encapsulamiento, herencia, abstracción y polimorfismo**.

## 🧩 Estructura de clases
- `Vehiculo` (abstracta)
- `Automovil` (hereda de Vehiculo)
- `Moto` (hereda de Vehiculo)
- `concesionario_main.py` (punto de entrada)

## ⚙️ Instalación

```bash
pip install -r requirements.txt
```

## ▶️ Ejecución

```bash
python concesionario_main.py
```

## 📋 Salida esperada

| Vehículo | Precio Base | Impuesto | Precio Final |
|-----------|--------------|-----------|---------------|
| Automóvil - Marca: Toyota, Modelo: Corolla, Puertas: 5 | $85,000.00 | $5,950.00 | $90,950.00 |
| Automóvil - Marca: Mazda, Modelo: 3, Puertas: 4 | $90,000.00 | $7,200.00 | $97,200.00 |
| Moto - Marca: Yamaha, Modelo: XTZ, Cilindraje: 250cc | $15,000.00 | $750.00 | $15,750.00 |
| Moto - Marca: Kawasaki, Modelo: Ninja, Cilindraje: 600cc | $35,000.00 | $3,150.00 | $38,150.00 |

**Total del inventario:** `$242,050.00`

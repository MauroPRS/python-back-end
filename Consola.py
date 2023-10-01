from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self, marca, voltaje, eficiencia, precio, nombre, version, lite):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.nombre = nombre
        self.version = version
        self.lite = lite

    def calcular_descuento(self):
        descuento_eficiencia = super().calcular_descuento()
        if self.lite:
            return descuento_eficiencia + 0.05
        else:
            return descuento_eficiencia

    def mostrar_caracteristicas(self):
        print("Características de la Consola:")
        print(f"Marca: {self.marca}")
        print(f"Voltaje: {self.voltaje}")
        print(f"Eficiencia: {self.eficiencia}")
        print(f"Precio: {self.precio}")
        print(f"Nombre: {self.nombre}")
        print(f"Versión: {self.version}")
        print(f"Lite: {self.lite}")
        print(f"Descuento aplicado: {self.calcular_descuento() * 100}%")
        print(f"Valor total luego del descuento: {self.calcular_precio_con_descuento()}")

    


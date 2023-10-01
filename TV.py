from Tecnologia import Tecnologia
class TV(Tecnologia):
    def __init__(self, marca, voltaje, eficiencia, precio, tamano):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.tamano = tamano

    def mostrar_caracteristicas(self):
        print(f"Marca: {self.marca}")
        print(f"Voltaje: {self.voltaje}")
        print(f"Eficiencia: {self.eficiencia}")
        print(f"Precio: {self.precio}")
        print(f"Tamaño: {self.tamano}")
        print(f"Descuento aplicado: {self.calcular_descuento() * 100}%")
        print(f"Valor total luego del descuento: {self.calcular_precio_con_descuento()}")
from Tecnologia import Tecnologia
from Transporte import Transporte

class Scooter(Tecnologia, Transporte):
    def __init__(self, marca, voltaje, eficiencia, precio, peso_kg, aro, velocidad, valor_por_kg=300):
        Tecnologia.__init__(self, marca, voltaje, eficiencia, precio)
        Transporte.__init__(self, marca, voltaje, eficiencia, precio, peso_kg, 300) 

        self.peso_kg = peso_kg
        self.aro = aro
        self.velocidad = velocidad
        self.valor_por_kg = valor_por_kg

    def mostrar_caracteristicas(self):
        print("Características del Scooter:")
        print(f"Marca: {self.marca}")
        print(f"Voltaje: {self.voltaje}")
        print(f"Eficiencia: {self.eficiencia}")
        print(f"Precio: {self.precio}")
        print(f"Peso: {self.peso_kg} kg")
        print(f"Aro: {self.aro}")
        print(f"Velocidad: {self.velocidad}")
        print(f"Descuento aplicado: {self.calcular_descuento() * 100}%")
        
        costo_despacho = self.calcular_costo_despacho()
        print(f"Costo del despacho: ${costo_despacho}")

        valor_total = self.calcular_precio_con_descuento() + costo_despacho
        print(f"Valor total luego del descuento y despacho: {valor_total}")

    def calcular_costo_despacho(self):
         return super().calcular_costo_despacho(self.valor_por_kg)
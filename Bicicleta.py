from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self, marca, precio, peso_kg, aro):
        costo_despacho_base = 4000
        valor_por_kg = 400  
        super().__init__(marca, None, None, precio, peso_kg, costo_despacho_base)
        self.aro = aro

    def calcular_costo_despacho(self):
        return super().calcular_costo_despacho(10)  

    def calcular_precio_con_descuento(self):
        return self.precio 

    def mostrar_caracteristicas(self):
        print(f"Marca: {self.marca}")
        print(f"Precio: {self.precio}")
        print(f"Peso: {self.peso_kg} kg")
        print(f"Aro: {self.aro}")

        costo_despacho = self.calcular_costo_despacho()
        print(f"Costo del despacho: ${costo_despacho}")

        valor_total = self.calcular_precio_con_descuento() + costo_despacho
        print(f"Valor total luego del descuento y despacho: {valor_total}")



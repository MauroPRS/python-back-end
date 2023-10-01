class Tecnologia:
    def __init__(self, marca:str, voltaje:int, eficiencia:str, precio:float):
        self.marca = marca
        self.voltaje = voltaje
        self.eficiencia = eficiencia
        self.precio = precio

    def calcular_descuento(self):
        if self.eficiencia in ['A', 'B']:
            return 0.5
        elif self.eficiencia in ['C', 'D']:
            return 0.3
        elif self.eficiencia in ['E', 'F']:
            return 0.1
        else:
            return 0

    def calcular_precio_con_descuento(self):
        descuento_eficiencia = self.calcular_descuento()
        precio_con_descuento = self.precio * (1 - descuento_eficiencia)
        return precio_con_descuento
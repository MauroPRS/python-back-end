class Transporte:
    def __init__(self, marca, voltaje, eficiencia, precio, peso_kg, costo_despacho_base):
        self.marca = marca
        self.voltaje = voltaje
        self.eficiencia = eficiencia
        self.precio = precio
        self.peso_kg = peso_kg
        self.costo_despacho_base = costo_despacho_base

    def calcular_costo_despacho(self, valor_por_kg):
        costo_despacho = self.costo_despacho_base + self.peso_kg * valor_por_kg
        return costo_despacho
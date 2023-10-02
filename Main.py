from Consola import Consola
from Scooter import Scooter
from  TV import TV
from Bicicleta import Bicicleta

lista_tvs=[]
lista_consolas = []
lista_scooters = []
lista_bicicletas = []




def mostrar_menu():
    print("Menú:")
    print("1. Registrar TV")
    print("2. Registrar Consola")
    print("3. Registrar Scooter")
    print("4. Registrar Bicicleta")
    print("5. Cotizar Consolas")
    print("6. Cotizar TV")
    print("7. Cotizar Scooters")
    print("8. Cotizar Bicicletas")
    print("9. Salir")

def registrar_bicicleta():
    marca = input("Ingrese la marca de la Bicicleta: ")
    precio = float(input("Ingrese el precio de la Bicicleta: "))
    peso_kg = int(input("Ingrese el peso de la Bicicleta en kg: "))
    aro = input("Ingrese el aro de la Bicicleta: ")
    bicicleta = Bicicleta(marca, precio, peso_kg, aro)
    bicicleta.mostrar_caracteristicas()
    lista_bicicletas.append(bicicleta)

def registrar_scooter():
    marca = input("Ingrese la marca del Scooter: ")
    voltaje = input("Ingrese el voltaje del Scooter: ")
    eficiencia = input("Ingrese la eficiencia del Scooter (A, B, C, D, E, F): ")
    precio = float(input("Ingrese el precio del Scooter: "))
    peso_kg = float(input("Ingrese el peso del Scooter en kg: "))
    aro = int(input("Ingrese el aro del Scooter: "))
    velocidad = int(input("Ingrese la velocidad del Scooter: "))
    scooter = Scooter(marca, voltaje, eficiencia, precio, peso_kg, aro, velocidad)
    scooter.mostrar_caracteristicas()
    scooter = Scooter(marca, voltaje, eficiencia, precio, peso_kg, aro, velocidad)
    lista_scooters.append(scooter)

    
def registrar_consola():
    marca = input("Ingrese la marca de la Consola: ")
    voltaje = input("Ingrese el voltaje de la Consola: ")
    eficiencia = input("Ingrese la eficiencia de la Consola (A, B, C, D, E, F): ")
    precio = float(input("Ingrese el precio de la Consola: "))
    nombre = input("Ingrese el nombre de la Consola: ")
    version = input("Ingrese la versión de la Consola: ")
    lite = input("¿Es versión Lite? (sí/no): ").lower() == 'sí'
    consola = Consola(marca, voltaje, eficiencia, precio, nombre, version, lite)
    consola.mostrar_caracteristicas()
    consola = Consola(marca, voltaje, eficiencia, precio, nombre, version, lite)
    lista_consolas.append(consola)

def registrar_tv():
    marca = input("Ingrese la marca del TV: ")
    voltaje = input("Ingrese el voltaje del TV: ")
    eficiencia = input("Ingrese la eficiencia del TV (A, B, C, D, E, F): ")
    precio = float(input("Ingrese el precio del TV: "))
    tamano = input("Ingrese el tamaño del TV: ")
    tv = TV(marca, voltaje, eficiencia, precio, tamano)
    tv.mostrar_caracteristicas()
    tv = TV(marca, voltaje, eficiencia, precio, tamano)
    lista_tvs.append(tv)

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            registrar_tv()
        elif opcion == 2:
            registrar_consola()
        elif opcion == 3:
            registrar_scooter()
        elif opcion == 4:
            registrar_bicicleta()
        elif opcion==5:
            for consola in lista_consolas:
                consola.mostrar_caracteristicas()
        elif opcion==6:
            for tv in lista_tvs:
                tv.mostrar_caracteristicas()
        elif opcion==7:
            for scooters in lista_scooters:
                scooters.mostrar_caracteristicas()   
        elif opcion==8:
            for bicicletas in lista_bicicletas:
                bicicletas.mostrar_caracteristicas()     
        elif opcion == 9:
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
import os
import json

# Definimos los datos para almacenar las salas y reservas
salas = {}

def guardar_datos():
    """Guarda el estado actual de las salas en un archivo JSON."""
    with open("salas.json", "w") as archivo:
        json.dump(salas, archivo)
    print("Datos guardados correctamente.")

def cargar_datos():
    """Carga los datos desde el archivo JSON si existe."""
    global salas
    if os.path.exists("salas.json"):
        with open("salas.json", "r") as archivo:
            salas = json.load(archivo)
        print("Datos cargados correctamente.")
    else:
        print("No hay datos guardados. Comenzando con datos vacíos.")

def crear_sala():
    """Permite crear una nueva sala con una cantidad específica de filas y columnas."""
    nombre_sala = input("Ingrese el nombre de la sala: ")
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    
    # Crear la matriz de asientos (todos disponibles inicialmente)
    asientos = [['O' for _ in range(columnas)] for _ in range(filas)]
    salas[nombre_sala] = asientos
    guardar_datos()
    print(f"Sala {nombre_sala} creada exitosamente.")

def mostrar_sala(nombre_sala):
    """Muestra el estado actual de una sala."""
    if nombre_sala in salas:
        print(f"Estado de la sala {nombre_sala}:")
        for fila in salas[nombre_sala]:
            print(' '.join(fila))
    else:
        print("La sala no existe.")

def cargar_y_mostrar_sala():
    """Carga una sala específica desde el archivo y muestra su estado actual."""
    # Asegura que los datos más recientes estén cargados
    cargar_datos()  
    nombre_sala = input("Ingrese el nombre de la sala a cargar y mostrar: ")
    mostrar_sala(nombre_sala)

def reservar_asiento():
    """Permite reservar un asiento específico en una sala."""
    nombre_sala = input("Ingrese el nombre de la sala: ")
    if nombre_sala in salas:
        fila = int(input("Ingrese el número de fila: ")) - 1
        columna = int(input("Ingrese el número de columna: ")) - 1
        if salas[nombre_sala][fila][columna] == 'O':
            salas[nombre_sala][fila][columna] = 'X'
            guardar_datos()
            print("Asiento reservado exitosamente.")
        else:
            print("El asiento ya está reservado.")
    else:
        print("La sala no existe.")

def cancelar_reserva():
    """Permite cancelar una reserva en una sala."""
    nombre_sala = input("Ingrese el nombre de la sala: ")
    if nombre_sala in salas:
        fila = int(input("Ingrese el número de fila: ")) - 1
        columna = int(input("Ingrese el número de columna: ")) - 1
        if salas[nombre_sala][fila][columna] == 'X':
            salas[nombre_sala][fila][columna] = 'O'
            guardar_datos()
            print("Reserva cancelada exitosamente.")
        else:
            print("El asiento no estaba reservado.")
    else:
        print("La sala no existe.")

def menu_principal():
    """Muestra el menú principal de la aplicación y gestiona la interacción del usuario."""
    cargar_datos()
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear Sala")
        print("2. Mostrar Sala")
        print("3. Cargar y Mostrar Sala")
        print("4. Reservar Asiento")
        print("5. Cancelar Reserva")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_sala()
        elif opcion == '2':
            nombre_sala = input("Ingrese el nombre de la sala a mostrar: ")
            mostrar_sala(nombre_sala)
        elif opcion == '3':
            cargar_y_mostrar_sala()
        elif opcion == '4':
            reservar_asiento()
        elif opcion == '5':
            cancelar_reserva()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()


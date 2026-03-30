import csv
import os

# Crear archivo si no existe
if not os.path.exists("clientes.csv"):
    with open("clientes.csv", "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["id", "nombre", "correo"])  # encabezados


while True:
    print("\n1. Agregar cliente")
    print("2. Ver clientes")
    print("3. Buscar cliente")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    # ➕ AGREGAR CLIENTE
    if opcion == "1":
        id_cliente = input("ID: ")
        nombre = input("Nombre: ")
        correo = input("Correo: ")

        with open("clientes.csv", "a", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow([id_cliente, nombre, correo])

        print("Cliente agregado correctamente")

    # 📖 VER CLIENTES
    elif opcion == "2":
        with open("clientes.csv", "r") as archivo:
            reader = csv.DictReader(archivo)

            for fila in reader:
                print(fila["id"], "-", fila["nombre"], "-", fila["correo"])

    # 🔍 BUSCAR CLIENTE
    elif opcion == "3":
        buscar = input("Ingrese ID a buscar: ")
        encontrado = False

        with open("clientes.csv", "r") as archivo:
            reader = csv.DictReader(archivo)

            for fila in reader:
                if fila["id"] == buscar:
                    print(fila["id"], "-", fila["nombre"], "-", fila["correo"])
                    encontrado = True

        if not encontrado:
            print("Cliente no encontrado")

    # 🚪 SALIR
    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")
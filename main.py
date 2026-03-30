import os, json

if not os.path.exists("clientes.json"):
    with open("clientes.json", "w", encoding = "utf-8") as archivo:
        json.dump([], archivo, indent=4)


selec = ""

while selec != "salir" and selec != "4":
    print("1. Agregar cliente\n2. Ver clientes\n3. Buscar cliente\n4. Salir")
    selec = input("Ingrese una opción: ").lower()

    with open("clientes.json", "r") as archivo:
        leer = json.load(archivo)

    if selec == "agregar cliente" or selec == "1":

        ide = len(leer) + 1
        nombre = input("Ingrese nombre del cliente: ")
        correo = input(f"Ingrese correo del cliente {nombre}: ")

        nuevo = {
            "id": ide,
            "nombre": nombre,
            "correo": correo
        }

        leer.append(nuevo)

        with open("clientes.json", "w", encoding = "utf-8") as archivo:
            json.dump(leer, archivo, indent=4)
                
            print(f"El cliente {nombre} ha sido registrado.")
    
    elif selec == "ver clientes" or selec == "2":

        if len(leer) > 0:
            for p in leer:
                print(p["id"], "-", p["nombre"], "-", p["correo"])
        
        else:
            print("No hay clientes registrados.")
    
    elif selec == "buscar cliente" or selec == "3":

        if len(leer) > 0:
            buscar = int(input("Ingrese ID del cliente que desea buscar: "))
            encontrado = False

            for cliente in leer:
                if cliente["id"] == buscar:
                    print(cliente["id"], "-", cliente["nombre"], "-", cliente["correo"])
                    encontrado = True

            if encontrado == False:
                print(f"No hay clientes registrados con el ID {buscar}")
        
        else:
            print("No hay clientes registrados")

    elif selec == "salir" or selec == "4":
        print("Ha salido del programa.")
    
    else:
        print("Opción inválida.")
            
        
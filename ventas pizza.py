import json
import datetime

ventas = []

def mostrar_menu():
    while True:
        print("\nMenú del Sistema de Ventas de Pizzas")
        print("1. Registrar una venta")
        print("2. Mostrar todas las ventas")
        print("3. Buscar ventas por cliente")
        print("4. Guardar las ventas en un archivo")
        print("5. Cargar las ventas desde un archivo")
        print("6. Generar Boleta")
        print("7. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_venta()
        elif opcion == '2':
            mostrar_ventas()
        elif opcion == '3':
            buscar_ventas_por_cliente()
        elif opcion == '4':
            guardar_ventas()
        elif opcion == '5':
            cargar_ventas()
        elif opcion == '6':
            generar_boleta()
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def registrar_venta():
    
    nombre_cliente = input("Ingrese el nombre del cliente: ")

 

    print("Seleccione el tipo de pizza:")
    print("1. Peperoni")
    print("2. Mediterránea")
    print("3. Vegetariana")
    tipo_pizza_opcion = input("Ingrese el número correspondiente: ")
    tipo_pizza = ''
    if tipo_pizza_opcion == '1':
        tipo_pizza = 'Peperoni'
    elif tipo_pizza_opcion == '2':
        tipo_pizza = 'Mediterránea'
    elif tipo_pizza_opcion == '3':
        tipo_pizza = 'Vegetariana'
    else:
        print("Opción no válida. Inténtelo de nuevo.")
        return



    print("Seleccione el tamaño de la pizza:")
    print("1. Pequeña")
    print("2. Mediana")
    print("3. Familiar")
    tamaño_pizza_opcion = input("Ingrese el número correspondiente: ")
    tamaño_pizza = ''
    if tamaño_pizza_opcion == '1':
        tamaño_pizza = 'Pequeña'
    elif tamaño_pizza_opcion == '2':
        tamaño_pizza = 'Mediana'
    elif tamaño_pizza_opcion == '3':
        tamaño_pizza = 'Familiar'
    else:
        print("Opción no válida. Inténtelo de nuevo.")
        return



    print("Seleccione el tipo de usuario:")
    print("1. Estudiante diurno")
    print("2. Estudiante vespertino")
    print("3. Administrativo")
    tipo_usuario_opcion = input("Ingrese el número correspondiente: ")
    tipo_usuario = ''
    if tipo_usuario_opcion == '1':
        tipo_usuario = 'Estudiante diurno'
    elif tipo_usuario_opcion == '2':
        tipo_usuario = 'Estudiante vespertino'
    elif tipo_usuario_opcion == '3':
        tipo_usuario = 'Administrativo'
    else:
        print("Opción no válida. Inténtelo de nuevo.")
        return
    


    precio = calcular_precio(tipo_pizza, tamaño_pizza)

    descuento = aplicar_descuento(precio, tipo_usuario)

    total = precio - descuento
    venta = {
        'nombre_cliente': nombre_cliente,
        'tipo_pizza': tipo_pizza,
        'tamaño_pizza': tamaño_pizza,
        'tipo_usuario': tipo_usuario,
        'precio': precio,
        'descuento': descuento,
        'total': total,
        'fecha_hora': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    ventas.append(venta)
    print("Venta registrada con éxito.")

def calcular_precio(tipo_pizza, tamaño_pizza):
    precios = {
        'Peperoni Pequeña': 5000,
        'Peperoni Mediana': 8000,
        'Peperoni Familiar': 10000,
        'Mediterránea Pequeña': 5500,
        'Mediterránea Mediana': 8500,
        'Mediterránea Familiar': 10500,
        'Vegetariana Pequeña': 4500,
        'Vegetariana Mediana': 7500,
        'Vegetariana Familiar': 9500
    }
    tipo_y_tamaño = f"{tipo_pizza} {tamaño_pizza}"
    if tipo_y_tamaño in precios:
        return precios[tipo_y_tamaño]
    else:
        print("Error: El tipo de pizza o el tamaño no son válidos.")
        return 0

def aplicar_descuento(precio, tipo_usuario):
    descuentos = {
        'Estudiante diurno': 0.15,
        'Estudiante vespertino': 0.20,
        'Administrativo': 0.10
    }
    return precio * descuentos.get(tipo_usuario, 0)

def mostrar_ventas():
    for venta in ventas:
        print(venta)

def buscar_ventas_por_cliente():
    nombre_cliente = input("Ingrese el nombre del cliente a buscar: ")
    ventas_cliente = [venta for venta in ventas if venta['nombre_cliente'] == nombre_cliente]
    for venta in ventas_cliente:
        print(venta)

def guardar_ventas():
    with open('ventas.json', 'w') as file:
        json.dump(ventas, file)
    print("Ventas guardadas en el archivo ventas.json")

def cargar_ventas():
    global ventas
    try:
        with open('ventas.json', 'r') as file:
            ventas = json.load(file)
        print("Ventas cargadas desde el archivo ventas.json")
    except FileNotFoundError:
        print("No se encontró el archivo ventas.json")

def generar_boleta():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    ventas_cliente = [venta for venta in ventas if venta['nombre_cliente'] == nombre_cliente]
    if ventas_cliente:
        print("\nBoleta")
        print("Fecha y Hora:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("Cliente:", nombre_cliente)
        total_a_pagar = 0
        for venta in ventas_cliente:
            print(f"Pizza: {venta['tipo_pizza']} - Tamaño: {venta['tamaño_pizza']} - Precio: {venta['precio']} - Descuento: {venta['descuento']} - Total: {venta['total']}")
            total_a_pagar += venta['total']
        print(f"Total a Pagar: {total_a_pagar}")
    else:
        print("No se encontraron ventas para el cliente especificado.")



if __name__ == "__main__":
    mostrar_menu()

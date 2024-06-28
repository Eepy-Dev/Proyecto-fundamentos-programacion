biblioteca = {}
while True:
    print("Bienvenido al menú de la biblioteca")
    print("1. Agregar libro ")
    print("2. Eliminar libro ")
    print("3. Buscar libro ")
    print("4. Listar libros ")
    print("5. Salir ")
    opcion = int(input("Seleccione una opción: "))

        
    if opcion == 1:
        
         def agregar_libro(biblioteca):
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            biblioteca[titulo] = autor
            print(f"Libro '{titulo}' de {autor} agregado a la biblioteca.")
         agregar_libro(biblioteca)   

    elif opcion == 2:
        
        def eliminar_libro(biblioteca):
            titulo = input("Ingrese el título del libro a eliminar: ")
            if titulo in biblioteca:
                del biblioteca[titulo]
                print(f"Libro '{titulo}' eliminado de la biblioteca.")
            else:
                print(f"El libro '{titulo}' no se encuentra en la biblioteca.")
        eliminar_libro(biblioteca)

    elif opcion == 3:
        
        def buscar_libro(biblioteca):
            titulo = input("Ingrese el título del libro a buscar: ")
            if titulo in biblioteca:
                print(f"El libro '{titulo}' es de {biblioteca[titulo]}.")
            else:
                print(f"El libro '{titulo}' no se encuentra en la biblioteca.")
        buscar_libro(biblioteca)
        
    elif opcion == 4:
        
        def listar_libros(biblioteca):
            if biblioteca:
                print("\n--- Lista de Libros ---")
            for titulo, autor in biblioteca.items():
                print(f"'{titulo}' de {autor}")
            else:
                print("La biblioteca está vacía.")
        listar_libros(biblioteca)

    elif opcion == 5:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

   

    
    

    





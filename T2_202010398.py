#Author Pablo Amaya

def main():
    usuarios = []
    libros = []

    def agregar_usuario():
        try:
            id_usuario = int(input("Ingresa el ID del usuario: "))
            nombre = input("Ingresa el nombre del usuario: ")
            edad = int(input("Ingresa la edad del usuario: "))
            activo = input("¿Está activo? (s/n): ").lower() == 's'
            usuarios.append({"id": id_usuario, "nombre": nombre, "edad": edad, "activo": activo, "libros": []})
            print("Se ha agregado al usuario\n")
        except ValueError:
            print("Error: El ID y la edad deben ser números.\n")

    def agregar_libro():
        try:
            isbn = int(input("Ingresa el ISBN del libro: "))
            titulo = input("Ingresa el título del libro: ")
            libros.append({"isbn": isbn, "titulo": titulo})
            print("Se ha agregado el libro\n")
        except ValueError:
            print("Error: ISBN debe ser un número.\n")

    def agregar_libro_a_usuario():
        try:
            id_usuario = int(input("Ingresa el ID del usuario: "))
            isbn_libro = int(input("Ingresa el ISBN del libro: "))
            usuario = next((u for u in usuarios if u["id"] == id_usuario), None)
            libro = next((l for l in libros if l["isbn"] == isbn_libro), None)

            if usuario and libro:
                usuario["libros"].append(libro)
                print("Libro agregado al usuario exitosamente!\n")
            else:
                print("Error: No se encontró el libro o usuario.\n")
        except ValueError:
            print("Error: El ID y el ISBN deben ser números.\n")

    def imprimir_usuario():
        try:
            id_usuario = int(input("Ingresa el ID del usuario a mostrar: "))
            usuario = next((u for u in usuarios if u["id"] == id_usuario), None)

            if usuario:
                print("\nUsuario:")
                print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Edad: {usuario['edad']}, Activo: {usuario['activo']}")
                print("Libros:")
                for libro in usuario["libros"]:
                    print(f"  - ISBN: {libro['isbn']}, Título: {libro['titulo']}")
                print()
            else:
                print("Error: No se encontró el usuario.\n")
        except ValueError:
            print("Error: ID debe ser un número.\n")

    while True:
        print("-------Bienvenido al sistema-------\n")
        print("Menú:")
        print("1. Agregar un nuevo usuario")
        print("2. Agregar un nuevo libro")
        print("3. Asignar un libro a un usuario")
        print("4. Imprimir determinado usuario con sus libros")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            agregar_libro()
        elif opcion == "3":
            agregar_libro_a_usuario()
        elif opcion == "4":
            imprimir_usuario()
        elif opcion == "5":
            print("")
            print("------Gracias por usar el servicio------")
            print("")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()

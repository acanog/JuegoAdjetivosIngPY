from administrator.sesion_login import show_users, create_user, delete_user
def managment_users():
    print("Gestión de Usuarios")
    print("Decide que quieres hacer: " \
    "\n1. Mostrar usuarios" \
    "\n2. Crear usuario" \
    "\n3. Eliminar usuario" \
    "\n4. Salir")
    option = int(input())

    while True:
        match option:
            case 1:
                print("Mostrar usuarios")
                show_users()
            case 2:
                print("Crear usuario")
                username = input("Ingrese el nombre de usuario: ")
                password = input("Ingrese la contraseña: ")
                create_user(username, password)            
            case 3:
                print("Eliminar usuario")
                username = input("Ingrese el nombre de usuario a eliminar: ")
                delete_user(username)      
            case 4:
                print("salir")
                break
            case _:
                print("Opción no válida.")
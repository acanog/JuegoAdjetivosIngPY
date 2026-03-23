from administrator.main_users import managment_users
from administrator.sesion_login import validate_login
from classmates.classmates import Classmates_list
from adjectives.main_adjetives import adjetives_play
from classmates.main_classmates import main_classmates

#Main principal del programa, aqui se decide que juego se va a jugar o si se va a gestionar los compañeros
print("Ingrese las credenciales para iniciar")
login = False

username = input("Nombre de usuario: ")
password = input("Contraseña: ")

while not validate_login(username, password):
    print("Credenciales inválidas. Por favor, inténtalo de nuevo.")
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")


print("¡Que comiencen los juegos del miedo!")

#Cargamos las listas de compañeros
classmates_list_f = Classmates_list;

while True:
    option = 99
    while option <= 0 or option > 3:
        if option == 99:
            print("Decide que quieres hacer: " \
            "\n1. Jugar con adjetivos" \
            "\n2. Gestionar compañeros" \
            "\n3. Gestionar usuarios" \
            "\n4. Salir")
            option = int(input())
        else:
            print("opcion no valida, por favor elige una opción del 1 al 3")
    #Decidimos que juego se va a jugar o si se va a gestionar los compañeros        
    match option:
        case 1:
            print("Juegos adjetivos")
            adjetives_play(classmates_list_f)
        case 2:
            print("Gestionar compañeros")
            main_classmates(classmates_list_f)
        case 3:
            print ("gestionar usuarios")
            managment_users()
        case 3:
            print("¡Gracias por jugar!")
            break
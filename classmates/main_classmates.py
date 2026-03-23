
from classmates.admin_classmates import score_positions, add_classmate, delete_classmate, reset_chosen_flag

#funcion para gestionar compañeros, aquí se decide que gestión se va a realizar
def main_classmates(classmates_list_f):
    print("Elige la gestion de usuario que deseas realizar:")
    
    classmates_list_f = classmates_list_f;

    while True:
        option = 99
        while option <= 0 or option >= 5:
            if option == 99:
                print("Decide que quieres hacer: ")
                print("1. Ver tabla de posiciones de compañeros")
                print("2. Agregar compañero")
                print("3. Eliminar compañero")
                print("4. Reiniciar bandera de compañeros")
                print("5. Salir")
                option = int(input())
            else:
                print("Opción no válida, por favor elige una opción del 1 al 3")

        #decidimos que gestión de compañeros se va a realizar
        match option:
            case 1:
                print("Puntajes de compañeros")
                score_positions(classmates_list_f)
            case 2:
                print("Agregar compañero")
                add_classmate(classmates_list_f)
            case 3:
                print("Eliminar compañero")
                delete_classmate(classmates_list_f)
            case 4:
                print("Reiniciar banderas de compañeros")
                reset_chosen_flag(classmates_list_f)
            case 5:
                print("¡Gracias por jugar!")
                break
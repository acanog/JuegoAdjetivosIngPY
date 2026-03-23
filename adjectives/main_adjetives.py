from classmates.finder_classmates import choose_random_classmates
from adjectives.finder_categories import choose_random_categories
from adjectives.adjetives_for_children import Adjetives_for_children_list, categories_children
from adjectives.adjetives_for_over18 import Adjetives_for_over18_list, categorias_for_over18

list_classmates = []

#funcion para gestionar el juego de adjetivos, aquí se decide que compañero se va a elegir, que categoria y que adjetivo

def adjetives_play(list_classmates):
    

    print("A continuacion se elegira un compañero al azar")

    classmates_list_f = list_classmates;

    adjetives = []

    while True:
        print("Eres niño? (s/n)")
        answer = input().lower()
        if answer in ["s", "n"]:
            break

    while True:

        #Decidimos que lista de adjetivos y categorias se va a usar dependiendo de la respuesta del usuario
        if answer == "s":
            adjetives = Adjetives_for_children_list
            categories = categories_children
        else:
            adjetives = Adjetives_for_over18_list
            categories = categorias_for_over18

        #se llama la funcion para elegir un compañero al azar, si no quedan compañeros por elegir se termina el juego
        classmate_choose = choose_random_classmates(classmates_list_f)
        if classmate_choose is None:
            print("No quedan compañeros por elegir.")
            break
        print(f"El compañero elegido es: {classmate_choose['name']}")
        counter = 0

        change_adjetive = True

        #se muestra la lista de categorias y se pide al usuario que elija una categoria escribiendo el numero correspondiente, si no quedan categorias por elegir se termina el juego
        print("elige una categoria deacuerdo a la lista y escribiendo el numero correspondiente:")
        for cat in categories:
            print(f"{cat['id_category']}: {cat['category']}")
        id_category = int(input())
        print("Adjetivos:")

        #se llama la funcion para elegir un adjetivo al azar de la categoria elegida, si no quedan adjetivos por elegir se termina el juego
        while change_adjetive == True:
            categories_choose = choose_random_categories(id_category, adjetives)
            counter += 1
            print(f"El adjetivo es {categories_choose['en']}")

            while True:
                print("Te gustaria cambiar de adjetivo? Solo lo puedes hacer 1 vez (s/n)")
                answer_repeat = input().lower()
                if answer_repeat in ["s", "n"]:
                    break
            if answer_repeat == "n":
                change_adjetive = False
            elif counter > 1:
                print("Ya has cambiado de adjetivo una vez, no puedes cambiar más.")
                break

        #se pide al usuario que escriba la respuesta, si la respuesta es correcta se le asignan puntos dependiendo de si cambio o no de adjetivo, si la respuesta es incorrecta se muestra la respuesta correcta, si no quedan categorias por elegir se termina el juego
        if change_adjetive == False:
            print(f"Como se dice {categories_choose['en']} en español?")
            answer_response = input().lower()
            if answer_response in categories_choose['es'].lower():
                if counter == 1:
                    print("¡Excelente! Has acertado sin cambiar de adjetivo.")
                    classmate_choose["score"] += 3
                elif counter == 2:
                    print("¡Muy bien! Has acertado después de cambiar una vez.")
                    classmate_choose["score"] += 1
            else:
                print(f"¡Incorrecto! La respuesta correcta es: {categories_choose['es']}")
            if categories_choose is None:
                print("No quedan categorías por elegir.")
                break

        #se pregunta al usuario si quiere elegir otro compañero, si la respuesta es no se termina el juego
        print("¿Quieres elegir otro compañero? (s/n)")
        answer_next = input().lower()

        if answer_next != "s":
            break
    print("¡Gracias por jugar!")

#adjetives_play(list_classmates)
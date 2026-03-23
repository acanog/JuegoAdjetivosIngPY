
list_classmates = []

    #clase que muestra la tabla de posiciones de los compañeros,
    #ordenados por puntaje de mayor a menor, indicando el nombre, el puntaje y si han sido elegidos o no.

def score_positions(list_classmates):
    #funcion que muestra la tabla de posiciones de los compañeros, ordenados por puntaje de mayor a menor, indicando el nombre, el puntaje y si han sido elegidos o no.
    """
    Muestra la lista de compañeros.
    """
    print("Tabla de posiciones de compañeros:")    
    #ordenamos la lista de compañeros por puntaje de mayor a menor
    sorted_classmates = sorted(list_classmates, key=lambda x: x['score'], reverse=True)
    order = 0
    for classmate in sorted_classmates:
        order += 1
        #se muestra el orden de los compañeros por score priorizando  el top 3
        match order:
            case 1:
                print(f"Felicidades {classmate['name']}: Tienes un puntaje de {classmate['score']} puntos y eres el numero 1, {classmate['chosen']}")
            case 2:
                print(f"Felicidades {classmate['name']}: estas en el top 3 con un puntaje de  {classmate['score']}, {classmate['chosen']}")
            case 3:                
                print(f"Felicidades {classmate['name']}: estas en el top 3 con un puntaje de  {classmate['score']}, {classmate['chosen']}")
            case _:
                print(f"{classmate['name']}: Tienes un puntaje de {classmate['score']} puntos, {classmate['chosen']}")
                

def add_classmate(list_classmates):
    #funcion que agrega un nuevo compañero a la lista, solicitando el nombre del nuevo compañero al usuario, asignándole un ID único, y agregándolo a la lista con chosen=False y score=0.
    """
    Agrega un nuevo compañero a la lista.
    """
    name = input().strip(print("Indica el nombre del nuevo compañero:"))
    new_id = max([c["id"] for c in list_classmates], default=0) + 1
    new_classmate = {"id": new_id, "name": name, "chosen": False, "score": 0}
    list_classmates.append(new_classmate)
    print(f"Compañero '{name}' agregado con ID {new_id}.")

def delete_classmate(list_classmates):
    #funcion que elimina un compañero de la lista, solicitando el nombre del compañero a eliminar al usuario, y eliminándolo de la lista.
    """
    Elimina un compañero de la lista.
    """
    name = input("Indica el nombre del compañero a eliminar:").strip()
    new_list = [c for c in list_classmates if c["name"] != name]
    if len(new_list) == len(list_classmates):
        print(f"No se encontró un compañero con el nombre '{name}'.")
        return
    list_classmates[:] = new_list
    print(f"Compañero '{name}' eliminado.")

def reset_chosen_flag(list_classmates):
    #funcion que reinicia el flag 'chosen' para todos los compañeros, estableciendo chosen=False para cada compañero en la lista.
    """
    Reinicia el flag 'chosen' para todos los compañeros.
    """
    for classmate in list_classmates:
        classmate["chosen"] = False
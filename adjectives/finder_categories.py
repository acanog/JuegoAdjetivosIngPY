import random

id_category = 99
list_Categories = []

def choose_random_categories(id_category, list_Categories):
    #funcion para elegir un adjetivo al azar de una categoria, se le pasa el id de la categoria y la lista de categorias, se busca la categoria por su id, se filtran los adjetivos que no han sido elegidos, se elige uno al azar, se marca como elegido y se retorna, si no quedan adjetivos por elegir se retorna None
    """
    Elige aleatoriamente una categoría con chosen=False, lo marca como True y lo retorna.
    Si no quedan, retorna None.
    """   
    # Buscar la categoría por su id    
    if id_category == 99:
        return None
    
    category = next((cat for cat in list_Categories if cat["id_category"] == id_category), None)
    if not category:
        print(f"Error: No se encontró la categoría con id {id_category}")
        return None

    # Filtrar adjetivos no elegidos
    adjetives_not_choose = [adj for adj in category["adjectives"] if not adj["chosen"]]
    if not adjetives_not_choose:
        print(f"Todos los adjetivos de la categoría '{category['category']}' ya fueron elegidos.")
        return None

    # Seleccionar uno al azar
    elegido = random.choice(adjetives_not_choose)
    # Marcarlo como elegido
    elegido["chosen"] = True
    return elegido

choose_random_categories(id_category, list_Categories)
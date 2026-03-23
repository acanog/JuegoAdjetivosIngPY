import random

list_classmates = []

def choose_random_classmates(list_classmates):
    #Busca aleatoriamente un compañero con chosen=False, lo marca como True y lo retorna. Si no quedan, retorna None.
    """
    Elige aleatoriamente un compañero con chosen=False, lo marca como True y lo retorna.
    Si no quedan, retorna None.
    """
    # Filtrar los no elegidos
    no_elegidos = [c for c in list_classmates if not c["chosen"]]
    if not no_elegidos:
        return None
    # Seleccionar uno al azar
    elegido = random.choice(no_elegidos)
    # Marcarlo como elegido
    elegido["chosen"] = True
    return elegido

choose_random_classmates(list_classmates)
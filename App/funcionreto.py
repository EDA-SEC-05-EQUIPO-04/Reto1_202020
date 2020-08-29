from Sorting import shellsort as shsort
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

def MovieSorting (list1, parameter):
    """
    FUNCION 2:
    list1: Lista de metadatos de la película.
    parameter: si se ordena por COUNT o AVERAGE

    Como aficionado del cine Quiero crear el Ranking  de las películas  
    por las mas y menos votadas (COUNT) y por las mejor o peor calificadas 
    (AVERAGE)  del catalogo.

    Las condiciones son:
    −Por lo menos 10 películas (x = 10).
    −COUNT se ordena por la cantidad de votos (vote_count).
    −AVERAGE se ordena por la calificación promedio (vote_average).
    −Ordenamiento ascendente y descendente.
    """
    if parameter == "AVERAGE":
        datos = "vote_average"
    elif parameter == "COUNT":
        datos = "vote_count"
    
    count = 1
    iter = listiterator.newIterator(parameter)
    while listiterator.hasNext(iter):
        c = listiterator.next(iter)
        tup = []



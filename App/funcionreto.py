from Sorting import shellsort as shsort
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from ADT import list as lt
from Sorting import config as cfdos


def MovieSorting (list1, parameter, lessfunction):
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
    
    mvlst = lt.newList('SINGLE_LINKED', None)
    
    iter = listiterator.newIterator(list1)
    while listiterator.hasNext(iter):
        c = listiterator.next(iter)
        tup = ()
        tup.append(c["original_title"])
        tup.append(c[parameter])
        tup.append(c["id"])

        lt.addLast(mvlst, tup)

    iter = it.newIterator(mvlst)

    #Basicamente shellsort pero adaptado

    n = lt.size(mvlst)
    h = 1

    while h < n/3:          
        h = 3*h + 1
    while (h >= 1):
        for i in range (h,n):
            j = i
            while (j>=h) and lessfunction (lt.getElement(mvlst[1],j+1),lt.getElement(mvlst[1],j-h+1)):
                lt.exchange (mvlst, j+1, j-h+1)
                j -=h
        h //=3

    tenbest = lt.subList(mvlst, 0, 10)
    tenworst = lt.subList(mvlist, (lt.size(mvlst)-11), (lt.size(mvlst)-1))

    print ("MEJORES:")
    print ("PELICULA    CALIF.")
    for i in len(tenbest):
        print((tenbest[i]['elements'][0]),"     ",(tenbest[i]['elements'][1]))
    
    print ("PEORES:")
    print ("PELICULA    CALIF.")
    for i in len(tenworst):
        print((tenworst[i]['elements'][0]),"     ",(tenworst[i]['elements'][1]))
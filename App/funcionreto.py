from Sorting import shellsort as shsort
from DataStructures import listiterator
from DataStructures import liststructure as lt
from ADT import list as lt
from Sorting import config as cfdos
from time import process_time 

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


def conocer_actor (casting, details):
    peliculas_dirigidas_por_x_director = lt.newList('SINGLE_LINKED', None)
    actor = input("Ingrese el actor:\n")

    t1_start = process_time()

    iter = listiterator.newIterator(casting)
    while listiterator.hasNext(iter):
        d = listiterator.next(iter)
        if d["actor1_name"] == actor or d["actor2_name"] == actor or d["actor3_name"] == actor or d["actor4_name"] == actor or d["actor5_name"] == actor:        
            lt.addFirst(peliculas_dirigidas_por_x_director, d)
            


    peliculas = lt.newList('SINGLE_LINKED', None)

    directores = {}

    iter1 = listiterator.newIterator(peliculas_dirigidas_por_x_director)
    while listiterator.hasNext(iter1):
        ide = listiterator.next(iter1)

        iter2 = listiterator.newIterator(details)
        while listiterator.hasNext(iter2):
            p = listiterator.next(iter2)

            if ide["id"] == p["id"]:
                lt.addFirst(peliculas, p)
                print(p["original_title"])
                if ide["director_name"] in directores:
                    directores[ide["director_name"]] += 1
                else:
                    directores[ide["director_name"]] = 1


    #encontrar directores pelis
    maximo_colab = max(directores, key=directores.get)  
    


    #encontrar los datos

    numero_peliculas_director = lt.size(peliculas)
    suma_promedio_voto = 0

    iter = listiterator.newIterator(peliculas)
    while listiterator.hasNext(iter):
        s = listiterator.next(iter)
        suma_promedio_voto += float(s["vote_average"])


    promedio_pelis = 0
    if(numero_peliculas_director > 0):
        promedio_pelis = suma_promedio_voto/numero_peliculas_director

    #print("Peliculas dirigidas por "+ director +": " + str(peliculas['title'])) Encontrar los nombres de las peliculas
    print("Numero de películas de "+ actor + ": " + str(numero_peliculas_director))
    print("Promedio de calificación de las peliculas del actor: " + str(promedio_pelis))
    print("el director con mayor número de colaboraciones es: " + maximo_colab)
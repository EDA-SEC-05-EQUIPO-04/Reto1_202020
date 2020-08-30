import config as conf
import csv
from ADT import list as lt
from DataStructures import listiterator
from time import process_time 


#Cargar archivos
def crear_lista(camino):
    
    lista = lt.newList('SINGLE_LINKED', None)
    #casting_file = "Data/MoviesCastingRaw-small.csv"
    # #casting_file = "Data/themoviesdb\MoviesCastingRaw-small.csv"
    with open(camino, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            lt.addFirst(lista, row)
    return lista




def conocer_a_un_director(director):
    """
    Función 3
    Conocer a un director
    director: nombre del director

    Como aficionado del cine Quiero
    conocer el trabajo de un director.
    """

    casting = crear_lista("Data/themoviesdb\MoviesCastingRaw-small.csv")
    details = crear_lista('Data/themoviesdb\SmallMoviesDetailsCleaned.csv')

    peliculas_dirigidas_por_x_director = lt.newList('SINGLE_LINKED', None)
    
    iter = listiterator.newIterator(casting)
    while listiterator.hasNext(iter):
        d = listiterator.next(iter)
        if d["director_name"] == director:
            lt.addFirst(peliculas_dirigidas_por_x_director, d)
        

    peliculas = lt.newList('SINGLE_LINKED', None)



    iter1 = listiterator.newIterator(peliculas_dirigidas_por_x_director)
    while listiterator.hasNext(iter1):
        ide = listiterator.next(iter1)

    iter2 = listiterator.newIterator(details)
    while listiterator.hasNext(iter2):
        p = listiterator.next(iter2)

        if ide["id"] == p["id"]:
            lt.addFirst(peliculas, p)
            print (p["original_title"])
            


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
    resultado = {}
    resultado["Numero de películas de "+ director] = numero_peliculas_director
    resultado["Promedio de calificación de las peliculas del director "] = promedio_pelis
    return resultado







#FUNCION 5









def entender_genero_peliculas (genero):
    """
    
    Funcion 5:
    genero: género de intéres
    casting: info del archivo csv casting
    details: info del archivo csv details cleaned

    Como aficionado del cine Quiero
    entender las características de un
    genero de películas.

    Las condicionesson:
    −El nombre del genero
    cinematográfico (genres).

    """
    
    
    casting = crear_lista("Data/themoviesdb\MoviesCastingRaw-small.csv")
    details = crear_lista('Data/themoviesdb\SmallMoviesDetailsCleaned.csv')

    peliculas_del_genero = lt.newList('SINGLE_LINKED', None)
    iter = listiterator.newIterator(details)
    while listiterator.hasNext(iter):
        d = listiterator.next(iter)
        if genero in d["genres"]:
            lt.addFirst(peliculas_del_genero, d)
            print(d["original_title"])


    numero_peliculas_genero = lt.size(peliculas_del_genero)
    suma_promedio_voto = 0
    nombres_peliculas = []

    iter = listiterator.newIterator(peliculas_del_genero)
    while listiterator.hasNext(iter):
        s = listiterator.next(iter)
        suma_promedio_voto += float(s["vote_count"])

    promedio_vote_count = 0
    if(numero_peliculas_genero > 0):
        promedio_vote_count = suma_promedio_voto/numero_peliculas_genero

    #mostrar la lista
    respuesta = {}
    respuesta['Numero de películas asociadas al género '+ genero] = numero_peliculas_genero
    respuesta["Promedio de votos de las peliculas del género "+ genero] = promedio_vote_count
    return respuesta

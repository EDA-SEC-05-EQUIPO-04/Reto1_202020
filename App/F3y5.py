import config as conf
import csv
from ADT import list as lt
from DataStructures import listiterator
from time import process_time 


#Cargar archivos

casting = lt.newList('SINGLE_LINKED', None)
#casting_file = "Data/MoviesCastingRaw-small.csv"
casting_file = "Data/themoviesdb\MoviesCastingRaw-small.csv"
with open(casting_file, encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        lt.addFirst(casting, row)


details = lt.newList('SINGLE_LINKED', None)
#details_file = "Data/SmallMoviesDetailsCleaned.csv"
details_file = "Data/themoviesdb\SmallMoviesDetailsCleaned.csv"
with open(details_file, encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        lt.addFirst(details, row)

"""
print("1- Req 3 - Conocer a un director")

#hacer la lista

peliculas_dirigidas_por_x_director = lt.newList('SINGLE_LINKED', None)
director = input("Ingrese el director\n")

t1_start = process_time()

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
            break
    print(peliculas)

#encontrar titulos pelis

iter = listiterator.newIterator(peliculas)
while listiterator.hasNext(iter):
    s = listiterator.next(iter)


#encontrar los datos

numero_peliculas_director = lt.size(peliculas)
suma_promedio_voto = 0
nombres_peliculas = []

iter = listiterator.newIterator(peliculas)
while listiterator.hasNext(iter):
    s = listiterator.next(iter)
    suma_promedio_voto += float(s["vote_average"])
    print(nombres_peliculas)

promedio_pelis = 0
if(numero_peliculas_director > 0):
    promedio_pelis = suma_promedio_voto/numero_peliculas_director

#print("Peliculas dirigidas por "+ director +": " + str(peliculas['title'])) Encontrar los nombres de las peliculas
print("Numero de películas de "+ director + ": " + str(numero_peliculas_director)
print("Promedio de calificación de las peliculas del director: " + str(promedio_pelis))


"""




#FUNCION 5

print("1- Req 5 - Entender un género")

genero = input('inserte el género de su interes: ')

peliculas_del_genero = lt.newList('SINGLE_LINKED', None)

iter = listiterator.newIterator(details)
while listiterator.hasNext(iter):
    d = listiterator.next(iter)
    if genero in d["genres"]:
        lt.addFirst(peliculas_del_genero, d)
        print(d)


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

#print("Peliculas dirigidas por "+ director +": " + str(peliculas['title'])) Encontrar los nombres de las peliculas
print("Numero de películas asociadas al género  "+ genero + ": " + str(numero_peliculas_genero))
print("Promedio de votación de las peliculas del género " + genero +": "+ str(promedio_vote_count))

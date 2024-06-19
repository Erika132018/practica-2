import sys
sys.path.append('../')
import random
import time
from controls.tda.linked.linkedList import Linked_List

try:

    lista = Linked_List()

    for i in range(20000):
        lista.add(round(random.random() * 1000, 2))
    data = round(random.random() * 1000, 2)
    inicio_total = time.time()
    inicio_sort = time.time()
    #lista.sort(1,algoritmo=1) #-->QuickSort
    #lista.sort(1,algoritmo=2) #-->MergeSort
    #lista.sort(1,algoritmo=0) #-->ShellSort
    #----------Metodos de Busqueda----------
    #lista.binary_search(data, type=1)
    lista.binary_search_secuencial(data, type=1)
    #lista.binary_search( 1, type=1)
    #print(lista)
    fin_sort = time.time()
    tiempo_total = fin_sort - inicio_total

    #print("Tiempo de ejecución total (QuickSort ascendente): ", tiempo_total)
    #print("Tiempo de ejecución total (MergeSort ascendente): ", tiempo_total)
    #print("Tiempo de ejecución total (ShellSort ascendente): ", tiempo_total)
    #print("Tiempo de ejecución (binary_search): ", tiempo_total)
    print("Tiempo de ejecución (binary_search_secuencial): ", tiempo_total)


except Exception as error:
      print(error)
lista = [8.17, 90, 1, 5, 5, 44, 1.32]
lista.sort() #Para ordenar de forma ascendente y descendente lista.sort(reverse=True)
menor = min(lista) #Para sacar el menor
mayor = max(lista) #Para sacar el mayor
longitud = len(lista) #Longitud de la lista
resultado = 8 in lista #Esto es para saber si el numero 8 se encuentra en la lista, utilizamos "in" boolean
indice = lista.index(8.17) #No informa en que posicion o indice se encuentra el valor
contador = lista.count(5) #nos informa cuantas veces esta el valor en la lista
print(lista)
print(menor)
print(mayor)
print(longitud)
print(indice)
print(contador)
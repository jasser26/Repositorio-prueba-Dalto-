#Lis(Funcion) Crea una Lista

lista = list(["hola", "dalto",24])

#len (devuelve la cantidad de elemtos de la lista)

resultado = len(lista)

#Append Agrega elementos a la lista con append

agregando_con_append = lista.append("JAJAJAJA")

#Insert agrega un elemento en un indice especifico

lista.insert(2,"Toma amigo")

#Agregando varios elementos a la lista
lista.extend([False, 2030])

#POP eliminado un elemento de la lista(por su indice)
print(len(lista))
lista.pop(0)

#Remove remueve un elemento por su valor

lista.remove("Toma amigo")

#clear este es nazi o sea elimina todos los elementos

#lista.clear()

#Sort ordena los elementos siempre y cuando no tenga cadena de texto
#lista.sort()
#lista.sort(reverse True)

#Reverse invierte los elementos de una lista

lista.reverse()         

print(lista)


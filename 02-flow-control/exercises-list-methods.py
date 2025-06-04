###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###
import os

os.system("cls")

def print_header(title : str, description : str):
    print('='*100)
    print('» ',title.upper())
    print('-'*100)
    print(description)
    print('='*100)


# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
print_header("Ejercicio 1"," Añadir y modificar elementos")
list_1 = [1,2,3,4,5]
list_1.append(6)
list_1.insert(1,10)
list_1[0] = 0
print(list_1)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().
print_header("Ejercicio 2","Combinar y limpiar listas")
lista_a.extend(lista_b)
print(lista_a)

removed_element = lista_a.pop(3)
print(removed_element)
lista_b.clear()

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.
print_header("Ejercicio 2","Combinar y limpiar listas")
list_2 = [1,2,3,4,5,6,7,8,9,10]
del list_2[2:5]
print(list_2)

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
print_header("Ejercicio 4","Ordenar y contar")
list_3 = [5, 2, 8, 1, 9, 4, 2]
list_3.sort()
# print(list_3)
print(list_3.count(2))
print( 7 in list_3 )


# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
print_header("Ejercicio 5","Copia vs Referencia")
list_4 = [1,2,3]
list_4_copy_slicing = list_4[:]
list_4_copy = list_4.copy()
referencia = list_4
referencia[0] = 10

print(list_4)
print(list_4_copy_slicing)
print(list_4_copy)
print(referencia)

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
print_header("Ejercicio 6", "Ordenar strings sin diferenciar mayúsculas y minúsculas.")
list_5 = ["Manzana", "pera", "BANANA", "naranja"]
list_5.sort(key=str.lower)
print(list_5)
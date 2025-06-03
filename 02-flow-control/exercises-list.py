
###
# EJERCICIOS
###

import os

os.system("cls")

def print_header(title : str, description : str):
    print('='*60)
    print('» ',title.upper())
    print('-'*60)
    print(description)
    print('='*60)


# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
print_header("Ejercicio 1", "El mensaje secreto")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
new_list = mensaje[-7:]
print("".join(new_list))

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
print_header("Ejercicio 2", "Intercambio de posiciones")
print(numeros)
numeros[0], numeros[-1] = numeros[-1], numeros[0]
print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
print_header("Ejercicio 3", "El sándwich de listas")
sandwich = []
sandwich += pan 
sandwich += ingredientes
sandwich += pan_abajo
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
print_header("Ejercicio 4", "Duplicando la lista")
new_list = lista[:]
new_list += lista[:]
print(new_list)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
print_header("Ejercicio 5", "Extrayendo el centro")
lista = [10, 20, 30, 40, 50]
middle = len(lista)//2
print(lista[middle])


# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
print_header("Ejercicio 6", "Reversa parcial")
lista = [1, 2, 3, 4, 5, 6]
reversed = lista[2::-1] + lista[3:]
print(reversed)
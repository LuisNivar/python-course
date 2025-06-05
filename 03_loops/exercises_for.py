
###
# EJERCICIOS (for)
###
import os
import math

os.system("cls")

def print_header(title : str, description : str):
    print('='*60)
    print('» ',title.upper())
    print('-'*60)
    print(description)
    print('='*60)


# # Ejercicio 1: Imprimir números pares
# # Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
# print_header("Ejercicio 1","Imprime numeros pares")
# for n in range(2,21,2):
#     print(n)

# # Ejercicio 2: Calcular la media de una lista
# # Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# # Calcula la media de los números usando un bucle for.
# print_header("Ejercicio 2","Calcular la media de una lista")
# lenght = 0
# acc = 0
# for n in numeros:
#     acc += n
#     lenght += 1

# print(acc/lenght)

# # Ejercicio 3: Buscar el máximo de una lista
# # Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# # Encuentra el número máximo en la lista usando un bucle for.
# print_header("Ejercicio 3", "Buscar el maximo de una lista")
# max = -math.inf
# for n in numeros:
#     if n > max:
#         max = n

# print(max)


# # Ejercicio 4: Filtrar cadenas por longitud
# # Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# # Crea una nueva lista que contenga solo las palabras con más de 5 letras
# # usando un bucle for y list comprehension.
# print_header("Ejercicio 4","Filtrar cadenas por longitud")
# large_words = [palabra for palabra in palabras if len(palabra) >= 5]
# print(large_words)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print_header("Ejercicio 5","Contar palabras que empiezan con una letra")
letter = None

while letter is None:
    letter = input("Enter one letter: ").lower()
    
    if(len(letter) == 0 or len(letter)> 1):
        letter = None
        print("I need ONE letter!")

print("-"*60)

counter = 0
for palabra in palabras:
    counter += 1 if palabra[0].lower() == letter else 0

print(counter)
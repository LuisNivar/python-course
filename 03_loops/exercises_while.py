###
# EJERCICIOS (while)
###
import os

os.system("cls")

def print_header(title : str, description : str):
    print('='*60)
    print('» ',title.upper())
    print('-'*60)
    print(description)
    print('='*60)


# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
# print_header("Ejercicio 1","Cuenta atrás")
# counter = 10
# while counter > 0:
#     print(counter)
#     counter -= 1

# # Ejercicio 2: Suma de números pares (while)
# # Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
# print_header("Ejercicio 2", "Suma de numeros pares (while)")
# counter = 0
# acc = 0
# while counter <= 20:
#     if(counter % 2 == 0):
#         acc += counter
#     counter +=1
    
# print(acc)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

# print_header("Ejercicio 3", "Factorial de un número")

# number = -1
# while number < 0:
#     number = int(input("Enter a positive number:\n"))

# counter = number
# factorial = 1
# while counter > 0:
#     factorial *= counter
#     counter -= 1

# print(f"!{number} = {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
# print_header("Ejercicio 4","Validación de contraseña")
# characters = 0

# while characters < 8:
#     password = input("Enter a password, with a least 8 characters:\n")
#     characters = len(password)
#     if characters < 8:
#         print("Invalid password!")
    
# print("Valid password!")


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
# print_header("Ejercicio 5","Tabla de multiplicar")
# input_val = None

# while input_val == None:
#     try:
#         input_val = int(input("Enter a number:\n"))
#     except:
#         print("This is not a number")

# counter = 1
# while counter <= 10:
#     print(f"{input_val} x {counter} = {input_val * counter}")
#     counter += 1

# # Ejercicio 6: Números primos hasta N
# # Pide al usuario que introduzca un número entero positivo N.
# # Imprime todos los números primos menores o iguales que N usando un bucle while.
print_header("Ejercicio 6","Números primos hasta N")
input_val = None
n = -1

while input_val == None or n <= 2:
    try:
        n = int(input("Enter a positive number: "))
        if(n <= 0):
            print("This is not a positive number")
        else:
            break
    except:
        print("This is not a number")

num = 2
while num <= n:
    is_prime = True
    divisor = 2
    while divisor  <= num ** 0.5:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(num)

    num += 1
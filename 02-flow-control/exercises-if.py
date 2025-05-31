###
# EJERCICIOS
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

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print_header("Ejercicio 1","Mayor de dos numeros")
input_a = input("Introduzca el primer número (a):\n")
a = int(input_a)
input_b = input("Introduzca el segundo número (b):\n")
b = int(input_b)
result = "a > b" if a > b else "b > a"
print(result)


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

print_header("Ejercicio 2", "Calculadora simple")
input_a, input_b= input("Introduzca el primer número (a), segundo número (b). Separado de punto y coma (;)\n").split(";")
a = int(input_a)
b = int(input_b)

permited_operation = "+-*/"
operation = " "

while operation not in permited_operation:
    operation = input("Introduzca la operacion:")

if b == 0 and operation == '/':
    print("Fatal error")
    exit()

if operation == "+":
    print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "*":
    print(a*b)
elif operation == "/":
    print(a/b)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print_header("Ejercicio 4", "Año bisiesto")
input_year = input("Enter a year:\n")
year = int(input_year)

is_mod4_zero = year % 4 == 0
is_mod100_zero= year % 100 == 0
is_mod400_zero = year % 400 == 0

is_valid_centenary = is_mod100_zero and is_mod400_zero

if (is_mod4_zero and not is_mod100_zero) or is_mod400_zero:
    print("Es bisiesto")
else:
    print("No es bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print_header("Ejercicio 5", "Categorizar edades")
input_age = input("Enter your:\n")
age = int(input_age)

if  age <= 2:
    print("Bebe")
elif age <=12:
    print("Niño")
elif age <=17:
    print("Adolescente")
elif age <=64:
    print("Adulto")
else:
    print("Adulto mayor")
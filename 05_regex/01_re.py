import re
import os

os.system("cls")

pattern = "Hello"
text = "Hello world"

result = re.search(pattern,text)
print(result)
print(result.group()) # type: ignore
print("-"*60)

if result:
    # .group() devuelve la cadena que coincide con el pattern
    print(result.group())

    # .start() devolver la posición inicial de la coincidencia
    print(result.start())

    # .end() devolver la posición final de la coincidencia
    print(result.end())

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
pattern = "midu"

matches = re.finditer(pattern,text)

print("-"*60)
for index, match in enumerate(matches):
    print(index, match.group(), match.start(), match.end())

# MODIFIERS

# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
pattern = "python"

matches = re.finditer(pattern,text, re.IGNORECASE)

print("-"*60)
for index, match in enumerate(matches):
    print(index, match.group(), match.start(), match.end())

# REPLACE TEXT

text = "Hello everybody. Hello again."
pattern = "Hello"
replacement = "Good bye"

result = re.sub(pattern, replacement, text)
print(text)
print(result)
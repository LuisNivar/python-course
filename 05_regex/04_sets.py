import os
import re

os.system("cls")

# email = "elmanindelflow@gmail.com"

# text = "Agua pasa por mi casa, cate de mi corazón"
# pattern = r"[aeiou]"

# vowels = re.findall(pattern, text)
# print(vowels)

# print("-"*80)
# text = "man ran ban ñan lan san wan"
# pattern = r"[rbm]an"
# matches = re.findall(pattern, text)
# print(matches)

# print("-"*80)
# # Ejercicio:
# # Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# # Solo queremos las palabras man, fan y ban
# text = "omniman fanatico man bandana fantastic fan ban "
# pattern = r"\b[mfb]an\b"
# matches = re.findall(pattern, text)
# print(matches)


# print("-"*80)
# text = "1563498"
# pattern = r"[1-5]"
# matches = re.findall(pattern, text)
# print(matches)


# print("-"*80)
# text = "dsd 156349dasd8ABB"
# pattern = r"[a-z]"
# matches = re.findall(pattern, text)
# print(matches)

# print("-"*80)
# text = "dsd 156349dasd8ABB"
# pattern = r"[a-zA-z]"
# matches = re.findall(pattern, text)
# print(matches)

# print("-"*80)
# text = "dsd 15349dasd8ABB"
# pattern = r"[a-zA-z0-9]"
# matches = re.findall(pattern, text)
# print(matches)
print("-"*80)


# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
"lo.que+sea@shopping.online"
"michael@gov.co.uk"

url = "michael@gov.co.uk"
url_patter = r"[\w._%+-]+@[\w.-]+\.[a-zA-A]{2,6}"
match = re.findall(url_patter, url)
print(match)


# # ^ -> Coincide con todo lo que no esté entre corchetes | negación
# print("-"*80)
# text = "dsd 156349dasd8ABB"
# pattern = r"[^a-zA-z]"
# matches = re.findall(pattern, text)
# print(matches)
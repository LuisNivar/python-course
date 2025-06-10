import os
import re

os.system("cls")

# * -> Puede aparecer 0 o más veces
text = "aabcddd"
pattern = r"a*"

matches = re.findall(pattern,text)
print(matches) # -> ['aa', '', '', '', '', '', '']

# Ejercicio 1:
# ¿Cuantas palabras tienen de 0 a más "a" y después una b?
print("-"*60)
text = "abaco abeja acera acero acabar bien"
pattern = r"\ba*b\w+\b"

matches = re.findall(pattern, text)
print(matches)

# + -> Debe aparecer 1 a más veces
print("-"*60)
text = "aaa bb c a"
pattern = r"a+"

matches = re.findall(pattern, text)
print(matches)

# ? -> Debe aprecer 0 a más veces
print("-"*60)
text = "aaba ca ba ab b a"
pattern = r"a?b"

matches = re.findall(pattern, text) # ['ab', 'b', 'ab', 'b']
print(matches)


# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
print("-"*60)
phone = "+34 688999999"
pattern = r"\+34 \d{9}"

matches = re.findall(pattern, phone) # ['ab', 'b', 'ab', 'b']
print(matches)

# {n} -> Exactamente n ocurencias
print("-"*60)
text = "aaab aaaa abaaa" # ['aaa', 'aaa', 'aaa']
pattern = r"a{3}"
matches = re.findall(pattern, text) # 
print(matches)

# {n,m} -> De n a m ocurencias
print("-"*60)
text = "aaab aaaa abaaa aa ba ab" # ['aaa', 'aaa', 'aaa', 'aa']
pattern = r"a{2,3}"
matches = re.findall(pattern, text) # 
print(matches)

# Ejercicio:
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
print("-"*60)
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches)

# Ejercicio
# Encuentra las palabras de más de 6 letras
print("-"*60)
words = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches)
print("-"*60)
import re
import os

os.system("cls")

text = "Hola, H0la H%la hoLA..."
pattern = "h.la"

# . -> Cualquier caracter 

found = re.findall(pattern, text, re.IGNORECASE)
print(found)

print("-"*60)

text = "Eso, essso, elo, eno, entro"
pattern = "e.o"
matches = re.findall(pattern, text)
print(matches)

print("-"*60)

text = "El pequeño zorro. Un pez lo vio saltar una valla."
pattern = r"\."
matches = re.findall(pattern, text)
print(matches)

print("-"*60)

# \d -> Para numeros

text = "Mi numero de telefono es 8998888888"
pattern = r"\d{10}"
matches = re.findall(pattern, text)
print(matches)

print("-"*60)

text = "El sujeto tenia 18 años de edad y 153 libras y media 1.75 metros"
pattern = r"\d"
matches = re.findall(pattern, text)
print(matches)

print("-"*60)

text = "Mi numero de telefono es +1 8998888888"
pattern = r"\+1 \d{10}"
matches = re.search(pattern, text)
if matches:
    print(matches.group())


print("-"*60)

text = "Uvuvwevwevwe Onyetenyevwe Ugwemuhwem Osas"
pattern = r"\w"
matches = re.findall(pattern, text)
print(matches)

print("-"*60)

# s -> Espacios en blanco, tabulaciones, saltos de linea

text = "Uvuvwevwevwe Onyetenyevwe\nUgwemuhwem\tOsas"
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)

# ^ -> Coincide con el inicio de una cadena
print("-"*60)

username = "%Pepito689"
pattern = r"^\w"
valid = re.search(pattern, username)

if(valid):
    print("Valid user name")
else:
    print("User name invalid")

# ^ -> Coincide con el inicio de una cadena
print("-"*60)

phone = "+1 8998888888"
phone_pattern = r"^\+\d{1,3} "
valid = re.search(phone_pattern, phone)

if(valid):
     print("Valid phone number")
else:
    print("Not valid phone number")

# $ -> Coincide con el final de una cadena
print("-"*60)

text = "Necesito que me prestes $500, por favor"
pattern = r"por favor$"

valid = re.search(pattern, text)

if(valid):
     print("Not problem")
else:
    print("Noup")


# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\w+\.txt"
print("-"*60)

result = re.findall(pattern, files)
print(result)

# b -> Coincide con el principio y/o final de una palabra
print("-"*60)
text = "casa casado cosa casada acasa ocasa casa"
pattern = r"\bc.sa\b"

result = re.findall(pattern, text)
print(result)

#  | -> Coincidir con una cosa u otra
print("-"*60)
text = "Me gusta la piña. El ananá es bueno. Sin tilde tambien anana"
pattern = r"piña|anana|ananá"

result = re.findall(pattern, text)
print(result)

print("-"*60) 
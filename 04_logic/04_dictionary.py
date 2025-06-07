import os 
os.system("cls")

person = {
    "name": "John",
    "last_name": "Doe",
    "age" : 25,
    "skills" : ["css","js","html","ts"],
    "socials" : {
        "x" : "@johndoe",
        "facebook" : "johndoe",
        "instagram" : "@johndoe245"
    },
    "height": 170,
    "is_student" : True
} 

print("-"*60)
print(person["name"])
print(person["age"])
print(person["socials"]["x"]) 
print(person["skills"])
print(person["height"])
print("-"*60)  

# DELETE KEY
print(person) 
del person["height"]
print("")
print(person) 

print("-"*60) 
print(person["is_student"])

is_student = person.pop("is_student")
print(is_student)
print("")
print(person) 

# UPDATE
a = {"name" : "Jose", "age": 15}
b = {"name" : "Pablo", "age": 27}

print("a =", a)
print("b =", b)

print("")
a.update(b)
print("a =", a)
print("-"*60) 

# KEY 
print("name" in a)
print("size" in a)
print("")

print(person.keys(), "\n")
print(person.values(), "\n")
print(person.items(), "\n") # tuple
print("-"*60) 

for key, value in person.items():
    print(f"• {key}: {value}")
print("")
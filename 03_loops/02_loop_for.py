print("-"*60)
fruits = ["apple","lemon","pear"]
for fruit in fruits:
    print(fruit)

print("-"*60)
name = "Manolito"
for char in name:
    print(char)

print("-"*60)

# ENUMERATE

for index, fruit in enumerate(fruits):
    print(index, fruit)
print("-"*60)

# NESTED FOR

cols = ["A","B","C","D"]
rows = [1,2,3,4]

for c in cols:
    for r in rows:
        print(f"{c}{r} ",end="")
    print("") 

# BREAK
print("-"*60)
animals = ["cat","dog", "pigeon","pig","parrow","horse","mare"]

for index, animal in enumerate(animals):
    print(index, animal)
    if(animal == "pig"):
        break

# CONTINUE
print("-"*60)
animals = ["cat","dog", "pigeon","pig","parrow","horse","mare"]

for index, animal in enumerate(animals):
    if(animal == "pig"):
        continue
    
    print(index, animal)
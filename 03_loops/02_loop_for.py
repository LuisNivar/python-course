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


# LIST COMPREHENSION
print("-"*60)
#animals_upper = [animal.upper() for animal in animals]
animals_upper = [_.upper() for _ in animals]
print(animals_upper)
print("-"*60)
numbers = [_ for _ in range(9)]
print(numbers)
even = [_ for _ in range(20) if _ % 2 == 0]
print(even)

# range -> iterable NOT list
print("-"*60)
nums = range(10)
print(nums)
list_of_nums = list(nums)
print(list_of_nums)
print("-"*60)
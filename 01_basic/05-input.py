name = input("What's your name?\n")
print(f"Hello {name}")

input_age = input("What's your age?\n")
age = int(input_age)

print(f"Your age in 5 years will be {age + 5}")

country, city = input("What counry and city do you live in?\n").split() 
print(f"{country} is a great country and {city} it's pretty good.")

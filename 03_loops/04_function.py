import os
os.system("cls")

# print("-"*60)

# def greet():
#     print("Hi!")

# greet()
# print("-"*60)

# def greet_to(name):
#     print(f"Hi, {name}!")

# greet_to("Manolo")
# greet_to("Tom")

# print("-"*60)

# def sum(a,b):
#     return a + b

# result = sum(2,3)
# print("sum(2,3) =", result)

# print("-"*60)

# def diff(a,b):
#     """Difference between a and b"""
#     return a - b


# print(diff(5,2))
# print(diff.__doc__)

# print("-"*60)

# help(diff)

# print("-"*60)
# def pow(base, exponent = 2):
#     return base ** exponent

# print(pow(3))
# print(pow(4,3))

print("-"*60)
# POSITIONAL PARAMS
def description(name, age, country):
    print(f"Hi! I'm {name}, I'm {age} years old. I live in {country}")

description("Mark",18,"Chicago")

description(18,"Paris","Josep")

# KEY PARAMS / NAMED ARGUMENTS
description(age=18,country="Paris",name="Josep")

# VARIABLE LENGTH ARGUMENTS
print("-"*60)
def sum_two(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

result = sum_two(1,2,3,4)
print(result)

# KEY-VALUE ARGUMENTS
print("-"*60)
def description_of(**kargs):
    for key, value in kargs.items(): # tuple
        print(f"{key}: {value}")

description_of(name="John",age="25",profession="Dev")
print("")
description_of(weight=185.5, color="red", shape="sphere")
print("-"*60)
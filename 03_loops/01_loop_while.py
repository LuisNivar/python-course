import os
os.system("cls")

# # WHILE
# counter = 0

# while counter <= 5:
#     print(counter)
#     counter += 1

# print("-"*60)

# # BREAK
# counter = 0
# while counter <= 100:
#     print(counter)
#     counter += 1
#     if(counter % 5 == 0):
#         print("multiple of 5")
#         break

# print("-"*60)

# # CONTINUE
# counter = 0
# while counter < 20:
#     counter += 1
#     if(counter % 2 == 0):
#         continue
#     print(counter)

# # WHILE ELSE
# counter = 0

# while counter <= 5:
#     print(counter)
#     counter += 1
# else:
#     print("Loop has ended") # like a finally

# print("-"*60)

# counter = 0
# while counter <= 100:
#     print(counter)
#     counter += 1
#     if(counter % 5 == 0):
#         print("multiple of 5")
#         break
# else:
#      print("Loop has ended") # does not work with "break"

## REAL USE
# print("-"*60)
# number = -1
# while number < 0:
#     number = int(input("Enter a positive number:\n"))
#     if(number < 0):
#         print("This isn't a positive number")
# else:
#      print(f"Your number is {number}") # does not work with "break"

## TRY EXCEPT
print("-"*60)
number = -1
while number < 0:
    try:
        number = int(input("Enter a positive number:\n"))
        if(number < 0):
            print("This isn't a positive number")
    except:
        print("This isn't a number")
else:
     print(f"Your number is {number}") # does not work with "break"

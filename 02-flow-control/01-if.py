import os
os.system("cls")

age = 18
if age >= 18:
    print("You're an adult!")
else:
    print("You're a kid!")


calification = 72
if calification >= 90:
    print('A')
elif calification >= 80:
    print('B')
elif calification >= 75:
    print('C')
elif calification >= 70:
    print('D')
else:
    print('F')


## && => and 
## || => or
## !  => not

# Ternary 
customer_age = 25
message = "You can buy it" if customer_age >= 18 else "You can't buy it"
print("» ", message)
import os
os.system("cls")

list_1 = [1,2,3,4,5,6]
list_2 = ["a","b","c"]
list_3 = [1, "a", True]
list_4 = [[1,2],[3,4]]

print("list_1 = ",list_1)
print("list_2 = ",list_2)
print("list_3 = ",list_3)
print("list_4 = ",list_4)


print("list_1[1]: ",list_1[1])
print("list_2[0]: ",list_2[0])
print("list_4[1][0]: ",list_4[1][0])
print("-"*30)

print("list_1[1:3]: ",list_1[1:3]) # no inclusive
print("list_1[:3]: ",list_1[:3]) 
print("list_1[3:]: ",list_1[3:]) # index 3 → to end
print("list_1[:]: ",list_1[:]) # copy 
print("-"*30)

print("list_1[::2]: ",list_1[::2]) # index even (0,2,4...)
print("list_1[::-1]: ",list_1[::-1]) # revert
print("list_1[1::2]: ",list_1[1::2])
print("-"*30)

print("list_1 + list_2 = ", list_1 + list_2)

list_1 += list_2 # best way
print("list_1 += list_2 = ", list_1)
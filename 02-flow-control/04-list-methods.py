import os
os.system("cls")

print("-"*100)
list_1 = [0,1,2,3,4]
# ADD
print("list_1 = ",list_1)
list_1.append(5)
print("list_1.append(5) : ",list_1)
print("-"*100)
list_1.extend([6,7,8])
print("list_1.extend([6,7,8]) : ",list_1)
print("-"*100)
list_2 = ["a","b","c","d","f","h","i","j"]
print('list_2 = ["a","b","c","d","f"]', list_2)
print("-"*100)
# REMOVE
list_2.remove("b") # remove first occurence
print('list_2.remove("b") : ', list_2)
print("-"*100)
list_2.pop(3) # remove by index
print('list_2.pop(3) : ', list_2)
print("-"*100)
del list_2[-1] 
print('del list_2[-1] : ', list_2)
del list_2[::2]
print('del list_2[::2] : ', list_2) # delete by range
print("-"*100)

#SORT
list_3 = [1,8,9,2,6,7,0,11]
print("list_3 =",list_3)
print("-"*100)
list_3.sort()
print("list_3.sort(): ", list_3) 
sorted_list_3 = sorted(list_3) # return a new sorted list from original
print("sorted_list_3 = sorted(list_3)",sorted_list_3) 
list_4 = ["apple", "pear","orange","banana"] # ascii comparation 
list_5 = ["Apple", "pear","Orange","banana"] # ascii comparation

print("list_4 =",list_4)
print("list_5 =",list_5)

list_4.sort()
list_5.sort()


print("list_4 =",list_4)
print("list_5 =",list_5)


## Utils 
list_6 = ["$","%","^","&","%"]
has_money = "$" in list_6
print("has_money =", has_money)
print(list_6.count("%")) 
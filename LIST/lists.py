lst1=[1, 'sravan', 10.9]
lst2 =[90,20,50,100,8,0]
lst3 =[5,89,3,99,23,7]


print(lst1)
print(lst1[2])
print(lst1+lst2)
print(lst1*5)
print(max(lst2))
print(min(lst2))
print(len(lst2))
print(lst2[:])                              # prints all in the list
print(lst2[1:3])
print(lst2[-1])                              # prints the last one
for i in lst2:                               # looping
  print(i)

print(lst1.remove(10.9))                    # remove the element
print(lst1)

lst1.append('hyderabad')                    # ADDing to the list append
print(lst1)

lst1[2]=15.9                                #updating data or replacing data
print(lst1)

del lst2[2]                                  # delete the element in the list
print(lst2)

print(tuple(lst1))                         # to convert list in to tuple

print(lst1.clear())                         # clears all the elements

print(lst1.copy())                           #copys all the elements         

print(lst3.sort())

print(lst3.reverse())
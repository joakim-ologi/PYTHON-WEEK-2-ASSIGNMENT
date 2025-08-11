#empty list
my_list = []
#add new values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
#insert a value at the second positioning
my_list.insert(1, 15)
print(my_list)
#extend the list with another list
my_list.extend([50, 60, 70])
#remove the last  element from my list
my_list.pop()
print(my_list)
#sorting list from ascending order
my_list.sort()
#find index of a value
print(my_list.index(30))

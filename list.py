my_list =[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
my_list.insert(1, 15)
print(my_list)
# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print(my_list)
# Remove the last element from my_list
my_list.pop()
# Remove the last element from my_list
print(my_list)
# Sort my_list in ascending order
my_list.sort()
# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
print(my_list)
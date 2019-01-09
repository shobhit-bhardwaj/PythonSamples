'''
@author: Shobhit Bhardwaj
'''

my_list = ['One ', 'Two', 'Three', 'Four', 'Five']
print(my_list)

print(my_list[1])
print(my_list[1:])
print(my_list[1:4])
print(my_list[1:4:2])
print(my_list[::-1])

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = list1 + list2
print(list3)

list3[0] = 9
print(list3)

list3.append(6)
print(list3)

popped = list3.pop()
print(popped)
print(list3)

popped = list3.pop(0)
print(popped)
print(list3)

my_list = [7, 1, 4, 9, 0, 4, 5]
my_list.sort()                      #    Inplace Method
print(my_list)

my_list.reverse()                      #    Inplace Method
print(my_list)

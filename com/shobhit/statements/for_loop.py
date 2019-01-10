'''
@author: Shobhit Bhardwaj
'''

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for value in my_list:
    print(value)

name = 'Shobhit Bhardwaj'
for letter in name:
    print(letter)

my_list = [[1, 2], [3, 4], [5, 6]]
for (a, b) in my_list:
    print(f'{a} - {b}')

my_tuple = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in my_tuple:
    print(f'{a} - {b} - {c}')

my_dict = {'k1':'v1', 'k2':'v2', 'k3':'v3'}
for (key, val) in my_dict.items():
    print(f'Key - {key} -> Value - {val}')

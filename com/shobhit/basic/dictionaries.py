'''
@author: Shobhit Bhardwaj
'''

my_dict = {'k1':'v1', 'k2':'v2', 'k3':'v3'}
print(my_dict)

my_dict['k4'] = 'v4'
print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_dict = {'k1':'v1', 'k2':50, 'k3':[100, 200, 300], 'k4':{'a':'x', 'b':'y', 'c':'z'}}
print(my_dict['k1'])
print(my_dict['k2'])
print(my_dict['k3'][1])
print(my_dict['k4']['b'])

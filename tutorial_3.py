#create lists, sets, and dictionaries in python and perform operations like adding element, removing elements, and accessing elements.

my_list = [1, 2, 3]
my_list.append(4)
element_list = my_list.pop(1)
print(element_list)

my_set = {1, 2, 3}
element_set = 2
if element_set in my_set:
    my_set.remove(element_set)
    print(element_set)

my_dict = {'a': 1, 'b': 2, 'c': 3}
element_dict = my_dict.pop('b')
print(element_dict)
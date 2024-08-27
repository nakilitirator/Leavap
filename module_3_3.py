def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params('ABC', True, (8, 9))
print_params(b = 25)
print_params(c = [1,2,3])

print()

values_list = ('ABC', True, (8, 9))
values_dict = {'a': 1, 'b': 'строка', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [25.25, 'cтрока']
print_params(*values_list_2, 42)


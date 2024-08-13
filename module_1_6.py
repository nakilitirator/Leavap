my_dict = {'Pavel': 2000, 'Maria': 2001,'Dima': 1996}
print(my_dict)
print(my_dict['Pavel'])
print(my_dict.get('Alex', 'Такого ключа нет'))
my_dict.update({'Dory': 1990,
                'Panny': 2005})
print(my_dict.pop('Dory'))
print(my_dict)

my_set = {1, 2, 3, 'Pavel', 4, 1, 2, 3, 4, 'Pavel'}
print(my_set)
my_set.add(tuple([1, 2, 3]))
my_set.add(True)
my_set.discard(1)
print(my_set)


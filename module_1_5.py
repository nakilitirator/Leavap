immutable_var = (1, 2, True, 'String')
print (immutable_var)
# immutable_var[0] = 2 -- Картеж - неизменное хранилище, каждый элемент которого постоянен. Исключение: изменяемые объекты (списки) в картеже, элементы которых можно менять.
print(type(immutable_var))
mutable_list = ([1, 2, 3, 4], 5) + (6, 7)
print(mutable_list)
mutable_list[0][0] = 23
mutable_list[0][2] = 35
print(mutable_list)
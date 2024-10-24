class StepValueError(ValueError): # пользовательский класс исключения, который наследуется от ValueError.
    #print('шаг не может быть равен 0')
    pass

class Iterator:

    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        else:
            self.step = step # шаг с которой совершается итерация
        self.start = start # целое число с которого начинается итерация
        self.stop = stop # целое число на котором заканчивается итерация


    def __iter__(self):
        self.pointer = self.start # сбрасываем значение pointer на start
        return self # возвращаем сам объект итератора

    def __next__(self): # метод увеличивающий атрибут pointer на step
        if self.step > 0:
            if self.pointer > self.stop: # pointer станет больше stop
                raise StopIteration()
        else:
            if self.pointer < self.stop: # pointer станет меньше stop
                raise StopIteration()
        self.pointer += self.step # увеличиваем атрибут pointer на step
        return self.pointer - self.step


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
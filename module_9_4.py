#  Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda _first, _second: [a == b for a in _first for b in _second], first, second)))


# Замыкание
def get_advanced_writer(file_name): # file_name - параметр принимающий название файла для записи
    def write_everything(*data_set): # *data_set - параметр принимающий неограниченное количество данных любого типа.
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.writelines(str(data) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__
class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        from random import choice
        return choice(self.words)


# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
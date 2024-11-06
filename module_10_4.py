import random
from threading import Thread
from time import sleep
from queue import Queue


class Table(): # Класс, который хранит информацию о находящемся за ним Guest.
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread): # Класс-поток, при запуске которого происходит задержка от 3 до 10 секунд.
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        pause =  random.randint(3, 10)
        sleep(pause)


# Класс Cafe - кафе, в котором есть определённое кол-во столов
# и происходит имитация прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).
class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f'{guest.name} сел(а) за стол номер {table.number} ')
                    table.guest.start()
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди.')

    def discuss_guests(self):
        while True:
            for table in self.tables:
                if (not self.queue.empty()) and (table.guest is None):
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()
                if (not table.guest is None) and (table.guest.is_alive()):
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
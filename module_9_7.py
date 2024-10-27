def is_prime(func):

    # Функция-декоратор, которая распечатывает "Простое",
    # если результат 'обёрнутой' функции будет простым числом и
    # "Составное" в противном случае.


    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        sum_ = sum(args)

        n = 0
        for i in range(2, sum_ // 2 + 1):
            if sum_ % i == 0:
                n += 1
        if n <= 0:
            print("Простое")
        else:
            print("Составное")
        return result

    return wrapper


@is_prime # декоратор для функции sum_three
def sum_three(*args): # Функция складывает 3 числа
    return sum(args)


if __name__ == "__main__":
    result = sum_three(2, 3, 6)
    print(result)
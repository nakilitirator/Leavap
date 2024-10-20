def add_everything_up(a, b):
    """
    Сложение разных типов даннных: a и b,
    которые могут быть как числами(int, float),
                       так и строками(str).
    """
    try:
        return round((a + b), 3)  # округление, т.к. много знаков после запятой
    except TypeError:
        if isinstance(a, str):
            return a + str(b)
        else:
            return str(a) + b


if __name__ == "__main__":
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))
    print(add_everything_up('Urban', '-university'))

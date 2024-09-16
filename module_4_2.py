def test_function():
        def inner_function():
            print('Я в области видимости функции test_function')

        inner_function()


#inner_function() # В глобальном пространстве функцию inner_function не видно, она находится внутри функции test_function.

test_function()


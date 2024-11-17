def introspection_info(obj): # Функция для подробной интроспекции принимаемого объекта
    obj_type = type(obj).__name__ # определить ТИПы объекта
    attributes = dir(obj) # определить АТРИБУТы объекта
    methods = [method for method in attributes if callable(getattr(obj, method))] # определить МЕТОДы объекта
    module = obj.__class__.__module__ # определить МОДУЛЬ, к которому принадлежит объект

    # Определим ссылку на словарь, который будет содержать информацию об объекте
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module},
    return info


number_info = introspection_info(42)
print('Интроспекция числа:', number_info)

string_info = introspection_info('Hello')
print('Интроспекция строки:', string_info)

list_info = introspection_info([1, 20, 4.0, 'word'])
print('Интроспекция списка:', list_info)
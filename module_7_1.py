import os.path


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        if os.path.exists(self.__file_name):
            file = open(self.__file_name, 'r')
            result = file.read()
            file.close()
            return result
        file = open(self.__file_name, 'w')
        file.close()
        return ""

    def add(self, *products):
        file_products = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name in file_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(product.__str__() + "\n")
        file.close()


if __name__ == "__main__":

    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
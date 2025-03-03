class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                products = file.read()
            return products.strip()
        except FileNotFoundError:
            with open(self.__file_name, 'w'):
                pass
            return ""

    def add(self, *products):
        current_products = self.get_products()
        with open(self.__file_name, 'a') as file:
            for el in products:
                if str(el) in current_products:
                    print(f"Продукт {str(el)} уже есть в магазине")
                else:
                    file.write(str(el) + '\n')


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

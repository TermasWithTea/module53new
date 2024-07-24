class House:
    houses_history = []

    def __new__(cls,*args,**kwargs):
        obj = super().__new__(cls)
        cls.houses_history.append(args[0])
        return obj

    def __init__(self, name, number_of_flour):
        self.value = None
        self.name = name
        self.number_of_flour = number_of_flour

    def go_to(self, new_flour):
        if 1 <= new_flour <= self.number_of_flour:
            for floor in range(1, new_flour + 1):
                print(f"прибытие на {floor} этаж")
        else:
            print("такого этажа не существует")

    def __len__(self):
        return self.number_of_flour

    def __str__(self):
        return (f'Название:{self.name}, кол-во этажей:{self.number_of_flour}')

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_flour == other.number_of_flour

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_flour < other.number_of_flour
        else:
            return self.number_of_flour < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_flour <= other.number_of_flour
        else:
            return self.number_of_flour <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_flour > other.number_of_flour
        else:
            return self.number_of_flour > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_flour >= other.number_of_flour
        else:
            return self.number_of_flour >= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.name != other.name
        else:
            return self.name != other

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_flour += value
            return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_flour += value
            return self

    def __iadd__(self, value):
        if isinstance(value,int):
            self.number_of_flour += value
            return self

    def __del__(self):
        print(f'{self.name}снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)


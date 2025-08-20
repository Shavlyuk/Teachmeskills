# =============================
# Домашняя работа: ООП на Python
# TeachMeSkills.by
# =============================

# Задание 1. Класс «Товар» и «Склад».
#
# Класс «Товар» содержит закрытые поля:
# - название товара
# - название магазина
# - стоимость в рублях
#
# Класс «Склад» содержит массив товаров.
#
# Обеспечить возможности:
# ✅ Вывод информации о товаре со склада по индексу
# ✅ Вывод информации о товаре со склада по имени
# ✅ Сортировка товаров по названию, по магазину и по цене
# ✅ Перегрузка сложения товаров по цене


# === TODO: реализовать класс Product ===
class Product:
    def __init__(self, name, shop, price):
        # TODO: сохранить значения в закрытые поля
        self.__name = name
        self.__shop = shop
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def store(self):
        return self.__shop

    @property
    def price(self):
        return self.__price


    def __str__(self):
        # TODO: вернуть читаемую строку с данными товара
        return f"Товар: {self.__name}, Магазин: {self.__shop}, Цена: {self.__price} руб."

    # TODO: перегрузить оператор сложения (__add__), чтобы возвращалась сумма цен двух товаров
    def __add__(self, other):
        if isinstance(other, Product):
            return self.__price + other.__price
        elif isinstance(other, (int, float)):
            return self.__price + other
        else:
            raise TypeError("Не поддерживается сложение с этим типом")

# === TODO: реализовать класс Warehouse ===
class Warehouse:
    def __init__(self):
        # TODO: создать список товаров
        self.__products = []

    def add_product(self, product):
        # TODO: добавить товар на склад
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    def get_by_index(self, index):
        # TODO: вернуть информацию о товаре по индексу
        if 0 <= index < len(self.__products):
            return self.__products[index]
        else:
            raise IndexError("Неверный индекс")

    def get_by_name(self, name):
        # TODO: вернуть информацию о товаре по имени
        for product in self.__products:
            if product.name == name:
                return product
        return None

    def sort_by_name(self):
        # TODO: отсортировать по названию
        self.__products.sort(key=lambda x: x.name)

    def sort_by_shop(self):
        # TODO: отсортировать по магазину
        self.__products.sort(key=lambda x: x.store)

    def sort_by_price(self):
        # TODO: отсортировать по цене
        self.__products.sort(key=lambda x: x.price)


# === Тесты для задачи 1 ===
print("=== Задача 1: Склад ===")
w = Warehouse()
p1 = Product("Молоко", "Пятерочка", 70)
p2 = Product("Хлеб", "Магнит", 40)
p3 = Product("Сыр", "Пятерочка", 300)

w.add_product(p1)
w.add_product(p2)
w.add_product(p3)

print(w.get_by_index(1))
print(w.get_by_name("Сыр"))

# TODO: протестировать сортировку и сложение p1 + p2
total_price = p1 + p2
print(f"Общая стоимость товаров {p1.name} и {p2.name}: {total_price} руб.")

# =============================
# Задание 2. Класс «ПчёлоСлон».
#
# Инициализируется двумя числами:
# - часть пчелы
# - часть слона
#
# Методы:
# ✅ Fly() – True, если часть пчелы >= части слона
# ✅ Trumpet() – "tu-tu-doo-doo", если часть слона >= пчелы, иначе "wzzzz"
# ✅ Eat(meal, value) – meal только "nectar" или "grass".
#   - если nectar: у слона уменьшается, у пчелы увеличивается
#   - если grass: наоборот
#   - нельзя выйти за пределы 0–100


# === TODO: реализовать класс BeeElephant ===
class BeeElephant:
    def __init__(self, bee_part, elephant_part):
        # TODO: сохранить bee_part и elephant_part
        self.bee = max(0, min(100, bee_part))
        self.elephant = max(0, min(100, elephant_part))

    def fly(self):
        # TODO: реализовать логику Fly
        return self.bee >= self.elephant

    def trumpet(self):
        # TODO: реализовать логику Trumpet
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        # TODO: реализовать логику Eat
        if meal == "nectar":
            self.elephant = max(0, self.elephant - value)
            self.bee = min(100, self.bee + value)
        elif meal == "grass":
            self.bee = max(0, self.bee - value)
            self.elephant = min(100, self.elephant + value)
        self.bee = max(0, min(100, self.bee))
        self.elephant = max(0, min(100, self.elephant))


# === Тесты для задачи 2 ===
print("\n=== Задача 2: ПчёлоСлон ===")
be = BeeElephant(30, 70)
print(be.fly())            # False
print(be.trumpet())        # tu-tu-doo-doo
be.eat("nectar", 20)       # должно изменить пропорции
print(be.fly())            # возможно True


# =============================
# Задание 3. Класс «Автобус».
#
# Свойства:
# ✅ скорость
# ✅ макс. кол-во мест
# ✅ макс. скорость
# ✅ список фамилий пассажиров
# ✅ флаг наличия свободных мест
# ✅ словарь мест (номер: фамилия)
#
# Методы:
# ✅ посадка/высадка одного или нескольких пассажиров
# ✅ увеличение/уменьшение скорости на заданное значение
# ✅ операции:
#   - `in` проверяет фамилию в списке
#   - `+=` посадка
#   - `-=` высадка


# === TODO: реализовать класс Bus ===
class Bus:
    def __init__(self, max_seats, max_speed):
        # TODO: инициализировать поля
        self.speed = 0
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passenger_list = []
        self.has_free_seats = True
        self.seats = {i: None for i in range(1, max_seats + 1)}

    def board(self, *passengers):
        for name in passengers:
            if not self.has_free_seats:
                print(f"Нет свободных мест! {name} не сел")
                continue
        for item in passengers:
            if isinstance(item, (list, tuple)):
                self.board(*item)  # Рекурсивная распаковка
            else:
                for seat_num, passenger in self.seats.items():
                    if passenger is None:
                        self.seats[seat_num] = item
                        self.passenger_list.append(item)
                        self.update_seats()
                        break

    def unboard(self, *passengers):
        for item in passengers:
            if isinstance(item, (list, tuple)):
                self.unboard(*item)  # Рекурсивная распаковка
            else:
                for seat_num, passenger in self.seats.items():
                    if passenger == item:
                        self.seats[seat_num] = None
                        self.passenger_list.remove(item)
                        self.update_seats()
                        break


    def change_speed(self, delta):
        # TODO: изменить скорость на delta
        new_speed = self.speed + delta
        self.speed = max(0, min(self.max_speed, new_speed))
        return self.speed

    def update_seats(self):
        self.has_free_seats = len(self.passenger_list) < self.max_seats

    def __contains__(self, surname):
        # TODO: проверить фамилию пассажира
        return surname in self.passenger_list

    def __iadd__(self, surname):
        # TODO: += посадка
        self.board(surname)
        return self

    def __isub__(self, surname):
        # TODO: -= высадка
        self.unboard(surname)
        return self


# === Тесты для задачи 3 ===
print("\n=== Задача 3: Автобус ===")
bus = Bus(max_seats=3, max_speed=100)
bus.board("Иванов", "Петров")
print("Иванов" in bus)     # True
bus += "Сидоров"
print("Сидоров" in bus)    # True
bus -= "Петров"
print("Петров" in bus)     # False
bus.change_speed(20)
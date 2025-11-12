# ================================
# TeachMeSkills.by — Домашнее задание
# ================================
"""
Здесь задания на генераторы и паттерны проектирования:
- Строитель
- Фабричный метод
- Стратегия

Заполняйте TODO, читайте комментарии и запускайте тесты.
"""

# ================================
# ЗАДАНИЕ 1: Генератор чисел Фибоначчи
# ================================

def fibonacci_generator(n: int):
    """Генераторная функция, возвращает n чисел Фибоначчи."""
    # TODO: напишите генератор
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Тест:
print("\n--- Задание 1 ---")
n = int(input("Сколько чисел Фибоначчи вывести? "))
for num in fibonacci_generator(n):
    print(num, end=' ')
print()


# ================================
# ЗАДАНИЕ 2: Бесконечная циклическая последовательность
# ================================

def cycle_123():
    """Генераторная функция, бесконечно выдаёт 1-2-3"""
    # TODO: напишите генератор

    for _ in range(count):
        yield '1-2-3'

# Тест:
print("\n--- Задание 2 ---")
count = int(input("Сколько чисел вывести из бесконечного цикла? "))
gen = cycle_123()
for _ in range(count):
    print(next(gen), end=' ')
print()


# ================================
# ЗАДАНИЕ 3: Паттерн «Строитель»
# ================================

class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        return f"Pizza(size={self.size}, cheese={self.cheese}, pepperoni={self.pepperoni}, mushrooms={self.mushrooms}, onions={self.onions}, bacon={self.bacon})"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        # TODO: реализуйте метод
        self.pizza.size = size
        return self

    def add_cheese(self):
        # TODO: реализуйте метод
        self.pizza.cheese = False
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = False
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = False
        return self

    def add_onions(self):
        self.pizza.onions = False
        return self

    def add_bacon(self):
        self.pizza.bacon = False
        return self

    # TODO: реализуйте остальные add_… методы и метод build()
    def build(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_pizza(self):
        # TODO: используйте методы builder, чтобы собрать пиццу
        return self.builder.build()


# Тест:
print("\n--- Задание 3 ---")
builder = PizzaBuilder()
director = PizzaDirector(builder)
pizza = director.make_pizza()
print(pizza)


# ================================
# ЗАДАНИЕ 4: Паттерн «Фабричный метод»
# ================================

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        # TODO: реализуйте метод
        print('Гав!')


class Cat(Animal):
    def speak(self):
        # TODO: реализуйте метод
        print('Мяв!')


class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        # TODO: возвращайте Dog или Cat в зависимости от animal_type
        animal_type = animal_type.lower()
        if animal_type == 'dog':
            return Dog()
        else:
            return Cat()


# Тест:
print("\n--- Задание 4 ---")
factory = AnimalFactory()
animal = factory.create_animal("dog")
animal.speak()
animal = factory.create_animal("cat")
animal.speak()


# ================================
# ЗАДАНИЕ 5: Паттерн «Стратегия»
# ================================

class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        self.a = a
        self.b = b
        pass


class Addition(OperationStrategy):
    def execute(self, a, b):
        # TODO: реализуйте метод
        return a + b


class Subtraction(OperationStrategy):
    def execute(self, a, b):
        # TODO: реализуйте метод
        return a - b


class Multiplication(OperationStrategy):
    def execute(self, a, b):
        # TODO: реализуйте метод
        return a * b


class Division(OperationStrategy):
    def execute(self, a, b):
        # TODO: реализуйте метод
        if b == 0:
            raise ValueError('Деление на зиро!')
        return a / b

class Calculator:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: OperationStrategy):
        self.strategy = strategy

    def calculate(self, a, b):
        # TODO: выполните операцию через текущую стратегию
        return self.strategy.execute(a, b)


# Тест:
print("\n--- Задание 5 ---")
calc = Calculator()
calc.set_strategy(Addition())
print("5 + 3 =", calc.calculate(5, 3))
calc.set_strategy(Subtraction())
print("5 - 3 =", calc.calculate(5, 3))
calc.set_strategy(Multiplication())
print("5 * 3 =", calc.calculate(5, 3))
calc.set_strategy(Division())
print("5 / 3 =", calc.calculate(5, 3))


# ================================
# УДАЧИ! 🚀
# ================================
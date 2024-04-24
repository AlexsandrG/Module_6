# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000
# и функцию def horse_powers, которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car - класс Nissan и переопределите свойство price,
# а также переопределите функцию horse_powers
# Дополнительно создайте класс Kia, который также будет наследником класса Car
# и переопределите также свойство price, а также переопределите функцию horse_powers

class Car:
    price = 1000000

    def horse_powers(self):
        return 100


class Nissan(Car):
    price = 1500000

    @property
    def horse_powers(self):
        return 200


class Kia(Car):
    price = 800000

    def horse_powers(self):
        return 300


car = Car()
print(f'Цена авто: {car.price}')
print(f'Лошадиных сил: {car.horse_powers()}')
nissan = Nissan()
print(f'Цена авто: {nissan.price}')
print(f'Лошадиных сил: {nissan.horse_powers}')
kia = Kia()
print(f'Цена авто: {kia.price}')
print(f'Лошадиных сил: {kia.horse_powers()}')

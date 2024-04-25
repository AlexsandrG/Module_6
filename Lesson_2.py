# Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
# которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
# а также переопределите функцию horse_powers
# Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price


class Vehicle():
    def __init__(self):
        self.vehicle_type = "none"


class Car():
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return 200


class Nissan(Vehicle, Car):
    def __init__(self):
        super().__init__()
        self.price = 1500000
        self.vehicle_type = 'Benzin'

    def horse_powers(self):
        return 300

    def horse_powers(self):
        return 400


nissan_1 = Nissan()
print(nissan_1.vehicle_type, nissan_1.price)

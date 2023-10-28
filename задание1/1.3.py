class Car:
    color = None
    fuel = None
    type = None
    power = None
    def data(self):
        print(f'цвет автомобиля: {myCar.color}')
        print(f'количество топлива: {myCar.fuel}')
        print(f'тип автомобиля: {myCar.type}')
        print(f'тяговая мощность автомобиля: {myCar.power}')
        print('...................')
        print(f'цвет автомобиля: {myCar_1.color}')
        print(f'количество топлива: {myCar_1.fuel}')
        print(f'тип автомобиля: {myCar_1.type}')
        print(f'тяговая мощность автомобиля: {myCar_1.power}')


myCar = Car()
myCar.color = 'red'  # красим в красный цвет
myCar.fuel = 50    # заливаем топливо
myCar.type = 'passenger'
myCar.power = 70

myCar_1 = Car()
myCar_1.color = 'blue'
myCar_1.fuel = 130
myCar_1.type = 'truck'
myCar_1.power = 120

myCar.data()
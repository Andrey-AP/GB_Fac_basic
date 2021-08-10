class Car:
    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = False

    def go(self):
        print(f'{self.name} go')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, direction):
        print(f'{self.name} terned {direction}')

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'you fucking idiot? your speed is {self.speed}')
        else:
            print(f'EEEEEE your speed is {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'you fucking idiot? your speed is {self.speed}')
        else:
            print(f'EEEEEE your speed is {self.speed}')


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        self.is_police = True


pol = PoliceCar('ment', 90, 'black')
print(pol.is_police)
pol.turn('left')

wor=WorkCar('bus', 900, 'red')
print(wor.is_police)
wor.show_speed()
wor.speed=15
wor.show_speed()


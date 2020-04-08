class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police
    def go(self):
        self.speed = 60
        print("Car is going")
    def stop(slef):
        self.speed = 0
        print("Car stoped")
    def turn(slef, direction):
        self.speed = 20
        print(f"Car is turned to {direction}")
        self.speed = 60

class SportCar(Car):
    def fast_mode(self, choice):
        self.speed = 120 if choice == "ON" else 60
        print(f"Fast mode: {choice}")

class TownCar(Car):
    def light_mode(self, choice):
        self.speed = 30 if choice == "ON" else 60
        print(f"Light mode: {choice}")

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police
        self.clearing = False
    def clearing_mode(self, choice):
        self.clearing = True if choice == "ON" else False
        print(f"Clearing mode: {choice}")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        self.speed, self.color, self.name, self.is_police, self.work_mode = speed, color, name, is_police, False
    def work_mode(self, choice):
        self.work_mode = True if choice == "ON" else False
        print(f"Work mode: {choice}")
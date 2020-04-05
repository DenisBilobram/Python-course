class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._widht = width
    def calculate(self):
        mass = self._lenght * self._widht * 25 * 5 / 1000
        print(f"Mass = {mass} t")
road = Road(20, 5000)
road.calculate()
import time
class TrafficLight:
    __colors = ["Red", "Yellow", "Green"]
    def running(self):
        while True:
            for color in self.__colors:
                print(f"Now is {color}")
                if color is "Yellow":
                    time.sleep(2)
                else:
                    time.sleep(7)

svet = TrafficLight()
svet.running()
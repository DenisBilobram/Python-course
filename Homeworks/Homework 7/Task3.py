class Cell():
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        new = Cell(self.count + other.count)
        return new

    def __sub__(self, other):
        if self.count >= other.count:
            new = Cell(self.count - other.count)
            return new
        return "Uncorrect data"

    def __mul__(self, other):
        new = Cell(self.count * other.count)
        return new

    def __truediv__(self, other):
        new = Cell(self.count * other.count)
        return new

    def make_order(self, num):
        times = self.count // num
        balance = self.count % num
        for i in range(times):
            for el in range(num):
                print("*", end="")
            print("")
        for i in range(balance):
            print("*", end="")
        print("")

f = Cell(10)
f.make_order(3)
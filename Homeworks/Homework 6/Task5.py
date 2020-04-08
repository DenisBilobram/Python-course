class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Start of drawing")

class Pen(Stationery):
    def draw(self):
        print("Start of drawing with help of Pen")

class Pencil(Stationery):
    def draw(self):
        print("Start of drawing with help of Pencil")

class Handle(Stationery):
    def draw(self):
        print("Start of drawing with help of Handle")

stationery = Stationery("dfsdf")
stationery.draw()
pen = Pen("dfsdf")
pen.draw()
pencil = Pencil("dfsdf")
pencil.draw()
handle = Handle("dfsdf")
handle.draw()
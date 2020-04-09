from abc import abstractmethod, ABC
class Clothes():
    sum = 0
    @property
    def info_sum(self):
        return f"Sum: {self.sum}"

class Coat(Clothes):
    def __init__(self, size):
        self.value = size/6.5 + 0.5
        Clothes.sum += self.value

class Suit(Clothes):
    def __init__(self, hight):
        self.value = hight * 2 + 0.3
        Clothes.sum += self.value

clothe = Clothes()
suit = Suit(100)
coat = Coat(200)
print(clothe.info_sum)
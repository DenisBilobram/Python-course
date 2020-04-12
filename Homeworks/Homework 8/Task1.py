class Data():
    dict_of_days = {"Первый": 1, "Второй": 2, "Третий": 3, "Четвёртый": 4, "Пятый": 5, "Шестой": 6}  # и т.д
    dict_of_months = {"Январь": 1, "Февраль": 2, "Март": 3, "Апрель": 4, "Май": 5, "Июнь": 6,"Июль": 7,"Август": 8, "Сентябрь": 9, "Март": 10, "Октябрь": 11, "Ноябрь": 12, "Декабрь": 12}
    dict_of_years = {"Двухтысячный": 2000, "Две тысячи четвёртый": 2004, "Две тысячи восьмой": 2008, "Две тысячи двенадцатый": 2012, "Две тысячи шестнадцатый": 2016, "Две тысячи твадцатый": 2020}
    def __init__(self, data):
        self.data = data
    @classmethod
    def number_back(cls, data):
        data = data.split("-")
        print(f"{cls.dict_of_days[data[0]]}-{cls.dict_of_months[data[1]]}-{cls.dict_of_years[data[2]]}")

    def number(self):
        return self.number_back(self.data)

    @staticmethod
    def is_correct_back(data):
        correct = True
        data = data.split("-")
        if Data.dict_of_days[data[0]] < 0 or Data.dict_of_days[data[0]] > 31:
            correct = False
        if Data.dict_of_months[data[1]] < 0 or Data.dict_of_months[data[1]] > 12:
            correct = False
        if Data.dict_of_years[data[2]] < 0 or Data.dict_of_years[data[2]] > 2021:
           correct = False
        print(correct)
    def is_correct(self):
        return self.is_correct_back(self.data)
d = Data("Первый-Январь-Двухтысячный")
d.number()
d.is_correct()
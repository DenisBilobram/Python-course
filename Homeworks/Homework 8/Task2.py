class my_class(Exception):
    def __init__(self, text):
        self.text = text

try:
    a = int(input("Enter a number"))
    b = int(input("Enter a number"))
    if b == 0:
        raise my_class("Division by zero")
except my_class as err:
    print(err)
else:
    print(a//b)

input("hello")
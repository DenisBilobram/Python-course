from functools import reduce

def product(first, second):
    return first * second

my_list = [el for el in range(100, 1001, 2)]
print(reduce(product, my_list))
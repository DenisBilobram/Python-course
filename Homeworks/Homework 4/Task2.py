my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [el for el in my_list if el > my_list[my_list.index(el) - 1]]
result.pop(0)
print(result)
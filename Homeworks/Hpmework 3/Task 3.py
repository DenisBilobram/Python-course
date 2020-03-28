def my_func(a=int(input("Enter a first parameter: ")), b=int(input("Enter a second parameter: ")), c=int(input("Enter a third parameter: "))):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    return sum(my_list)

print(my_func())
def my_func(x=int(input("Enter a positive number: ")), y=int(input("Enter a negtive degree: "))):
    if y == -1:
        result = 1 / x
        print(result)
    elif y < -1:
        i = 2
        degree = x
        while i <= abs(y):
            degree = degree * x
            i += 1
        result = 1 / degree
        print(result)

my_func()
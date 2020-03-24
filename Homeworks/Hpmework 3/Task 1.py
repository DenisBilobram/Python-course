def devide(a=float(input("Enter first number: ")), b=float(input("Enter second number: "))):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division on zero!!")
    else:
        print(round(result, 2))

devide()
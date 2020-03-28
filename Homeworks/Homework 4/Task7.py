def fact(number):
    i = 1
    factorial = 1
    while i <= number:
        factorial *= i
        i += 1
        yield factorial
for i in fact(4):
    print(i)
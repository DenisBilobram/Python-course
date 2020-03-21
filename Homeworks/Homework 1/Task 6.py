a = int(input("Enter parameter a: "))
b = int(input("Enter parameter b: "))
i = 1
while a <= b:
    a = a + (a * (10/100))
    i = i + 1
print(i)
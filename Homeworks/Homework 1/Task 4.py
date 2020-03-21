number = input("Enter a number: ")
i = 0
max = 0
while i < len(number):
    if int(number[i]) >= max:
        max = int(number[i])
    i += 1
print(max)
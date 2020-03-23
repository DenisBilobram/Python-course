user_string = input("Enter a string: ")
list_of_strings = user_string.split()
i = 0
st = ""
for index, value in enumerate(list_of_strings):
    if len(value) < 10:
        print(index, value)
    else:
        while i < 10:
            st += value[i]
            i += 1
        print(index, st)
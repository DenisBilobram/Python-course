def int_func(word=input("Enter a word: ")):
    my_list = word.split()
    second_list = []
    for words in my_list:
        for letter in words:
            second_list.append(letter)
        second_list.append("-")
    second_list[0] = second_list[0].upper()
    for i in second_list:
        if i == "-":
            try:
                second_list[second_list.index(i) + 1] = second_list[second_list.index(i) + 1].upper()
                second_list[second_list.index(i)] = " "
            except:
                pass
    second_list.pop()
    result = "".join(second_list)
    print(result)
int_func()
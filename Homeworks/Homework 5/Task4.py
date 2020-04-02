my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять", "Six": "Шесть", "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять"}
f_obj = open("text_4.txt", "r+", encoding="utf-8")
result_f = open("text_4_result.txt", "w", encoding="utf-8")
for line in f_obj:
    my_str = line.split(" - ")
    my_str[0] = my_dict.get(my_str[0])
    result = " - ".join(my_str)
    result_f.write(result)
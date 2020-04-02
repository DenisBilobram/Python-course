# для работы алгоритма нужен как минимум один запуск Task1.py
f_read = open("text_1.txt")
f_write = open("text_2.txt", "w")
text = f_read.read()
f_write.write(text)
f_read.close()
f_write.close()
f_obj = open("text_2.txt", "r+")
lines = f_obj.readlines()
f_obj = open("text_2.txt", "a+")
for index, line in enumerate(lines, start=1):
    f_obj.write(f"{index} string, size: {len(line)} symbols.\n")
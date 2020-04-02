obj_f = open("text_5.txt", "w+", encoding="utf-8")
obj_f.write("1 2 3 4 5 6 7 8 9 10")
obj_f = open("text_5.txt", "r", encoding="utf-8")
my_list = (obj_f.readline()).split()
sum = 0
for num in my_list:
    sum += int(num)
print(sum)
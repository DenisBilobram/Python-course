read_obj = open("text_3.txt", encoding="utf-8")
workers = read_obj.readlines()
selery = 0
count = 0
for worker in workers:
    my_list = worker.split()
    if float(my_list[1]) < 20000:
        print(my_list[0])
    selery += float(my_list[1])
    count += 1
print(f"middle: {selery // count}")
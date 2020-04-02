import json
read_f = open("text_7.txt", "r", encoding="utf-8")
write_f = open("text_77.json", "w", encoding="utf-8")
result_dict = {}
average = {}
result_list = [result_dict, average]
sum = 0
count = 0
for line in read_f:
    midl = line.split()
    itog = int(midl[2]) - int(midl[3])
    result_dict[midl[0]] = itog
    if itog > 0:
        sum += itog
        count += 1
average["avarage"] = sum // count
json.dump(result_list, write_f)
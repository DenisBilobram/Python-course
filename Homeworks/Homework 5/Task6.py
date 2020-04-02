read_obj = open("text_6.txt", encoding="utf-8")
result_dict = {}
for line in read_obj:
    sub = line.split()[0][0:line.split()[0].index(":")]
    half = line.split()[1:4]
    sum = 0
    for i in half:
        el = 0
        real_el = ""
        for char in i:
            if char.isdigit():
                real_el += char
        if real_el != "":
            sum += int(real_el)
            continue
        sum += int(el)
    result_dict.update({f"{sub}": sum})
print(result_dict)
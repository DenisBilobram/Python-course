f_obj = open("text_1.txt", "a")
text = ""
while True:
    data = input()
    if data == "":
        break
    f_obj.write(f"{data}\n")
f_obj.close()
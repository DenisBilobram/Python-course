# без метода sort и reverse реализовать было тяжко, от сюда такой плохой код
my_list = [7, 5, 3, 3, 2]
while True:
    st = ""
    i = 0
    data = input("Enter a number: ")
    while i < len(my_list):
        st += str(my_list[i])
        i += 1
    place = st.find(data)
    count = my_list.count(int(data))
    if place != -1:
        my_list.insert(place + count, int(data))
        print(my_list)
    else:
        p = 0
        while p < len(my_list):
            if int(data) > my_list[p]:
                place1 = my_list.index(my_list[p])
                my_list.insert(place1, int(data))
                print(my_list)
                break
            p += 1
            if p == len(my_list):
                my_list.append(int(data))
                print(my_list)
                break
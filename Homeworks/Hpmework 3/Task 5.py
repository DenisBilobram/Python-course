str = ""
interval = []
while True:
    str = (input("Enter a numbers (to exit enter a letter): "))
    my_list = str.split()
    try:
        for i in my_list:
            interval.append(int(i))
    except ValueError:
        print(f"The amount: {sum(interval)}")
        break
    print(f"The amount: {sum(interval)}")

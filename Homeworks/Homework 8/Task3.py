class test_array(Exception):
    def __init__(self, number):
        self.number = number

array = []
while True:
    try:
        tmp = input("Enter a number to array: ")
        if tmp == "stop":
            break
        for i in tmp:
            if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                raise test_array("Incorrect data")
    except test_array as err:
        print(err)
    else:
        array.append(int(tmp))
        print(array)
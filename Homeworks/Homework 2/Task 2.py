my_list = (input("Enter a list (without signs like these: [] "" , ): ")).split()
my_list_copy = my_list[:]
my_list_copy2 = my_list[:]
count_of_couple = len(my_list) // 2
balance = len(my_list) % 2
i = 0
couple = 1
while couple <= count_of_couple:
    if balance == 0:
        my_list[i] = my_list_copy[i + 1]
        my_list[i + 1] = my_list_copy2[i]
        couple += 1
        i += 2
    elif balance == 1 and i != len(my_list) - 1:
             my_list[i] = my_list_copy[i + 1]
             my_list[i + 1] = my_list_copy2[i]
             couple += 1
             i += 2
print(my_list)
list_of_seasons = ["winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter"]
dict_of_seasons = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer", 8: "summer", 9: "autumn",
                   10: "autumn", 11: "autumn", 12: "winter"}
# простая реализация
ask = int(input("Enter a number of month: "))
if ask == 12 or ask == 1 or ask == 2:
    print("It's winter")
if ask == 3 or ask == 4 or ask == 5:
    print("It's spring")
if ask == 6 or ask == 7 or ask == 8:
    print("It's summer")
if ask == 9 or ask == 10 or ask == 11:
    print("It's autumn")

# реализация через list
print(f"It's {list_of_seasons[ask - 1]}")

# реализация через dict
print(f"It's {dict_of_seasons.get(ask)}")
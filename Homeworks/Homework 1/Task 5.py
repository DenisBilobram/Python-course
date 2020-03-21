profit = int(input("Enter your profit: "))
expenses = int(input("Enter your expenses: "))
if profit > expenses:
    print("Congratulations, your company profitable")
    count = int(input("How many employees do you have?: "))
    profit_per_one = (profit - expenses) // count
    print(f"Your employees will get {profit_per_one}$ per person")
else:
    print("It's sad((")
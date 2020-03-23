list_of_turples = []
analytics = {"name": [], "value": [], "count": [], "unit": []}
i = 0
d = 0
while True:
    answer = input("Do you want to add element?(yes\\no): ")
    if answer == "yes":
        answer1 = input("What is the name of this element?: ")
        list_of_turples.append((i, {"name": answer1}))
        answer2 = input("How much does it cost?: ")
        list_of_turples[i][1]["value"] = int(answer2)
        answer3 = input("What count of this?: ")
        list_of_turples[i][1]["count"] = int(answer3)
        answer4 = input("What is unit of this?: ")
        list_of_turples[i][1]["unit"] = answer4
        i += 1
        print(list_of_turples)
        question = input("Do you want to see analutics?(yes\\no): ")
        if question == "yes":
            p = 0
            p = d
            while p < len(list_of_turples):
                analytics["name"].append(list_of_turples[p][1]["name"])
                analytics["value"].append(list_of_turples[p][1]["value"])
                analytics["count"].append(list_of_turples[p][1]["count"])
                analytics["unit"].append(list_of_turples[p][1]["unit"])
                p += 1
            print(analytics)
            d += 1
        else:
            continue
    elif answer == "no":
        break
from sys import argv

def salary(hour_, value_, premia_):
    try:
        result = (int(hours) * int(value)) + int(premia)
    except ValueError:
        print("Incorrect type!")
    else:
        print(result)

try:
    script_name, hours, value, premia = argv
except ValueError:
        print("Need more parameters!")

try:
    salary(hours, value, premia)
except TypeError:
    pass
except NameError:
    pass
class stock():
    areas = {"common": {"free": 500, "busy": 0},
             "programmers": {"free": 250, "busy": 0},
             "accountants": {"free": 250, "busy": 0}}
    
class orgtechnician():
    list_of_bases = ["common_base_of_data", "programmers_base", "accountants base"]
    common_count = 0
    kinds_of_orgtechnician = ["printer", "scanner", "xerox"]
    common_base_of_data = {"printers": {"count": 0, "colors": [], "total price": 0, "paints": []},
                    "scanners": {"count": 0, "colors": [], "total price": 0, "speeds": []},
                    "xeroxes": {"count": 0, "colors": [], "total price": 0, "times to copy": []}}

    programmers_base = {"printers": {"count": 0, "colors": [], "total price": 0, "paints": []},
                    "scanners": {"count": 0, "colors": [], "total price": 0, "speeds": []},
                    "xeroxes": {"count": 0, "colors": [], "total price": 0, "times to copy": []}}

    accountants_base = {"printers": {"count": 0, "colors": [], "total price": 0, "paints": []},
                    "scanners": {"count": 0, "colors": [], "total price": 0, "speeds": []},
                    "xeroxes": {"count": 0, "colors": [], "total price": 0, "times to copy": []}}

class printer(orgtechnician):
    area_per_one = 25
    def __init__(self, value, color, paint):
        self.color, self.value, self.paint = color, value, paint
        orgtechnician.common_base_of_data["printers"]["count"] += 1
        orgtechnician.common_base_of_data["printers"]["colors"].append(color)
        orgtechnician.common_base_of_data["printers"]["total price"] += value
        orgtechnician.common_base_of_data["printers"]["paints"].append(paint)
        orgtechnician.common_count += 1
        stock.areas["common"]["free"] -= printer.area_per_one
        stock.areas["common"]["busy"] += printer.area_per_one

    def change_locate(self, where):
        orgtechnician.common_base_of_data["printers"]["count"] -= 1
        orgtechnician.common_base_of_data["printers"]["colors"].remove(self.color)
        orgtechnician.common_base_of_data["printers"]["total price"] -= self.value
        orgtechnician.common_base_of_data["printers"]["paints"].remove(self.paint)
        if where == "programmers base":
            orgtechnician.programmers_base["printers"]["count"] += 1
            orgtechnician.programmers_base["printers"]["colors"].append(self.color)
            orgtechnician.programmers_base["printers"]["total price"] += self.value
            orgtechnician.programmers_base["printers"]["paints"].append(self.paint)
        elif where == "accountats_base":
            orgtechnician.accountats_base["printers"]["count"] += 1
            orgtechnician.accountats_base["printers"]["colors"].append(self.color)
            orgtechnician.accountats_base["printers"]["total price"] += self.value
            orgtechnician.accountats_base["printers"]["paints"].append(self.paint)

class scanner(orgtechnician):
    area_per_one = 30
    def __init__(self, value, color, speed_of_scanning):
        self.color, self.value, self.speed_of_scanning = color, value, speed_of_scanning
        orgtechnician.common_base_of_data["scanners"]["count"] += 1
        orgtechnician.common_base_of_data["scanners"]["colors"].append(color)
        orgtechnician.common_base_of_data["scanners"]["total price"] += value
        orgtechnician.common_base_of_data["scanners"]["speeds"].append(speed_of_scanning)
        orgtechnician.common_count += 1
        stock.areas["common"]["free"] -= scanner.area_per_one
        stock.areas["common"]["busy"] += scanner.area_per_one
    def change_locate(self, where):
        orgtechnician.common_base_of_data["scanners"]["count"] -= 1
        orgtechnician.common_base_of_data["scanners"]["colors"].remove(self.color)
        orgtechnician.common_base_of_data["scanners"]["total price"] -= self.value
        orgtechnician.common_base_of_data["scanners"]["speeds"].remove(self.speeds)
        if where == "programmers base":
            orgtechnician.programmers_base["scanners"]["count"] += 1
            orgtechnician.programmers_base["scanners"]["colors"].append(self.color)
            orgtechnician.programmers_base["scanners"]["total price"] += self.value
            orgtechnician.programmers_base["scanners"]["speeds"].append(self.speeds)
        elif where == "accountats_base":
            orgtechnician.accountats_base["scanners"]["count"] += 1
            orgtechnician.accountats_base["scanners"]["colors"].append(self.color)
            orgtechnician.accountats_base["scanners"]["total price"] += self.value
            orgtechnician.accountats_base["scanners"]["speeds"].append(self.speeds)

class xerox(orgtechnician):
    area_per_one = 35
    def __init__(self, value, color, time_to_copy):
        self.color, self.value, self.time_to_copy = color, value, time_to_copy
        orgtechnician.common_count += 1
        orgtechnician.common_base_of_data["xeroxes"]["count"] += 1
        orgtechnician.common_base_of_data["xeroxes"]["colors"].append(color)
        orgtechnician.common_base_of_data["xeroxes"]["total price"] += value
        orgtechnician.common_base_of_data["xeroxes"]["times to copy"].append(time_to_copy)
        stock.areas["common"]["free"] -= xerox.area_per_one
        stock.areas["common"]["busy"] += xerox.area_per_one

    def change_locate(self, where):
        orgtechnician.common_base_of_data["xerox"]["count"] -= 1
        orgtechnician.common_base_of_data["xerox"]["colors"].remove(self.color)
        orgtechnician.common_base_of_data["xerox"]["total price"] -= self.value
        orgtechnician.common_base_of_data["xerox"]["times to copy"].remove(self.time_to_copy)
        if where == "programmers base":
            orgtechnician.programmers_base["xerox"]["count"] += 1
            orgtechnician.programmers_base["xerox"]["colors"].append(self.color)
            orgtechnician.programmers_base["xerox"]["total price"] += self.value
            orgtechnician.programmers_base["xerox"]["times to copy"].append(self.time_to_copy)
        elif where == "accountats_base":
            orgtechnician.accountats_base["xerox"]["count"] += 1
            orgtechnician.accountats_base["xerox"]["colors"].append(self.color)
            orgtechnician.accountats_base["xerox"]["total price"] += self.value
            orgtechnician.accountats_base["xerox"]["times to copy"].append(self.time_to_copy)

m = xerox(100, "red", 100)
d = printer(100, "blue", "all")
a = scanner(200, "gold", 500)
d.change_locate("programmers base")
print(orgtechnician.common_base_of_data)
print(orgtechnician.programmers_base)
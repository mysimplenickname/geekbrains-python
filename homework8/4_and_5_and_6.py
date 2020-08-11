class OfficeAutomation:
    name: str
    model: str

    def __init__(self, name, model):
        self.name = name
        self.model = model


class MyValueError(Exception):
    def __str__(self):
        return f"You should enter a number."


class StorageOverflowException(Exception):
    def __str__(self):
        return f"Not enough space!"


class Storage:
    real_capacity: int
    storage_capacity: int
    items: dict

    def __init__(self, capacity):
        self.real_capacity = 0
        self.storage_capacity = capacity
        self.items = dict()

    def check_user_input(self, item_amount):
        if type(item_amount) != int:
            raise MyValueError
        else:
            return int(item_amount)

    def check_storage_overflow(self, item_amount):
        if self.real_capacity + item_amount > self.storage_capacity:
            raise StorageOverflowException
        else:
            return item_amount

    def put(self, item_type: OfficeAutomation, item_amount: int):
        try:
            self.real_capacity += self.check_storage_overflow(self.check_user_input(item_amount))
            print(f"You added {item_amount} item(s). {self.storage_capacity - self.real_capacity} free space(s) left.")

            if item_type in self.items:
                self.items[item_type] += item_amount
            else:
                self.items[item_type] = item_amount

        except MyValueError as value_exception:
            print(value_exception)

        except StorageOverflowException as overflow_exception:
            print(overflow_exception)

    def __str__(self):
        return str('\n'.join([f"{i.__class__.__name__} {i.name} {i.model}, amount: {j}." for i, j in self.items.items()]) + '\n')


class Printer(OfficeAutomation):
    print_type: str

    def __init__(self, name, model, print_type):
        super().__init__(name, model)
        self.print_type = print_type


class Scanner(OfficeAutomation):
    scan_type: str

    def __init__(self, name, model, scan_type):
        super().__init__(name, model)
        self.scan_type = scan_type


hp_printer = Printer("HP", "2676", "Laser")

anycubic_printer = Printer("Anycubic", "Photon S", "LCD")

cannon_scanner = Scanner("Canon", "LBP2900B", "Production")

storage = Storage(5)

storage.put(hp_printer, 1)
print(storage)

storage.put(cannon_scanner, 2)
print(storage)

storage.put(anycubic_printer, "f")
print()

storage.put(cannon_scanner, 3)
print()

storage.put(hp_printer, 2)
print(storage)

class Warehouse:
    pass


class OfficeEquipment:
    def __init__(self, name, model, s_number, type_eq='OfficeEquipment'):
        self.name = name
        self.model = model
        self.type_eq = type_eq
        self.sn = s_number


class Printer(OfficeEquipment):
    print_ls = []

    def __init__(self, name, model, print_speed, color, s_number):
        super().__init__(name, model, s_number, type_eq='Printer')
        self.print_speed = print_speed
        self.color = color
        Printer.print_ls.append(self)

    @classmethod
    def get_print_ls(cls):
        return cls.print_ls

    def __str__(self):
        return f'Manufacturing: {self.name}\n' \
               f'Model: {self.model}\n' \
               f'Print Speed: {self.print_speed}\n' \
               f'Color: {self.color}\n'


class Scan(OfficeEquipment):
    def __init__(self, name, model, scan_speed, s_number, doub_side=True):
        super().__init__(name, model, s_number, type_eq='Scanner')
        self.scan_speed = scan_speed
        self.doub_side = doub_side


class Copier(OfficeEquipment):
    def __init__(self, name, model, copier_speed, s_number):
        super().__init__(name, model, s_number, type_eq='Copier')
        self.copier_speed = copier_speed


p1 = Printer('HP', 'P100', 100, True, 'Nv534FF')
p2 = Printer('We', 'P100', 100, False, 'Nv534FF')
s1 = Scan('Brother', 'GH34', 10, 'Fhdd11')
for printer in Printer.get_print_ls():
    print(printer)

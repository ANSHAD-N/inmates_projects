class Computer:
    def __init__(self, ram, memory, processor):
        self.ram = ram
        self.memory = memory
        self.processor = processor

    def get_specs(self):
        print('Please enter the details.')
        self.ram = input('Enter Ram Size : ')
        self.memory = input('Memory size : ')
        self.processor = input('Enter processor : ')

    def display_specs(self):
        print('Here are the specs of the computer.')
        print('\n Ram size is: ' + self.ram, '\n Memory size is: ' + self.memory, ' \nprocessor is: ' + self.processor)


class Desktop(Computer):
    def __init__(self, case_color):
        self.case_color = case_color

    def get_case_details(self):
        self.case_color = input('Enter case color : ')

    def display_case_details(self):
        print('case color is: ' + self.case_color)


class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def get_weight(self):
        self.weight = input('Enter weight : ')

    def display_weight(self):
        print('weight is: ' + self.weight)


comp = Desktop('')

comp.get_specs()

comp.get_case_details()

comp.display_specs()

comp.display_case_details()

lap = Laptop('')

lap.get_specs()

lap.get_weight()

lap.display_specs()

lap.display_weight()
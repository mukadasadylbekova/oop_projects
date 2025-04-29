class Student:
    def __init__(self, name=None, age = None, grade = None, tuition_fee=None):
        self.name = name
        self.age = age
        self.grade = grade
        self.tuition_fee = tuition_fee

    def display_info(self):
        print(f"Student {self.name}, Age: {self.age}, Tuition fee: {self.tuition_fee}")

    def swap_the_fees(self, fee1, fee2):
        self.tuition_fee = fee1
        fee1, fee2 = fee2, fee1
        return [fee1, fee2]
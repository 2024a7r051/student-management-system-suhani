class Student:
    school = "Programming Pathshala"

    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "Fail"

    def display(self):
        print("------------------------------")
        print("Roll No :", self.roll)
        print("Name    :", self.name)
        print("Marks   :", self.marks)
        print("Grade   :", self.grade())
        print("------------------------------")

    @classmethod
    def show_school(cls):
        print(cls.school)

    @staticmethod
    def valid_marks(marks):
        return 0 <= marks <= 100
from student import Student

students = []


def add_student():
    roll = int(input("Enter Roll Number: "))

    for s in students:
        if s.roll == roll:
            print("Roll Number already exists")
            return

    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    if not Student.valid_marks(marks):
        print("Marks should be between 0 and 100")
        return

    student = Student(roll, name, marks)
    students.append(student)
    print("Student Added Successfully")


def view_students():
    if not students:
        print("No Students Found")
        return

    for s in students:
        s.display()


def search_student():
    roll = int(input("Enter Roll Number: "))

    for s in students:
        if s.roll == roll:
            s.display()
            return

    print("Student Not Found")


def update_marks():
    roll = int(input("Enter Roll Number: "))

    for s in students:
        if s.roll == roll:
            marks = int(input("Enter New Marks: "))

            if Student.valid_marks(marks):
                s.marks = marks
                print("Marks Updated Successfully")
            else:
                print("Invalid Marks")
            return

    print("Student Not Found")


def delete_student():
    roll = int(input("Enter Roll Number: "))

    for s in students:
        if s.roll == roll:
            students.remove(s)
            print("Student Deleted Successfully")
            return

    print("Student Not Found")


def show_topper():
    if not students:
        print("No Students Found")
        return

    topper = students[0]

    for s in students:
        if s.marks > topper.marks:
            topper = s

    print("\nTopper Details")
    topper.display()


if __name__ == "__main__":

    while True:
        print("\n==============================")
        print(" Student Management System")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Show Topper")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_marks()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            show_topper()

        elif choice == "7":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")
from student_class import Student

if __name__=="__main__":
    students = []

    student1 = Student("Mukadas Adylbekova", 20, "A", 5000)
    student2 = Student("Nuriza", 22, "B", 4500)
    student3 = Student("Nurbek", 23, "C", 4800)

    students.extend([student1, student2, student3])

    for student in students:
        student.display_info()

    students[0].tuition_fee = students[0].swap_the_fees(students[0].tuition_fee, students[1].tuition_fee)[0]
    print("\nAfter swapping the tuition fees of the first two students:")
    students[0].display_info()
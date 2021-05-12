from task02.oop_2 import *


def testing_base_case():
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")
    assert advanced_python_teacher.last_name == "Smetanin"


def testing_of_working_homeworkresult():
    teacher = Teacher("Oleg", "Vladimirov")
    student = Student("Ivan", "Ivanov")
    homework_first = teacher.create_homework("Learn it", 1)
    homework_res = student.do_homework(homework_first, "My own solution")
    assert homework_res.solution == "My own solution"
    assert homework_res.author == student


def testing_for_case_of_bad_student():
    teacher = Teacher("Oleg", "Vladimirovich")
    bad_student = Student("Ivan", "Ivanov")
    homework_first = teacher.create_homework("Learn it", 1)
    homework_res_of_bad_student = bad_student.do_homework(homework_first, "no hw")
    assert not teacher.check_homework(homework_res_of_bad_student)

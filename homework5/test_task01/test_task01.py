from task01.oop_1 import *


def testing_of_example():
    """Testing of example"""
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    assert teacher.last_name == "Daniil"
    assert student.first_name == "Petrov"

    expired_homework = teacher.create_homework("Learn functions", 0)
    assert (
        type(expired_homework.created) == datetime
    )  # Example: 2019-05-26 16:44:30.688762
    assert type(expired_homework.deadline) == timedelta  # 0:00:00
    assert expired_homework.text == "Learn functions"

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    assert type(oop_homework.deadline) == timedelta  # 5 days, 0:00:00

    assert type(student.do_homework(oop_homework)) == Homework
    assert student.do_homework(expired_homework) is None  # You are late

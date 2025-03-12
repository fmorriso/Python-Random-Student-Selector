import random
import sys

import names

from student import Student

# from collections import Counter

students: list[Student] = []


def get_python_version() -> str:
    """ the version of python running this program"""
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def add_random_students(num: int, period: int) -> None:
    """
    Add the specified number of random students for the specified class period to the list
    :param num: The number of students desired
    :param period: The class period to associate with each generated student
    """
    for i in range(num):
        last_name = names.get_last_name()
        # try for an even number of males and females
        if i % 2 == 0:
            first_name = names.get_first_name(gender = 'male')
        else:
            first_name = names.get_first_name(gender = 'female')
        s = Student(first_name, last_name, period)
        # print(f'{s}')
        students.append(s)


def select_random_student_from_period(period: int) -> Student:
    # filter for students in the specified period
    subset = [student for student in students if student.period == period]
    # choose a random student from the subset of students
    student = random.choice(subset)
    # remove that student from the list
    students.remove(student)
    return student


def number_students_in_period(period: int) -> int:
    # filter for students in the specified period
    subset = [student for student in students if student.period == period]
    return len(subset)


def refill_students_list(periods: list[int], minimum = 5, maximum = 25) -> None:
    students.clear()
    for period in periods:
        num_students = random.randint(minimum, maximum)
        add_random_students(num_students, period)


def get_whole_number_in_range(prompt: str, minimum: int = 0, maximum: int = 10) -> int:
    """
    Get a whole number with a restricted range of values.
    :param prompt:  A string containing the prompt text to show the user.
    :param minimum: The minimum value that can be entered.
    :param maximum: The maximum value that can be entered.
    :return: a whole value
    """
    MSG: str = f'{prompt} (between {minimum} and {maximum}) '
    while True:
        try:
            n = int(input(MSG))
            if minimum <= n <= maximum:
                return n
            print(f'Please enter a number between {minimum} and {maximum}')
        except (TypeError, ValueError):
            print('Please enter a whole number')


def main():
    refill_students_list([6,7,8])

    period = get_whole_number_in_range('Which class period?', minimum = 6, maximum = 8)

    while number_students_in_period(period) > 0:
        student = select_random_student_from_period(period)
        print(student.to_json())
        json = student.to_json()
        student = Student.from_json(json)
        print(student)


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    main()

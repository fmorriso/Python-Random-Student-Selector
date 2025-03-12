import sys
import random
import names

from student import Student

students: list[Student] = []

def get_python_version() -> str:
    """ the version of python running this program"""
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def fill_list_with_random_students() -> None:
    first_name, last_name = '', ''
    for i in range(50):
        period = random.randint(6, 8)
        last_name = names.get_last_name()
        if i % 2 == 0:
            first_name = names.get_first_name(gender = 'male')
        else:
            first_name = names.get_first_name(gender = 'female')
        s = Student(first_name, last_name, period)
        # print(f'{s}')
        students.append(s)


def main():
    fill_list_with_random_students()


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    main()
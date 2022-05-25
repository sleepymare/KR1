from statistics import mean


class Student():
    def __init__(self, name, surname, fullname, list_of_grades=None):
        if list_of_grades is None:
            list_of_grades = [3, 4, 5]
        self.list_of_grades = list_of_grades
        self.name = name
        self.surname = surname
        self.fullname = fullname

    def greetings(self):
        print("Hello I am", self.fullname)

    def mean_grade(self):
        return mean(self.list_of_grades)

    def is_otl(self):
        if self.mean_grade() > 4.5:
            print("YES")
        else:
            print("NO")

    def print(self):
        print(self.fullname)

    def __add__(self, other):
        return f'{self.name} is friends with {other.name}'



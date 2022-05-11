"""
Abigail Roberts
Lab 13
"""


class Person():
    """main"""

    def __init__(self, name=0, age=0):
        """name and age variables"""
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def get_name(self, name):
        return self.__name

    def get_age(self, age):
        return self.__age

    def __repr__(self):
        return "Name = (" + str(self.__name) + "," + str(self.__age) + ")"

    def __str__(self):
        return "(" + str(self.__name) + "," + str(self.__age) + ")"

    def __eq__(self, other):
        """Comparison"""
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.__age == other.__age and \
                   self.__name == other.__name

    def __lt__(self, other):
        """lt function"""
        if type(self) != type(other):
            return False
        return self.__age < other.__age()

    def __ge__(self, other):
        if type(self) != type(other):
            return False
        return self.__age() >= other.__age()

    class Student(Person):
        """Student is a subclass of person"""

        def __init__(self, grade=0, enrollement=0):
            """enrollement 1 is part time, 2 is full time"""
            self.grade = grade
            self.__gpa = gpa
            super().__init__()

        def calc_gpa():
            total = 0
            for elements in grades:
                if element == "A+":
                    total = total = 4.0
                elif element == "A":
                    total = total + 4.0
                elif element == "A-":
                    total = total + 3.7
                elif element == "B":
                    total = total + 3.0
                elif element == "B-":
                    total = total + 2.7
                elif element == "C+":
                    total = total + 2.3
                elif element == "C":
                    total = total + 2.0
                elif element == "C-":
                    total = total + 1.7
                elif element == "D":
                    total = total + 1.0
            gpa = total / 6
            print(calc_gpa)

        def __str__(self):
            return (str(self.__grade) + " is " + str(self.__gpa) + " a gpa of.")

        def __repr__(self):
            return "Grade = " + str(self.__grade + ", gpa = " + str(self.__gpa)

        def __eq__(self, other):
            """Comparison"""

        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.__grade == other.__grade and \
                   self.__gpa == other.__gpa


def __lt__(self, other):
    """lt function"""
    if type(self) != type(other):
        return False
    return self.__grade < other.__gpa()


def __ge__(self, other):
    """ge"""


if type(self) != type(other):
    return False
return self.__grade >= other.__gpa()









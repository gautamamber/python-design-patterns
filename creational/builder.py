"""
Builder Design Pattern: Separate the construction of a complex object
from its representation so that the same construction process
can create different representation. Allows construct complex objects step by step
It is basically designed to provide flexibility to the solutions to various object creation problems in object-oriented
programming.
Lets take an example of course structure
"""


class Course:

    def __init__(self):
        self.fee()
        self.available_batches()

    def fee(self):
        """
        fees method
        :return:
        """
        raise NotImplementedError

    def available_batches(self):
        """
        Number of available batches
        :return:
        """
        raise NotImplementedError

    def __repr__(self):
        return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)


class DataStructureClass(Course):
    """
    Class for Data structure and algorithms
    """
    def fee(self):
        """
        return fee for data st course
        :return:
        """
        self.fee = 8000

    def available_batches(self):
        """
        return available batches
        :return:
        """
        self.batches = 5

    def __str__(self):
        return "Data structure"


class SoftwareDevelopment(Course):
    """
    Class for Software development
    """
    def fee(self):
        """
        return fee for SDE course
        :return:
        """
        self.fee = 8000

    def available_batches(self):
        """
        return available batches
        :return:
        """
        self.batches = 5

    def __str__(self):
        return "software development"


class ComplexCourse:

    def __repr__(self):
        return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)


    # Complex course
class Complexcourse(ComplexCourse):

    def fee(self):
        self.fee = 7000

    def available_batches(self):
        self.batches = 6


def construct_course(cls):
    """
    construct a course
    :param cls:
    :return:
    """
    course = cls()
    course.fee()
    course.available_batches()
    return course


if __name__ == "__main__":
    dsa = DataStructureClass()
    sd = SoftwareDevelopment()
    complex_course = construct_course(Complexcourse)
    print(complex_course)

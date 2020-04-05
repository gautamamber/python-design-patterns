"""
Abstract Factory Method is a creational design patterns: It allows you to produce
the families of related objects without specifying  their concrete class. It provides a way to encapsulate a group of
individual factories. Basically, here we try to abstract the creation of the objects depending on the logic, business,
platform choice, etc.
"""
import random


class AbstractFactoryCoursesInstitute:
    """
    Portal of courses of institute
    """
    def __init__(self, course_factory=None):
        """
        course  factory is abstract factory
        :param course_factory:
        """
        self.course_factory = course_factory

    def show_course(self):
        """
        Create and show course
        :return:
        """
        course = self.course_factory()
        print(course)
        print(course.fee)


class DataStructure:
    """
    Data structure and algorithm course
    """
    def fee(self):
        """
        course fee
        :return:
        """
        return 4000

    def __str__(self):
        """
        return string
        :return:
        """
        return "Data structure"


class SoftwareDevelopment:
    """
    Data structure and algorithm course
    """
    def fee(self):
        """
        course fee
        :return:
        """
        return 7000

    def __str__(self):
        """
        return string
        :return:
        """
        return "Software Development"


def random_course():
    """
    A random class for choosing course
    :return:
    """
    return random.choice([DataStructure, SoftwareDevelopment])


if __name__ == "__main__":
    courses = AbstractFactoryCoursesInstitute(random_course)

    for i in range(5):
        courses.show_course()


"""
Advantages:
Easy to introduce new variants of the products without breaking the existing code.
"""

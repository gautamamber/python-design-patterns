"""
Singleton design patterns: It is one of the creational design pattern. To provide one and
only one object of a particular type
The singleton pattern is a design pattern that restricts the instantiation of a class to one object.
Singleton behavior can be implemented by Borg’s pattern but instead of having only one instance of the class there are
multiple instances that share the same state
"""


class BorgMethod:
    """
    state shared by each instance
    """
    __shared_state = dict()

    def __int__(self):
        """

        :return:
        """
        self.__dict__ = self.__shared_state
        self.state = "Singleton Design pattern"

    def __str__(self):
        """
        return state
        :return:
        """
        return self.state


if __name__ == "__main_":
    p1 = BorgMethod()
    p2 = BorgMethod()

    p1.state = "Hello"
    p2.state = "World"

    print(p1)
    print(p2)


"""
Advantages:
1. Objects created by singleton method is initialized only when it is 
requested for the first time
2. Can not have more than one instance
"""

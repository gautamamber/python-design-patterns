"""
Adapter Design pattern: Create a bridge between two incompatible interfaces
"""


class MotorCycle:
    """
    Class for motor cycle
    """
    def __init__(self):
        self.name = "Motor cycle"

    def two_wheeler(self):
        return "Two wheeler"


class Car:
    """
    Class for car
    """
    def __init__(self):
        self.name = "Car"

    def four_wheeler(self):
        return "Four wheeler"


class Truck:
    """
    class for truck
    """
    def __init__(self):
        self.name = "Truck"

    def eight_wheeler(self):
        return "Eight wheeler"


class Adapter:
    def __init__(self, obj, **adapter_methods):
        """
        set adapter methods in the object's dict
        :param obj:
        :param adapter_methods:
        """
        self.obj = obj
        self.__dict__.update(adapter_methods)

    def __getattr__(self, item):
        return getattr(self.obj, item)


if __name__ == "__main__":
    objects = []
    car = Car()
    objects.append(Adapter(car, wheels=car.four_wheeler))
    for obj in objects:
        print(obj.name, obj.wheels())

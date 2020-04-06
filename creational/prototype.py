"""
Prototype Design Pattern: It is a design pattern which aim to reduce
the number of classes for an application. It allows you to copy
existing objects independent of the concrete implementation of their classes.
The object is created by copying a prototypical instance during run-time.
"""


class Prototype:

    value = "default"

    def clone(self, **attrs):
        """
        clone prototype
        :return:
        """
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher:

    def __init__(self):
        self.objects = {}

    def get_objects(self):
        """
        Get all objects
        :return:
        """
        return self.objects

    def register_objects(self, name, obj):
        """
        Register an object
        :return:
        """
        self.objects[name] = obj

    def unregister_object(self, name):
        """
        Unregister object
        :param name:
        :return:
        """
        del self.objects[name]

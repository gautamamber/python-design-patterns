"""
Observer: Allows you to define or create a subscription mechanism to send the notification to multiple objects
about any new event that happens to the object that they are observing. The subject is basically observed by multiple
objects. The subject needs to be monitored and whenever there is a change in the subject, the observers are being
notified about the change
"""


class Subject:
    """
    Represent what is being observed
    """
    def __init__(self):
        """
        create an empty observer
        """
        self._observer = []

    def notify(self, modifier=None):
        """
        Alerts the observers
        :param modifier:
        :return:
        """
        for observer in self._observer:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        """
        If observer is not in the list append it into list
        :param observer:
        :return:
        """
        if observer not in self._observer:
            self._observer.append(observer)

    def detach(self, observer):
        """
        Remove the observer from the list
        :return:
        """
        try:
            self._observer.remove(observer)
        except:
            pass


class Data(Subject):
    """
    Monitor the object
    """

    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class HexaViewer:
    """
    Update the HexaViewer
    """
    def update(self, subject):
        print('HexViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))


class OctalViewer:
    """
    updates the Octal viewer
    """

    def update(self, subject):
        print('OctalViewer: Subject' + str(subject.name) + 'has data ' + str(oct(subject.data)))


if __name__ == "__main__":
    obj1 = Data('data1')
    obj2 = Data('data2')

    view1 = OctalViewer()
    view2 = HexaViewer()

    obj1.attach(view1)
    obj1.attach(view2)
    obj1.data = 10


"""
Advantages: 
It follows open close principles
It carefully describes about the coupling present between the objects and the observer.
"""
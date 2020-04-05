"""
Facade Design pattern: It provides an easier way to access methods of the underlying systems by providing a single
entry point.
 It will help us to hide or abstract the complexities of the subsystems
"""


class Washing:
    """
    Subsystem one
    """
    def wash(self):
        """
        washing the clothes
        :return:
        """
        print("washing")


class Rinsing:
    """
    Subsystem two
    """
    def rinse(self):
        """
        rinsin the clothes
        :return:
        """
        print("Rinsing")


class Spinning:
    """
    Subsystem three
    """
    def spinning(self):
        """
        spinning the clothes
        :return:
        """
        print("Spinning")


class WashingMachine:
    """
    Facade
    """
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def start_washing(self):
        """
        start washing the clothes
        :return:
        """
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spinning()


if __name__ == "__main__":

    washing_machine = WashingMachine()
    washing_machine.start_washing()
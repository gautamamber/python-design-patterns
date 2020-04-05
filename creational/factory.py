"""
Factory Design Pattern: Factory method is a creational design pattern that allows interface or a class to create
an object, but let subclasses decides which classes or objects to instantiate
Example code with factory method, lets create language converter program..
"""


class FrenchLocalizer:
    """
    It returns the french version of the message
    """
    def __init__(self):
        self.translations = {
            'car': 'voiture',
            'bike': 'bicycle',
            'hello': 'bojure'
        }

    def localize(self, message):
        """
        change the message using translation
        :return:
        """
        return self.translations.get(message, message)


class SpanishLocalizer:
    """
    It returns the Spanish version of the message
    """
    def __init__(self):
        self.translations = {
            'car': 'coche',
            'bike': 'bicicleta',
            'hello': 'zompa'
        }

    def localize(self, message):
        """
        change the message using translation
        :return:
        """
        return self.translations.get(message, message)


class EnglishLocalizer:
    """
    Return as it is for English
    """
    def localize(self, message):
        """
        return for english
        :param message:
        :return:
        """
        return message


def factory_version(language='English'):
    """
    Factory method for calling Localizers
    :param language:
    :return:
    """
    localizer = {
        'french': FrenchLocalizer,
        'spanish': SpanishLocalizer,
        'English': EnglishLocalizer
    }
    return localizer[language]()


if __name__ == "__main__":
    french = factory_version("french")
    spanish = factory_version("spanish")
    english = factory_version("English")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(french.localize(msg))
        print(english.localize(msg))


"""
Advantages of Factory Methods:
1. We can easily add new types of products without disturbing the existing 
code.
2. Tight coupling being avoided
"""

# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):
        """This is the constructor, this initialises the name and birth, only if
        the name is a string and not empty and the birth is a date object"""
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if name == "":
            raise ValueError("Name cannot be empty.")
        if not isinstance(birth, date):
            raise TypeError("Date of birth must be a datetime.date object.")
        else:        
            self.name = name
            self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        """This is the initials method, this takes the name and splits it into a list of words
        then the first letter of each word is taken and combined into one string to give the intials of the persons name"""
        Uppercased = self.name.split()
        initialsList = [word[0].upper() for word in Uppercased]
        initials = ''.join(initialsList)
        return initials

    def is_birthday(self):
        """This is the is_birthday method, this checks if the current date is equal to the persons date of birth"""
        today = date.today()
        if today.day == self.birth.day and today.month == self.birth.month:
            return True
        else:
            return False
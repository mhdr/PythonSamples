__author__ = 'mahmood'


class Person:
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0

    @staticmethod
    def initialize(first_name:str, last_name:str, age:int) -> 'Person':
        new_person = Person()

        new_person.first_name = first_name
        new_person.last_name = last_name
        new_person.age = age

        return new_person

    def print(self):
        out = "{0} {1} {2} years old".format(self.first_name, self.last_name, self.age)
        print(out)
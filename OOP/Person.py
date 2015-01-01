__author__ = 'mahmood'

class Person :
    first_name=""
    last_name=""
    age=0

    nick_name=""

    # initializer
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    # static method
    def initialize(first_name,last_name,age,nick_name):
        new_person=Person(first_name,last_name,age)
        new_person.nick_name=nick_name
        return new_person

    def print_person(self):
        if self.nick_name:
            out="{0} {1} ({2}) {3} years old".format(self.first_name,self.last_name,self.nick_name,self.age)
        else :
            out="{0} {1} {2} years old".format(self.first_name,self.last_name,self.age)

        print(out)

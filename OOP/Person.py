__author__ = 'mahmood'

class Person :
    first_name=""
    last_name=""
    age=0

    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    def print_person(self):
        out="{0} {1} {2} years old".format(self.first_name,self.last_name,self.age)
        print(out)

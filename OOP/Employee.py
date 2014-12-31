from Person import Person

__author__ = 'mahmood'

class Employee():
    person=0
    salary=0

    def __init__(self,person,salary):
        self.person=person
        self.salary=salary

    def print_salary(self):
        out="{0} {1}'s salary is {2}".format(self.person.first_name,self.person.last_name,self.salary)
        print(out)


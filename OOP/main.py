from Employee import Employee
from Person import Person

__author__ = 'mahmood'



person1=Person("Mahmood","Ramzani",29)
person1.print_person()

person2=Person("Javad","Najafi",30)
person2.print_person()

employee1=Employee(person1,10000)
employee1.print_salary()

employee2=Employee(person2,20000)
employee2.print_salary()

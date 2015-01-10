__author__ = 'mahmood'

from Person import Person

list=[]

person1=Person.initialize("Mahmood","Ramzani",29)
person2=Person.initialize("Javad","Najafi",30)
person3=Person.initialize("Mahmood","Rohani",29)

list.append(person1)
list.append(person2)
list.append(person3)

result=[x for x in list if x.first_name=="Mahmood"]

for p in result:
    print(p.print())
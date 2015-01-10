__author__ = 'mahmood'

from PeopleBL import PeopleBL

people=PeopleBL()

people.insert("Mahmood","Ramzani",1985,5,22)
people.insert("Majeed","Dourandish",1985,7,20)
people.insert("Mohsen","Dourandish",1986,6,12)
people.insert("Javad","Najafi",1984,9,10)
people.insert("Mahmood","Rohani",1985,1,2)


result=people.get_first_name("Mahmood")
for person in result:
    print(person)
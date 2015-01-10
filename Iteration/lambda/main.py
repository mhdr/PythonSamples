__author__ = 'mahmood'

from Person import Person
from People import People

people=People()
matches=people.search(lambda x : x.first_name=="Mahmood")

for p in matches:
    print(p.print())
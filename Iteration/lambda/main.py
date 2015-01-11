__author__ = 'mahmood'

from People import People

people=People()

matches=people.search(lambda x : x.first_name=="Mahmood")
people.search()
for p in matches:
    print(p.print())
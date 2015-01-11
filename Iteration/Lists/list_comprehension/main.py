__author__ = 'mahmood'

from People import People

people=People()
list=people.get()

result=[x for x in list if x.first_name=="Mahmood"]

for p in result:
    print(p.print())
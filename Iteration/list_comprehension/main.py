__author__ = 'mahmood'

from People import People

people=People()
list=People.get()

result=[x for x in list if x.first_name=="Mahmood"]

for p in result:
    print(p.print())
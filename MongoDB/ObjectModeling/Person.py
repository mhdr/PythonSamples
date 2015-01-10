__author__ = 'mahmood'

from BirthDate import BirthDate

class Person :
    first_name=""
    last_name=""
    birth_date=BirthDate()

    def initialize(first_name,last_name,year,month,day):
        new_person=Person()
        new_person.first_name=first_name
        new_person.last_name=last_name
        new_person.birth_date=BirthDate.initialize(year,month,day)
        
        return new_person


    def dic(self):
        result={"first_name":self.first_name,
                "last_name":self.last_name,
                "birth_date":self.birth_date.dic()}

        return result
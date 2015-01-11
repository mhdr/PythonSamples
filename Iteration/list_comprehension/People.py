__author__ = 'mahmood'

from Person import Person

class People:

    def get(self)->list[Person]:
        people_list = []


        new_person1 = Person.initialize("Mahmood", "Ramzani", 29)
        new_person2 = Person.initialize("Javad", "Najafi", 30)
        new_person3 = Person.initialize("Mahmood", "Rohani", 29)

        people_list.append(new_person1)
        people_list.append(new_person2)
        people_list.append(new_person3)

        return people_list





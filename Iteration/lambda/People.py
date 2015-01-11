__author__ = 'mahmood'

from Person import Person

class People:

    def get(self)->'list[Person]':
        """ get all people
        :return:list of all people
        :rtype:list[Person]
        """
        people_list = []


        new_person1 = Person.initialize("Mahmood", "Ramzani", 29)
        new_person2 = Person.initialize("Javad", "Najafi", 30)
        new_person3 = Person.initialize("Mahmood", "Rohani", 29)

        people_list.append(new_person1)
        people_list.append(new_person2)
        people_list.append(new_person3)

        return people_list

    def search(self, predicate:'function')->'list[Person]':
        """ filter list of people using predicate
        :param predicate: lambda expression
        :return:filtered list of people with lambda expression
        :rtype:list[Person]
        """
        people_list = self.get()

        result=[]

        for p in people_list:
            if predicate(p):
                result.append(p)

        return result





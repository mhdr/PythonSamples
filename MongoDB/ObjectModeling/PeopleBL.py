__author__ = 'mahmood'

from Person import Person
from pymongo import MongoClient


class PeopleBL:
    __client = None
    __db = None
    __people = None

    def __init__(self):
        self.__client = MongoClient()
        # database
        self.__db = self.__client["test-db"]
        # table
        self.__people = self.__db["People"]


    def insert(self, first_name, last_name, year, month, day):
        new_person1 = Person.initialize(first_name, last_name, year, month, day)
        id = self.__people.insert(new_person1.dic())
        return id

    def get_one_first_name(self,first_name):
        match = self.__people.find_one({"first_name": first_name})
        return match

    def get_first_name(self,first_name):
        match = self.__people.find({"first_name": first_name})
        return match

    def get_one_last_name(self,last_name):
        match = self.__people.find_one({"last_name": last_name})
        return match


    def get_last_name(self,last_name):
        match = self.__people.find_one({"last_name": last_name})
        return match
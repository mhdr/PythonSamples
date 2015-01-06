__author__ = 'Mahmood'

import configparser

config=configparser.ConfigParser()
config.read("config.ini")
first_name=config.get("Default","FirstName")
last_name=config.get("Default","LastName")
age=config.get("Default","Age")
city=config.get("Public","City")

out="{0} {1} {2} years old from {3}".format(first_name,last_name,age,city)
print(out)
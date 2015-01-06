__author__ = 'Mahmood'

import configparser

config_file=open("config2.ini","w")

config=configparser.ConfigParser()
config.add_section("Default")
config.set("Default","FirstName","Mahmood")
config.write(config_file)
config_file.close()

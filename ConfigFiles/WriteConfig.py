__author__ = 'Mahmood'

# first create a config file
import CreateConfig
import configparser

config=configparser.ConfigParser()
config.read("config2.ini")

# open the file for write but truncate it first
config_file=open("config2.ini","w")

config.set("Default","LastName","Ramzani")
config.write(config_file)
config_file.close()
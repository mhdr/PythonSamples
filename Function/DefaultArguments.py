__author__ = 'mahmood'

# Default arguments
def printinfo(name, age=29):
    print("Name: ", name)
    print("Age ", age)

printinfo( age=50, name="Mahmood" )
printinfo( name="Mahmood" )
__author__ = 'mahmood'

# Variable-length arguments
def printinfo(name,*grades) :
    print(name)
    for grade in grades :
        print("Garde : ",grade)
    print("...")


printinfo("Mahmood",19)
printinfo("Majeed",17,12)
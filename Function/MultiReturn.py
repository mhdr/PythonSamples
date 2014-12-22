__author__ = 'mahmood'

# multi return
def printinfo2(name1,name2) :
    greeting1="Hello {0}".format(name1)
    greeting2="Hello {0}".format(name2)
    return greeting1 , greeting2

gr1,gr2= printinfo2("Mahmood","Majeed")
print(gr1)
print(gr2)
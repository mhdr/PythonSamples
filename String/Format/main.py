__author__ = 'mahmood'

name1 = "Mahmood"
name2 = "Javad"
name3 = "Mehdi"

output1 = "{0} {1} {2}".format(name1, name2, name3)
print(output1)

output2 = "{2} {1} {1}".format(name1, name2, name3)
print(output2)

output3 = "{} {} {}".format(name1, name2, name3)
print(output3)

output4 = "{0} {0} {0}".format(name1)
print(output4)

output5 = "{nm1} {nm2} {nm3}".format(nm1=name1, nm2=name2, nm3=name3)
print(output5)

# decimal, hex, octal, binary
print("{0:d} - {0:x} - {0:o} - {0:b} ".format(21))

# Use Format as a Function
output6 = "{0} {0} {0}".format
print(output6("Mahmood"))

# Escaping Braces
print("The empty set is often represented as {{0}} ".format())
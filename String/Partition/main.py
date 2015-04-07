__author__ = 'mahmood'

name = "Mahmood Ramzani"
fname ,separator,lname= name.partition(" ")

print(fname)
print(separator)
print(lname)

# skip separator
fname ,_,lname= name.partition(" ")
print(fname)
print(lname)
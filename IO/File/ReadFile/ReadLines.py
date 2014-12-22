salaryFile=open("trans.dat")

# read all lines of file
allLines=salaryFile.readlines()


salaryList=[]
for line in allLines:
    salaryList.append(line[15:].strip("\n"))

salaryList.sort(reverse=True)

i=1
for s in salaryList :
    output="{0} : {1}".format(i,s)
    print(output)
    i+=1

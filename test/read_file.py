
import sys

myfile = open ("file","r+")


#print myfile.name


mylist = []

for line in myfile.readlines():
    mylist.append(line)

print mylist

for router in mylist:
    print router



myfile.close()
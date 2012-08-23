
import sys

myfile = open ("file","r+")


#print myfile.name


mylist = []
router_type = []

for line in myfile.readlines():
    mylist.append(line)
    i=line.rstrip().split()
    router_type.append(i)
    
    
print mylist
print router_type
print router_type[1][1]

for router in mylist:
    print router
    



myfile.close()
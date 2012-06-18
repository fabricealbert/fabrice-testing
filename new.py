#!/usr/bin/python
name = raw_input("what's your name ")
print ("hello  " + name + "!")
 

database= [
    ['fabrice','1234'],
    ['john','5678'],
    ['sal','0000']
    ]

username=raw_input("user ")
pin=raw_input("pin ")
if [username,pin] in database: print "granted"

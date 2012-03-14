# factorial function
def factorial (number):
    if number <=1:
        return 1
    else:
        return number*factorial(number-1)


# old way of doing factorial    
#    product = 1
#    for i in range(number):
#        product = product * (i+1)
#    return product

#----------------------------------
# fibonacci function

def fibonacci (n):
    if n==0 or n==1:
        return n
    else:
        return(fibonacci(n-2)+fibonacci(n-1))


# iterative fibonacci
#   terms = [0,1]
#    i=2
#    while i<=n:
#        terms.append(terms[i-1]+terms[i-2])
#        i=i+1
#    return terms[n]
#                     



#---------------------------------------
#below is user input and variables

#user_input = input("enter a number for !   ")
user_input2 = input("enter the term for Fibonacci   ")

        
terms = [0]
i=1
while i<= user_input2:
     terms.append(fibonacci(i))
     i=i+1
         

#-----------------------------------------
# below is screen output



#print user_input,"!=",factorial(user_input)
print "Fibonacci term for ",user_input2,"is", fibonacci(user_input2) 
print terms 
    



# Multiply 3 and any number

def mult(number):
 return(3*number);






# adds two numbers together

def add(a, b):
 return(a+b);



# Data structure

numbers = [1,2,3,6]

def sumOfListNumbers(someList):
 sum=0;
 for i in someList:
  sum=sum + i
 return sum;




# Program checker (do not change the lines below)

assert sumOfListNumbers(numbers) == 12

assert mult(3) == 9

assert add(1,3) == 4

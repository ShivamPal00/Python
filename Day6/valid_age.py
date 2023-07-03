# Write a program that asks the user to enter their age. Use an assert statement to raise an AssertionError if the age entered is negative. Handle this exception by displaying an error message

age=int(input("enter the age"))

assert(age>0),"pls enter the valid age postive no "
print("given age is valid",age)
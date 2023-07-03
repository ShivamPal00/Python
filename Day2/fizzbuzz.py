
# Write a program that prints the numbers from 1 to 100 and for multiples of ‘3’ print “Fizz” instead of the number and for the multiples of ‘5’ print “Buzz”. If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".


for i in range(1,101):
    if(i%3==0 and i%5==0):
        print("FizzBuzz",end=" ")
    elif(i%3==0):
        print("Fizz",end=" ")
    elif(i%5==0):
        print("Buzz",end=" ")
    else:    
        print(i,end=" ")    

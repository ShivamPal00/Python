# If b2 − 4ac > 0, the equation has 2 real solutions.
# if b2 − 4ac = 0, the equation has 1 real solution.
# if b2 − 4ac < 0, the equation has 2 complex solutions.


print("The give quadratic equation is ax^2+bx+c=0")
print("Please enter the value a b c")

a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))

num = pow(b,2)-(4*a*c)

if(num>0):
    print("the equation has 2 real solutions")
elif(num==0):
    print("the equation has 1 real solution")
elif(num<0):
    print("the equation has 2 complex solutions")
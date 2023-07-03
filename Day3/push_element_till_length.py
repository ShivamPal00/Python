# Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num until the list length reaches length.

num=int(input("enter the value"))
length=int(input("enter the length"))


l=[]

for i in range(1,length+1):
    n=num*i
    l.append(n)
print(l)

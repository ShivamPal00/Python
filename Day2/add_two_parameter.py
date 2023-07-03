# Write a program that takes two parameters and, if both parameters are strings, add them as if they were integers or if the two parameters are integers, concatenate them. If the two parameters are different data types, return None. All parameters will either be strings or integers.

a=""
b=""

for i in range(0,2):
    type_=input("enter type of input")
    if(type_=="int"):
        if(i==0):
            a=int(input())
        else:
            b=int(input())    
        
    else:
        if(i==0):
            a=input()
        else:
            b=input()    

        
s=""

if(type(a)==int and type(b)==int):
    s =str(a)+str(b)
elif(type(a)== str and type(b)== str):
    s=int(a)+int(b)
else:
    print("none")        

print(s)
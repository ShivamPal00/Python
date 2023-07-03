print("press 1 to reverse the string ")
print()
print("press 2 to encrypt the vowels present in the string ")
print()
print("press 3 to encrypt by adding aca ")
print()
print("press 4 to do all the things mention above  ")



num=int(input())

print("enter the string for encryption")
str=list(input())


rstr=""

# a => 0 
# e => 1 
# i => 2 
# o => 2 
# u => 3 


if(num==1):
    rstr=str[::-1]
elif(num==2):
    rstr=str
    for i in range(0,len(rstr)):
        if(rstr[i]=="a"):
            rstr[i]="0"
        elif(rstr[i]=="e"):
            rstr[i]="1"
        elif(rstr[i]=="i"):
            rstr[i]="2"
        elif(rstr[i]=="o"):
            rstr[i]="3"
        elif(rstr[i]=="u"):
            rstr[i]="4"                    
elif(num==3):
    rstr=str
    rstr+="aca"
elif(num==4):
    rstr=str[::-1]
    for i in range(0,len(rstr)):
        print(i)
        if(rstr[i]=="a"):
            rstr[i]="0"
        elif(rstr[i]=="e"):
            rstr[i]="1"
        elif(rstr[i]=="i"):
            rstr[i]="2"
        elif(rstr[i]=="o"):
            rstr[i]="3"
        elif(rstr[i]=="u"):
            rstr[i]="4"  
    rstr+="aca"
else:
    print("pls enter the valid input")
    num=int(input())

print("The encryption string is :")
print(rstr)


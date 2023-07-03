# Write a program For Converting Roman Numerals To Decimal Lying Between 1 to 4999.
# Symbol Value
# I              1
# IV           4 
# V            5 
# IX           9 
# X            10 
# XL          40 
# L            50 
# XC         90 
# C           100
# CD         400 
# D          500 
# CM      900 
# M       1000



s=input("enter the roman value")

ns=[]

for i in range(0,len(s)):
    if(s[i]=='I'):
        ns.append(1)
    elif(s[i]=="V"):
        ns.append(5)
    elif(s[i]=="X"):
        ns.append(10)
    elif(s[i]=="L"):
        ns.append(50)
    elif(s[i]=="C"):
        ns.append(100)                
    elif(s[i]=="D"):
        ns.append(500)
    elif(s[i]=="M"):
        ns.append(1000)        
# print(ns)        

max_value=max(ns)
max_index=ns.index(max_value)

# print(max_value)
# print(max_index)

left =ns[:max_index]
right=ns[max_index:]


# print(left)
# print(right)

leftsum=0
rightsum=0

for i in range(0,max_index):
    leftsum=leftsum+ns[i]

for i in range(max_index,len(ns)):
    rightsum=rightsum+ns[i]


ans =rightsum-leftsum
print(ans)    
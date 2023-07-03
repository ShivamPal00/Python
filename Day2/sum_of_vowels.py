# Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers.

# a-4
# e-3
# i-1
# o-0
# u-0

s =str(input())

sum=0

for i in range(0,len(s)):
    if(s[i]=="a"):
        sum=sum+4
    elif(s[i]=="e"):
        sum=sum+3
    elif(s[i]=="i"):
        sum=sum+1
    elif(s[i]=="o"):
        sum=sum+0
    elif(s[i]=="u"):
        sum=sum+0                

print(sum)
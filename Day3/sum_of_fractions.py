# Create a function that takes a list containing nested lists as an argument. Each sublist has 2 elements. The first element is the numerator and the second element is the denominator. Return the sum of the fractions rounded to the nearest whole number.


l=[]

for i in range(0,2):
    r=[]
    for j in range(0,2):
        n=int(input())
        r.append(n)
    l.append(r)    
print(l)    

sum=0

for i in range(0,2):
    sum=l[i][0]/l[i][1]+sum
sum=format(sum,'.1f')
print(sum)
decimal=sum.split('.')
print(decimal)
ans=int(decimal[0])
if(int(decimal[1])>5):
    ans=ans+1


print(ans)
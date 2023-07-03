import array
decimal=int(input("enter the decimal"))

ans=0
i=0
while(decimal):
    rem=decimal%2
    # print(rem)
    ans =ans+rem*pow(10,i)
    # print(ans)
    
    decimal=decimal//2
    i=i+1
    
    
   
print(decimal,"decimal to binay is",ans)
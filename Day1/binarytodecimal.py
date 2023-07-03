import array

n =int(input("length of the array"))
a=[]
for i in range(0,n):
    val=int(input())
    a.append(val)
# print(a)  
ans =0
for i in range(0,n):
   
    if(a[i]==1):
        ans=ans+pow(2,n-1-i)
# print(ans)   

print(a,"binary to decimal is",ans)

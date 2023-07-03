n=int(input())
bool=False
for i in range(1,n+1):
    l=[]
    sum=i
    l.append(i)

    for j in range(i+1,n+1):
        sum=sum+j

        if(sum>n):
            l=[]
            break
        elif(sum==n):
            bool=True
            l.append(j)
            break
        else:
            l.append(j)
    if(bool==True):
        break
print(l)

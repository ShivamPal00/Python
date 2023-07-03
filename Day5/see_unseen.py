n=int(input())

m=[]
if(n>0):
    for i in range(0,n):
        r=[]
        for j in range(0,n):
            if(i==j):
                r.append(1)
            else:
                r.append(0)
        m.append(r)
else:
    n=abs(n)
    for i in range(0,n):
        r=[]
        for j in range(0,n):
            if(i==n-1-j):
                r.append(1)
            else:
                r.append(0)
        m.append(r)

print(m)                

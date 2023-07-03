n=int(input())

max=n
while(n>1):
    if(n%2==0):
        n=n/2
        if(max<n):
            max=n
        print("even",n,end=" ")    
    else:
        n=n*3+1 
        if(max<n):
            max=n   
        print("odd",n,end=" ")    
print()
print("Max no. is ",max)            
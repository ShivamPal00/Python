# Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.
n=[]

for i in range(1,10):
    p=int(input())
    n.append(p)


print(n)  

n=sorted(n)
print(n)


for i in range(1,len(n)+1):
    if(i!=n[i-1]):
        print("missing value is ",i)
        break


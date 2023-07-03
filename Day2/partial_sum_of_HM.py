# In mathematics, the harmonic series is the divergent infinite series:

# Write a program that, given a precision parameter n, returns the value of the partial sum of the harmonic series up to n terms.



n=int(input())

sum=0

for i in range(1,n+1):
    sum=sum+1/i
print(sum)
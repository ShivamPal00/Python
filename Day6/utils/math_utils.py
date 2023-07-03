def factorial(n):
    ans=1
    for i in range(1,n+1):
        ans=ans*i
    return ans    

def ifPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True    
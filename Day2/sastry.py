# Write a program to establish if a given integer n is a Sastry number. If the number resulting from the concatenation of an integer n with its successor is a perfect square, then n is a Sastry Number.
# Example: Input: 183  Output: True 
# Concatenation of n and its successor = 183184 
# 183184 is a perfect square (428 ^ 2)


n=int(input())

n1=  int(str(n)+str(n+1))
print(n1)

square_root=pow(n1,1/2)
s=str(square_root)
s=s.split('.')
# print(s)


if(int(s[1])==0):
    print("The given no. is Sastry no.")
else:
    print("The given no. is not a Sastry no.")    
    
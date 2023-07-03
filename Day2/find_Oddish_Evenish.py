# Write a program that determines whether a number is Oddish or Evenish. A number is Oddish if the sum of all of its digits is odd, and a number is Evenish if the sum of all of its digits is even. If a number is Oddish, return "Oddish". Otherwise, return "Evenish".


n=int(input())

n1=n
sum=0
while(n1):
    digit=n%10
    sum=sum+digit
    n1=n1/10
if(sum%2==0):
    print("The given no. is Evenish")
else:
    print("The given no is Oddish")        
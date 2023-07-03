# A number is said to be Harshad if it's exactly divisible by the sum of its digits. Write a program that determines whether a number is a Harshad or not.


n=int(input())

digit_sum=0

while(n):
    digit=n%10
    digit_sum=digit_sum+digit
    n=n/10
if(n%digit_sum==0):
    print("no. is Harshad no.")
else:
    print("no. is not a Harshad no.")        
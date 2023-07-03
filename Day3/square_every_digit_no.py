# Create a function that squares every digit of a number.


n=int(input("enter the no"))

sum=0
i=0
j=0
while(n):
    digit=n%10
    n=int(n/10)
    square_of_digit=pow(digit,2)

    sum=sum+square_of_digit*pow(10,i+j)

    if(square_of_digit>9):
        j=j+1
    i=i+1
print(sum)
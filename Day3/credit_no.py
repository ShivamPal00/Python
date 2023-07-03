# Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.



n=[]

for i in range(0,16):
    c=int(input())
    n.append(c)

for i in range(0,12):
    n[i]="*"

print(n)
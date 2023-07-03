# Write a function that takes a list of numbers and returns a list with two elements:
# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.



l=[]
for i in range(0,8):
    n=int(input("enter the value"))
    l.append(n)
sumeven=0
sumodd=0
for i in range(0,8):
    if(l[i]%2==0):
        sumeven=sumeven+l[i]
    else:
        sumodd=sumodd+l[i]    
l[0]=sumeven
l[1]=sumodd

print(l)

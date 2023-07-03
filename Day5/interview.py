# Create a function to check if a candidate is qualified in an imaginary coding interview of an imaginary tech startup.
# The criteria for a candidate to be qualified in the coding interview is:
# The candidate should have complete all the questions.
# The maximum time given to complete the interview is 120 minutes.
# The maximum time given for very easy questions is 5 minutes each.
# The maximum time given for easy questions is 10 minutes each.
# The maximum time given for medium questions is 15 minutes each.
# The maximum time given for hard questions is 20 minutes each.
# If all the above conditions are satisfied, return "qualified", else return "disqualified".
# You will be given a list of time taken by a candidate to solve a particular question and the total time taken by the candidate to complete the interview.
# Given a list , in a true condition will always be in the format [very easy, very easy, easy, easy, medium, medium, hard, hard].
# The maximum time to complete the interview includes a buffer time of 20 minutes.


# l=[very easy, very easy, easy, easy, medium, medium, hard, hard]

# l=[5,5,10,10,15,15,20,20]

l=[]
for i in range(0,8):
    if(i<=1):
        n=int(input("enter the time taken by student to solve the very easy questions "))
        l.append(n)
    elif(i>1 and i<4):
        n=int(input("enter the time taken by student to solve the  easy questions "))
        l.append(n)
    elif(i>3 and i<6):
        n=int(input("enter the time taken by student to solve the medium questions "))
        l.append(n)
    elif(i>5 and i<8):
        n=int(input("enter the time taken by student to solve the hard questions "))
        l.append(n)            

sum=sum(l)
print(sum)
maxtime=120
if(sum>maxtime):
    print("not Qualified because")
elif(l[0]+l[1]>10):
    print("not Qualified because you have taken more than 10 mins to solve the very easy questions")
elif(l[2]+l[3]>20):
    print("not Qualified because you have taken more than 20 mins to solve the easy questions")   
elif(l[4]+l[5]>30):
    print("not Qualified because you have taken more than 30 mins to solve the medium questions")
elif(l[6]+l[7]>40):
    print("not Qualified because you have taken more than 40 mins to solve the hard questions")
else:
    print("Qualified")
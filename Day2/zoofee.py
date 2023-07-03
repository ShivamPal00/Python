print("enter no of people")
n =int(input())
cost=0
cost12to65=0
cost2to12=0
cost65above=0
costzero=0
countzero=0
count2to12=0
count12to65=0
count65above=0
for i in range(0,n):
    print("enter the age")
    age=int(input())
    if(age<0):
        print("inavlid input")
        print("please re-enter the valid age")
        age=int(input())   
    if(age<2):
        costzero=costzero+0
        countzero=countzero+1

    elif(age>=2 and age<=12):
    
        cost2to12=cost2to12+14
        count2to12=count2to12+1
    elif(age>12 and age<65 ):
        cost12to65=cost12to65+23
        count12to65=count12to65+1
    else:
        cost65above=cost65above+18  
        count65above=count65above+1
cost = cost65above+cost2to12+costzero+cost12to65       
decimal_cost='{:.2f}'.format(cost)
# print(decimal_cost);   

print("***************************BILL*************************************")
print("  ")
print("age range""             " "no of people""      ""total cost")
print("  ")
print("less than 2""              ",countzero,"               ",costzero)
print("2 to 12""                  ",count2to12,"               ",cost2to12)
print("12 to 65""                 ",count12to65,"               ",cost12to65)
print("65 above""                 ",count65above,"               ",cost65above)
print("    ")
print('total no of people',n)
print("    ")
print("*************************Total Cost********************************")
print("    ")
print("total cost is" ,decimal_cost)
print("    ")
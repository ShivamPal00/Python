team =["rcb","csk","mum","gl","kk"]
val= [0,0,0,0,0]
myDict = dict(zip(team,val))

print(myDict)
# print(list(myDict[1]))
for i in range(0,5):
    for j in range(i+1,5):
        print(team[i] ,"vs" ,team[j])
        score = str(input('enter the name of winning team'))
        if(team[i]==score):
            myDict[team[i]]+=2
            
        elif(team[j]==score):
            myDict[team[j]]+=2
        elif(score=="draw"):
            myDict[team[i]]+=1
            myDict[team[j]]+=1
print(myDict)
myDict =dict(sorted(myDict.items(),key=lambda x:x[1],reverse=True))

print(myDict) 
for key in myDict:
    myDict[key]=0

print(myDict)
print(list(myDict)[0],"VS",list(myDict)[2])
score=str(input())
if(score==list(myDict)[0]):
    myDict[list(myDict)[0]]+=2
else:
    myDict[list(myDict)[2]]+=2    


print(list(myDict)[1],"VS",list(myDict)[3])
score=str(input())
if(score==list(myDict)[1]):
    myDict[list(myDict)[1]]+=2
else:
    myDict[list(myDict)[3]]+=2       


myDict =dict(sorted(myDict.items(),key=lambda x:x[1],reverse=True))
print(myDict)      

print(list(myDict)[0],"VS",list(myDict)[1])
score=str(input())
if(score==list(myDict)[0]):
    myDict[list(myDict)[0]]+=2
else:
    myDict[list(myDict)[1]]+=2    

myDict =dict(sorted(myDict.items(),key=lambda x:x[1],reverse=True))

print("Wining team is:",list(myDict)[0])  
num=str(input())

con =int(num)
bool =False

for i in range(0,len(num)):
    digit=int(num[i])

    if(con%digit==0):
        bool=True
    else:
        bool=False
        break
print(bool)
row =3
col=2
array=[]
for i in range(0,row):
    r=[]
    for j in range(0,col):
        r.append(int(input()))
    array.append(r)    

l1=pow((pow((array[0][0]-array[1][0]),2)+pow((array[0][1]-array[1][1]),2)),(1/2))
l2=pow((pow((array[0][0]-array[2][0]),2)+pow((array[0][1]-array[2][1]),2)),(1/2))
l3=pow((pow((array[1][0]-array[2][0]),2)+pow((array[1][1]-array[2][1]),2)),(1/2))


print(array)  

print("length of the triangle are ",l1,",",l2,",",l3)
print("Perimeter of the triangle are ",l1+l2+l3)
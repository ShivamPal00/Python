    
N=9  
row=9
col=9
array   =               [ [ 3, 0, 6, 5, 0, 8, 4, 0, 0 ],
                       [ 5, 2, 0, 0, 0, 0, 0, 0, 0 ],
                       [ 0, 8, 7, 0, 0, 0, 0, 3, 1 ],
                       [ 0, 0, 3, 0, 1, 0, 0, 8, 0 ],
                       [ 9, 0, 0, 8, 6, 3, 0, 0, 5 ],
                       [ 0, 5, 0, 0, 9, 0, 6, 0, 0 ],
                       [ 1, 3, 0, 0, 0, 0, 2, 5, 0 ],
                       [ 0, 0, 0, 0, 0, 0, 0, 7, 4 ],
                       [ 0, 0, 5, 2, 0, 6, 3, 0, 0 ] ]

def solveSudoko(array,row,col):
   
    if(col==N-1):
        col=0
        row=row+1
    if(array[row][col]>0):
        return solveSudoko(array,row,col+1)




# for i in range(0,row):
#     r=[]
#     for j in range(0,col):
#         r.append(int(input()))
#     array.append(r)  

for i in range(row):
    for j in range(col):
        print(array[i][j],end=" ")
    print()     

print()
print()
print()
print()

# print(array)
solveSudoko(array,0,0)
for i in range(row):
    for j in range(col):
        print(array[i][j],end=" ")
    print()  
# print(array)


# check the sudoko is valid or not


# 

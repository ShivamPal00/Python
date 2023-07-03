# Given three lists of integers: lst1, lst2, lst3, return the sum of integers which are common in all three lists.

def intersection(lst1, lst2,lst3):
    return list( list(lst1) &  list(lst2) & list(lst3))

l1=[1,2,2]
l2=[5,2,1,2,9,2]
l3=[5,1,1,2,2]




l4 = []
for i in l1:
  if i in l2 and i in l3:
    l4.append(i)
 
print(l4)


sum=0

for i in range(0,len(l4)):
    sum=sum+l4[i]

print(sum) 
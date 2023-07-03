# Create a function that returns the indices of all occurrences of an item in the list.

l=[1,2,1]

ansl=set(l)
ans=[]
for i in l:
    if i in ansl:
        ans.append(i)


print(ans)
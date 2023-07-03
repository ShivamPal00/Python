# Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.


namedict={}

for i in range(0,3):

    key=input("enter the key ")
    name=input("enter the name ")
    namedict[key]=name

namedict =dict(sorted(namedict.items(),key=lambda x:x[1],reverse=False))

print(list(namedict))
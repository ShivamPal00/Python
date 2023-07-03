# Write a function in Python to count and display the total number of words in a text file



def display():
    f = open("C:\Python\Day6\shivam.txt","r")
    l=f.readlines()
    count=0
    for i in l:
        word=i.split()
        
        for j in word:
            count=count+1
    print("total no of word present in file is",count)
        
    f.close()
display()
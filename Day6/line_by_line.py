# Write a function in python to read the content from a text file "poem.txt" line by line and display the same on screen


def display():
    f = open("C:\Python\Day6\shivam.txt","r")
    l=f.readlines()
    for i in l:
        print(i,end=" ")
        
    f.close()
display()
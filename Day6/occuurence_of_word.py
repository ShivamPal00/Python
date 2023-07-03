# Write a function in Python to read lines from a text file "notes.txt". Your function should find and display the occurrence of the word "the“


def display():
    f = open("C:\Python\Day6\shivam.txt","r")
    l=f.readlines()
    count=0
    for i in l:
        word=i.split()
        print(word)
        for j in word:
            if(j=="the"):
                count=count+1
    print("no of 'the'  present in file is ",count)
        
    f.close()
display()
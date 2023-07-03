# # Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "T“



def display():
    f = open("C:\Python\Day6\shivam.txt","r")
    l=f.readlines()
    count=0
    for i in l:
        word=i.split()
        print(word)
        i=0
        for j in word:
            if(j[i]=='t'):
                i=i+1
                count=count+1
    print("no of 'the'  present in file is ",count)
        
    f.close()
display()
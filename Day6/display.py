
# Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters




def display():
    f = open("C:\Python\Day6\shivam.txt","r")
    l=f.readlines()
    for i in l:
        word=i.split()
        for j in word:
            if len(j)<5:
                print(j)
    f.close()
display()
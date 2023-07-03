# Write a program that prompts the user to enter the name of a file. Handle the FileNotFoundError exception by displaying an error message when the specified file is not found. If the file is found, read its contents and display them

s=input("enter the file name : ")

try:
    f = open(s,"r")
    print(f.read())
except FileNotFoundError as e:
    print(e)

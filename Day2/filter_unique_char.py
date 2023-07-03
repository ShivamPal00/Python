# Write a program that takes a string as input and filters out the unique characters in the string. Display the filtered characters as the output.

s=input()

a=set()

for i in range(0,len(s)):
    a.add(s[i])

print(s)
print()
print(a)

# Create a Python module named words that contains the following functions:
# first_word: Returns the first word of a string
# last_word: Returns the last word of a string
# number_of_words: Returns the length of the string
# Write a separate Python program that imports the word module and uses its functions to perform string operations on user-provided strings. Include a main function in the module that includes test cases, which should not be executed if the module is imported into another program.

import word_module as w

s=input("enter the string")

print("first word of the string is",w.first_word(s))
print("last word of the string is",w.last_word(s))
print("first word of the string is",w.total_char(s))

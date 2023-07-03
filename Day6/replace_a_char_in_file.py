#     Aditi has used a text editing software to type some text. After saving the article as WORDS.TXT, she realised that she has wrongly typed alphabet J in place of alphabet I everywhere in the article.
# Write a function definition for JTOI() in Python that would display the corrected version of entire content of the file WORDS.TXT with all the alphabets "J" to be displayed as an alphabet "I" on screen.
# Note: Assuming that WORD.TXT does not contain any J alphabet otherwise.
# Example:If Aditi has stored the following content in the file WORDS.TXT:WELL, THJS JS A WORD BY JTSELF. YOU COULD STRETCH THJS TO BE A SENTENCEThe function JTOI() should display the following content:WELL, THIS IS A WORD BY ITSELF. YOU COULD STRETCH THIS TO BE A SENTENCE

f = open("C:\Python\Day6\shivam.txt",'w')
f.write("WELL, THJS JS A WORD BY JTSELF. YOU COULD STRETCH THJS TO BE A SENTENCE")
f.close()
f = open("C:\Python\Day6\shivam.txt",'r')

file=f.read()

words = file.split()
print(words)

og_letter = 'J'
new_letter = 'I'
for i in range(len(words)):
    words[i]=words[i].replace(og_letter,new_letter)
print(words)
modified_content = file.replace(file,' '.join(words))
f.close()
mf = open("C:\Python\Day6\shivam.txt",'w')
a = mf.write(modified_content)
mf.close()
# Write a program that takes a 2D grid of characters and a target word as input. Determine if the target word exists in the grid horizontally, vertically, or diagonally. Display whether the word is found or not as the output.




s=[]

for i in range(0,3):
    r=[]
    for j in range(0,3):
        r.append(input())
    s.append(r)    
print(s)

print("enter the you want to find in matrix")
s1=input()
bool=False

# for traverse in horizontcally

if(bool==False):
   
    for i in range(0,3):
        bool=True
        for j in range(0,3):
            if(s1[j]!=s[i][j]):
                bool=False
                break
        if(bool==True):
            print("given word is present in row",i+1)
            break        
if(bool==False): 
    for i in range(0,3):
        bool=True
        for j in range(0,3):
            if(s1[j]!=s[j][i]):
                bool=False
                break
        if(bool==True):
            print("given word is present in col",i+1)
            break   
# for diagonally




if(bool==False):
    print("word is not present")
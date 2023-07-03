def reverse(s):
    s=s[::-1]
    return s

def occurrence(s,c):
    count=0
    for i in range(0,len(s)):
        if(c==s[i]):
            count=count+1

    return count        


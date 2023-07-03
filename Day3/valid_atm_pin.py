# Create a function to test if a string is a valid pin or not.
# A valid pin has:
# Exactly 4 or 6 characters.
# Only numerical characters (0-9).
# No whitespace.

def valid_atm_pin(n,bool):
    
    for i in range(0,len(n)):
        if(n[i]>='0' and n[i]<='9'):
            bool=True
        else:
            bool=False
            return bool    

    if(len(n)==4 or len(n)==6):
        bool=True
    else:
        bool=False
        return bool   
    return True 

n=input("enter the pin no")
bool=False
print(valid_atm_pin(n,bool))   




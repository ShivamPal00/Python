# You're going to write an interactive calculator! User input is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
# If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
# Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
# If the second input is not '+' or '-', again raise a FormulaError
# If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit.

class FormulaError(Exception):
    pass
def checkValidEquation(s):
    if(len(s)!=3):
        raise FormulaError("Error : inputs does not contain 3 elements")
    elif(type(float(s[0]))!=float or type(float(s[2]))!=float ):
        raise FormulaError("Error : input does not converted in float")
    elif(s[1]!='+' and s[1]!='-'):
        raise FormulaError("Error : input does not content operator ")    
try:
    s=input("enter the formula ")
    checkValidEquation(s)
    if(s[1]=='+'):
        print(float(s[0])+float(s[2]))
    elif(s[1]=='-'):
        print(float(s[0])-float(s[2]))  
except FormulaError as e:
    print(e)    



# Write a program that takes an integer as input from the user. Create a custom exception called "EvenNumberException" that is raised when the input is an even number. Handle this exception by displaying an error message


# raise

# if(n%2==0):
#     raise Exception("given no is even")
# else:
#     print("given no is odd")


#  custom Exception
class EvenNumberException(Exception):
    pass
def checkno(n):
    if(n%2==0):
        raise EvenNumberException("Error : given no is even no")

try:
    n=int(input("enetr the value "))
    checkno(n)
except EvenNumberException as e:
    print(e)    

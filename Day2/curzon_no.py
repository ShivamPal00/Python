# Write a program to establish if a given integer num is a Curzon number. If (1+2^num) is exactly divisible by (1+2*num), then num is a Curzon number.
# Example: Input: 5 Output: True  
# # 2 ** 5 + 1 = 33 
# # 2 * 5 + 1 = 11 
# # 33 is a multiple of 11


n=int(input())

num=1+pow(2,n)
den=1+(2*n)

print("  (1+2^num)is",num," "," (1+2*num) is ",den)
if(num%den==0):
    print("true")
else:
    print("false")    
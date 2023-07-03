num=str(input())

ans =0

for i in range(1,len(num)+1):
    ans=pow(int(num[i-1]),i)+ans
    print(ans)
if(ans==int(num)):
    print("given",num," is disarium no ",ans)
else:
    print("given",num," is not disarium no",ans)

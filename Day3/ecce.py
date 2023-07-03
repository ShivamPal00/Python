import re
p=re.compile('[a-z]+')
m=p.finditer('A college in Mumbai')
# print(list(m))
print()
for i in m:
    print(i.group())
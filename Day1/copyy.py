import copy


original_list =[1,2,3,4,5]
shallow_copy =copy.copy(original_list)

deep_copy =copy.deepcopy(original_list)


print(original_list)
print(shallow_copy)
print(deep_copy)



original_list[0]=10
# original_list[3][0]=40

print(original_list)
print(shallow_copy)
print(deep_copy)

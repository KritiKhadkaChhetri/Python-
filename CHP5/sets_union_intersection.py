s1 = {1, 45, 23, 67}
s2 = {23, 78, 90, 1}

# Union of two sets
#union_set = s1.union(s2)
#print("Union of s1 and s2:", union_set)  #Output: {1, 45, 67, 78, 90, 23}
print(s1.union(s2))
print(s1.intersection(s2))  #Output: {1, 23 } 
print({1,45}.issubset(s1))  #Output: True
print(s1.issuperset({1,45})) #Output: True
print(s1.difference(s2))  #Output: {67, 45}
print(s2.difference(s1))  #Output: {90, 78}
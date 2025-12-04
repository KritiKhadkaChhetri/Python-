a = (1, 2, 5, 7, 9, False, 7, "Kriti")
print(len(a))  # length of the tuple

print(a)

no = a.count(5)  # counts how many times 5 is present in the tuple
print(no)

index = a.index(7)  # returns the index of 7
print(index)

t = (5, 10, 15)
print(10 in t)   # True

print(100 in t)  # False

t = (10, 20, 30, 40)
print(t[1:3])   # (20, 30)

my_tuple = (1, 2, 3, 4, 5)
repeated = my_tuple * 3
print(repeated)  # (1, 2, 3, 4,
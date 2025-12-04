a = (1, 2, 5, 7, 9)
print(type(a))

a = ()
print(type(a)) #empty tuple

a = (1,)  #single element tuple
print(type(a))

a = (1, 2, 5, 7, 9, False, "Kriti")
(a[0]) = 23 #indexing
print(a[0]) #tuples  & strings are immutable
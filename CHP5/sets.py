s = {1,2,3,"Kriti"}
print(s)  # Output: {1, 2, 3, 'Kriti'}  
e = set() #Dont use s = {} as it creates an empty dictionary

#s = {1,2,3,4,5,5,5,5} #duplicates will be removed
#print(s)  # Output: {1, 2, 3, 4, 5}

s.add(6)  # Adding an element to the set
print(s,type(s))  # Output: {1, 2, 3, 4,
s.remove(3)  # Removing an element from the set
print(s,type(s))  
s.discard(10)  # Removing an element that may not exist (no error)
print(s,type(s))
s.pop()  # Removes and returns an arbitrary element,we cant specify which element to remove.python removes it randomly
print(s,type(s))
print(len(s))  # Output: Length of the set
s.remove(2)
print(s,type(s))
#s.clear()  # Clears the set
#print(s,type(s))  # Output: set()
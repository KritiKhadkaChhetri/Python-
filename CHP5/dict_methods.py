marks = {
"Alice": 85,
"Bob": 92,
"Charlie": 78, #dictionary = list of key-value pairs
"David": 90,
0: "Kriti"

}

#print(marks.items())  # Returns a view object of key-value pairs
print(marks.keys())   # Returns a view object of keys
print(marks.values()) # Returns a view object of values
print(marks.get("Alice"))  # Accessing value using key with get() method
print(marks.get("Eve"))  # Accessing a non-existing
marks.update({"Eve": 88})  # Adding a new key-value pair
print(marks)  # Print updated dictionary

print(marks.get("Kriti2")) #prints None
#print(marks["Kriti2"])   #KeyError: 'Kriti2'square bracket does not exist in dictionary
print(marks.pop("Bob"))  # Removes the key-value pair and returns the value
print(marks.popitem())  # Removes and returns the last inserted key-value pair
print(marks.copy())  # returns a shallow copy of  the dictionary
print(marks.setdefault("Frank", 75))  # Adds key with value if key is not present
print(marks)  # Print updated dictionary
print(marks.clear())  # Clears the dictionary
print(marks)  # Print updated dictionary
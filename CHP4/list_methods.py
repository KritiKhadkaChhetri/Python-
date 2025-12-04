friends = ["Apple", "Banana", "Kriti", "345.06", "True", "None"] 

print(friends)

friends.append("Kriti")  # adds at the end
print(friends)
# strings return new value when  we use methods but lists change their original value


l1 = [100, 2, 300, 400, 50]
#l1.sort()  # sorts the list
#l1.reverse()  # reverses the list
#l1.insert(2, 999)  # inserts 999 at index 2
#l1.pop(3)  # removes 300 from the list
#print(l1.pop(3))  # removes and returns the value removed
l1.remove(50)  # removes 50 from the list
print(l1)
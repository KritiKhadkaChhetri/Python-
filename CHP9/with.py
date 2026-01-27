f = open("file.txt")

print(f.read())
f.close()

#The same can be achieved using 'with' statement as follows:
with open("file.txt") as f:
    print(f.read())
    
#In this case, there is no need to explicitly close the file. It will be closed automatically after the nested block of code.

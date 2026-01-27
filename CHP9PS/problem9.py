with open("file.txt") as f:
    content1 = f.read()
    
with open("poem.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print("The contents of both files are identical.")
else:
    print("The contents of the files are different.")
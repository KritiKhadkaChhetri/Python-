f = open("poem.txt")

content = f.read()
if("twinkle" in content):
    print("Yes, the word 'twinkle' is present in the file.")
else:
    print("No, the word 'twinkle' is not present in the file.")
f.close()
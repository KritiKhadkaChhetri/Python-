

def rem(l, word):
    n = []
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n

l = ["apple", "banana", "cherry", "pie", "grape"]

print(rem(l, "ap"))
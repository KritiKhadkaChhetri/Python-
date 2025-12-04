s = set()

s.add(20)
s.add('20')
s.add(20.0)
print(len(s))  # Output will be {20, '20'} showing that integer and string are stored separately, but 20 and 20.0 are considered the same in the set
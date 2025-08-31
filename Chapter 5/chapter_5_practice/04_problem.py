s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

# length of the set is 2 because 20 and 20.0 are considered the same value (float)
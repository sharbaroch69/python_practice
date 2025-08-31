s1 = {1, 23}
s2 = {23, 42}


# Union
print(s1 | s2)  # {1, 23, 42}
# or
print(s1.union(s2)) # {1, 23, 42}
# Intersection
print(s1 & s2)  # {23}

# Difference
print(s1 - s2)  # {1}

# Symmetric Difference
print(s1 ^ s2)  # {1, 42}

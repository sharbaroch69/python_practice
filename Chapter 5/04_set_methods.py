s = {1, 2, 3}

# Add an element
s.add(4)

# Remove an element (raises error if not found)
s.remove(2)

# Remove an element (does nothing if not found)
s.discard(5)

# Remove and return a random element
item = s.pop()

# Clear all elements
s.clear()

# Copy a set
s2 = s.copy()

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

# Union
print(a.union(b))        # {1, 2, 3, 4, 5}
print(a | b)             # {1, 2, 3, 4, 5}

# Intersection
print(a.intersection(b)) # {3}
print(a & b)             # {3}

# Difference
print(a.difference(b))   # {1, 2}
print(a - b)             # {1, 2}

# Symmetric difference
print(a.symmetric_difference(b)) # {1, 2, 4, 5}
print(a ^ b)                    # {1, 2, 4, 5}

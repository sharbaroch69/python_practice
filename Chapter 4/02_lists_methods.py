range_list = list(range(100))

# print(range_list) 
# range_list.reverse()
# print(range_list)
# print(range_list[0:10]) # Slicing
# print(range_list[10:20])
# print(range_list[10:20:2]) # Slicing with step
print(range_list[::2]) # Slicing with step

if 99 in range_list:
    print("99 is present in the list")  
print("Found!")

# squares = [i**2 for i in range(100)]
# print(squares)

# first_names = ["Awais", "Ali", "Ahmed"]
# last_names = ["Khan", "Raza", "Ali"]
# full_names = [f"{first} {last}" for first, last in zip(first_names, last_names)]
# print(full_names)


# # Write a python function to remove a given word from a list ad strip it at the same time.
# def rem(l, name):
#     n = []
#     for item in l:
#         if item.strip() != name:
#             n.append(item.strip())
#     return n

# l = ["harry", "Awais", "Ali", "Usama"]
# name = input("Enter name to remove: ")
# print(rem(l, name))



def rem(l, name):
    n = []
    for item in l:
        if not(item == name):
            n.append(item.strip(name))
    return n

l = ["harry", "Awais", "Ali", "Usama"]

print(rem(l, "ai"))


# def rem(l, name):
#     n = []
#     for item in l:
#         if not(item == name):
#             n.append(item.strip())
#     return n
# l = ["harry", "Awais", "Ali", "Usama"]  
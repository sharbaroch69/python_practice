d = {} #empty dict
marks = {
    "Awais": 76,
    "Ali": 68,  
    "Ahmed": 70
}
print(marks.items()) # Display all key-value pairs
print(marks.keys())  # Display all keys
print(marks.values()) # Display all values
print(marks.get("Awais")) # Get value for a specific key

marks.update({"Awais": 80}) # Update value for a key
print(marks)

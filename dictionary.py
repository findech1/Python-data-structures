# Creating a dictionary
employee = {
    "name": "John Doe",
    "age": 30,
    "department": "IT",
    "location": "New York"
}

# Accessing dictionary values
print(employee["name"])
print(employee.get("age"))

# Modifying dictionary values
employee["age"] = 31
employee["location"] = "San Francisco"

# Looping through dictionary
for key, value in employee.items():
    print(key, ":", value)

# Checking if a key exists
if "department" in employee:
    print("Key 'department' exists in the dictionary")

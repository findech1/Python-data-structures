# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Set Operations
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_difference_set = set1.symmetric_difference(set2)

# Set Functions
set1.add(6)
set2.remove(7)
set3 = set1.copy()

# Display Results
print("Union Set:", union_set)
print("Intersection Set:", intersection_set)
print("Difference Set:", difference_set)
print("Symmetric Difference Set:", symmetric_difference_set)
print("Set 1 after adding 6:", set1)
print("Set 2 after removing 7:", set2)
print("Copied Set 1:", set3)

# Create two sets for demonstration
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Union of two sets
union_set = set1.union(set2)
print("Union Set:", union_set)

# Intersection of two sets
intersection_set = set1.intersection(set2)
print("Intersection Set:", intersection_set)

# Set difference (Elements in set1 but not in set2)
difference_set = set1 - set2
print("Set Difference (Set1 - Set2):", difference_set)

# Symmetric difference (Elements in either set but not in both)
symmetric_diff_set = set1.symmetric_difference(set2)
print("Symmetric Difference Set:", symmetric_diff_set)

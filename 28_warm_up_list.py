# Initialize the list
l = [1, 7, 4, 2, 100]

# Print the initial list
print(l)  # [1, 7, 4, 2, 100]

# Append elements
l.append(1024)
print(l)  # [1, 7, 4, 2, 100, 1024]

l.append(2)
print(l)  # [1, 7, 4, 2, 100, 1024, 2]

# Remove elements
l.remove(1)
print(l)  # [7, 4, 2, 100, 1024, 2]

l.remove(100)
print(l)  # [7, 4, 2, 1024, 2]

l.remove(2)
print(l)  # [7, 4, 1024, 2]

l.remove(2)
print(l)  # [7, 4, 1024]

# Initial list
l = []
l.append(1)
l.append(2)
l.append(3)

print(l)  # Output: [1, 2, 3]

# Create another list and append 'l' to it
x = []
x.append(l)
print(x)  # Output: [[1, 2, 3]]

# Append another list to x
m = [10, 20, 30]
x.append(m)
print(x)  # Output: [[1, 2, 3], [10, 20, 30]]

# Create another list and append 'x' to it
t = []
t.append(x)
print(t)  # Output: [[[1, 2, 3], [10, 20, 30]]]

# Append another list to t
t.append([100, 101, 102])
print(t)  # Output: [[[1, 2, 3], [10, 20, 30]], [100, 101, 102]]

# Accessing nested lists
print(t[0])    # Output: [[1, 2, 3], [10, 20, 30]]
print(t[1])    # Output: [100, 101, 102]

# Create an empty list
M = []

# Append sublists (like matrix rows)
M.append([1, 2, 3])
M.append([4, 5, 6])
M.append([7, 8, 9])

# Print the 2D list (matrix)
print(M)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements
print(M[0])      # Output: [1, 2, 3]
print(M[0][0])   # Output: 1
print(M[0][1])   # Output: 2
print(M[0][2])   # Output: 3

print(M[1][0])   # Output: 4
print(M[1][1])   # Output: 5

import numpy as np

image = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original Image:")
print(image)

# Reshape
reshaped = image.reshape(1, 9)
print("Reshaped Image:")
print(reshaped)

# Slicing
print("Selected Region:")
print(image[0:2, 0:2])

# Brightness Adjustment
bright = image + 20
print("Brightness Adjusted:")
print(bright)

# Broadcasting
result = image * 2
print("Broadcasting Result:")
print(result)

# Matrix Multiplication
matrix = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

transformed = np.dot(image, matrix)

print("Transformed Image:")
print(transformed)
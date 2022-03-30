import numpy as np
x = np.array([[1,2,3,4,], [5,6,7,8],[9,10,11,12], [13, 14, 15,16]])
print(x)
print("Display all elements excluding the first row")
print(x[1:])

print("Display all elements excluding the last column")
print(x[:, :3])

# Import the numpy package as np
import numpy as np


weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

# the type of np_height
print(type(np_height))

# elements wise calculation
bmi = np_weight / np_height ** 2
print("bmi elements:")
print(bmi)
print("bmi > 24: ")
print(bmi > 24)
print(np_height * 2)
print(bmi[bmi > 24]) # print the elements bigger than 24
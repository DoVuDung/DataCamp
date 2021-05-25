# Import numpy
import numpy as np
# height and weight are available as a regular lists
weight_lb = [1, 2, 3, 4, 5, 6, 7, 8, 9]
height_in = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[2])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[1:9])

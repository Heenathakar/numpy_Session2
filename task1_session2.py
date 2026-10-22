# Create a 2D NumPy array representing the ratings (out of 5)
# given by 4 users to 5 different food items on Zomato.
# Use slicing to extract the ratings given by the second and third users only.


import numpy as np 

arr=np.array([[1,2,3,2,1],
           [4,5,1,3,2],
           [5,2,1,3,4],
           [4,3,5,1,2]
           ])

print(" ratings given by the second and third users only",arr[1:3])



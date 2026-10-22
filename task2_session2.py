
# Given a NumPy array of daily steps tracked for 10 days, use boolean indexing to select only the days where the steps were greater than 8000.
#     <br><br><em><strong>Hint:</strong> Use an array like steps = np.array([7500, 8200, 9000, ...]) 
# and apply a boolean condition.</em>

import numpy as np 

step=np.array([7500, 8200, 9000,4320,4322,8000,2340,6000,9000,1200])
a=step[step>8000]
print(a)
print(step)
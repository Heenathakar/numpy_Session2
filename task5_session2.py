
'''Given a NumPy array of user ratings (can be negative, zero, or positive) 
for songs on Spotify, use boolean masking to set all negative ratings to zero, 
keeping other ratings unchanged.'''


import numpy as np 

rating=np.array([-2,0,-3,-4,5,3,2,1,-1,-5])
print("user rating",rating)
rating[rating<0]=0
print(rating)

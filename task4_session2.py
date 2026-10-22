'''Suppose you have a NumPy array of product prices
from Flipkart. 
Use broadcasting to apply a 10% discount to all prices 
and print the new array.<br><br><em><strong>Constraint:
</strong> Do not use any loops.</em'''

import numpy as np

prodcut=np.array([2000,3000,4999,1200])
print(prodcut)

print("broadcasting to apply a 10% discount",prodcut*0.90)
print(prodcut)
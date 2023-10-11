import numpy as np

a = np.array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 
       13, 14, 15, 16, 17, 18, 19, 20, 21,
       22, 23, 24, 25, 26, 27, 28, 29])

# mask1 = (a > 0) & (a < 10)

# mask2 = (a > 0) & (a < 10) | (a > 12) & ( a < 100 >)

# a[mask2]

mask = a > 3
print(sum(mask)) # sum sur des True et False il compte les True
print(a[mask])

b = np.array([[1,2,3], [4,5,6]])

print( b > 1 )
print( b[ b > 1 ] )
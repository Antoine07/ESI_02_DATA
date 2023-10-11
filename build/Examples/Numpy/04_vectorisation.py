import numpy as np

a = np.arange(100)

# compréhension de liste prends plus de temps car fait un Python
%timeit [x**2 + 2*x + 1 for x in a ]

# Vectorisation bcp plus rapide car, Numpy écrit en C optimise ses calculs
%timeit a**2 + 2*a + 1
import numpy
import math

def lsf(x):
    return 1/(1+math.exp(-x))

v=lsf(0.458)
print(v)

# this code is showing how numpy and scipy works together to produce fft

import scipy as sp
import numpy as np
from scipy.fft import fft

var1 = np.array([[2,4,6],[5,6,7]])
trans1 = fft(var1)

# fourrier transformation
print(trans1)


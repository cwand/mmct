import sys
sys.path.append("src")
import mmct

import time

import numpy as np

# Hypothsised probability

# Cumulative: 0.10  0.17  0.48  0.52  0.63  0.87, 0.89  1.00
p = np.array([0.10, 0.07, 0.31, 0.04, 0.11, 0.24, 0.02, 0.11])


# Observations

x = np.array([17,    6,    30,    4,    8,    18,    1,    14])



t0 = time.time()

t = mmct.tester()
t.n_samples = 80000

p = t.do_test(x,p)
print("Calculated p-value: {:.2f}".format(p))

t1 = time.time()

print('')
print("Time: {:.4f}s".format(t1-t0))

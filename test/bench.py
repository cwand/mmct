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

tx = mmct.tester()
tx.n_samples = 30000

p1 = tx.do_test(x,p)
print("Calculated p-value: {:.2f}".format(p1))

t1 = time.time()

ty = mmct.mt_tester()
ty.test_statistic = 'Prob'
ty.n_samples = 30000

p2 = ty.do_test(x,p)
print("Calculated p-value: {:.2f}".format(p2))

t2 = time.time()


print('')
print("Time 1: {:.4f}s".format(t1-t0))
print("Time 2: {:.4f}s".format(t2-t1))
